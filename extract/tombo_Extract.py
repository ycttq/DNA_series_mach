import h5py
import os
import numpy as np
import pandas as pd

def get_Group_Signal(name):
    """
    查找Signal所在Group的名称
    :param name:
    :return:
    """
    key = 'Signal'
    if name.find(key) != -1:
        return name

def signal_Extract(file):
    """
    单个Fast5文件
    从Signal中提取碱基对应的信号
    :param file: 文件名称
    :return: 信号,碱基
    """
    hdf = h5py.File(file, 'r')
    if hdf.get('Analyses/RawGenomeCorrected_001/BaseCalled_template/Events') != None:
        # 每个碱基信息
        Events = hdf['/Analyses/RawGenomeCorrected_001/BaseCalled_template/Events'][()]
        # Signal碱基信号开始位置
        startPos= hdf['/Analyses/RawGenomeCorrected_001/BaseCalled_template/Events'].attrs['read_start_rel_to_raw']
        # 获取Signal所在的组,read_*
        signal_Group = hdf.visit(get_Group_Signal)
        Signal = hdf[signal_Group][()]

        nd_Events = []
        # 转为二维数组
        for i in Events:
            nd_Events.append(list(i))
        nd_Events = np.array(nd_Events)

        start = np.array(nd_Events[:, 2], dtype='int64') + startPos
        length = np.array(nd_Events[:, 3], dtype='int64')
        end = start + length
        base = np.array(nd_Events[:,4],dtype=np.str)

        perSignal = []
        perBase = []
        for index in range(0, len(nd_Events)):
            # res.append((Signal[start[index]:end[index]].tolist(), dna[index]))
            perSignal.append(Signal[start[index]:end[index]].tolist())
            perBase.append(base[index])
        # 转为dataFrame格式
        res = {'perSignal':perSignal,'perBase':perBase}
        res_Extract = pd.DataFrame(res)
        print("碱基个数：{}".format(res_Extract.shape[0]))
        return res_Extract,1
    else:
        print('{}未被tombo识别...'.format(file))
        return None,0

if __name__ == '__main__':

    tombo_output_path = './passFast5/'
    csv_Path = './perSignal_Extract/'

    # 获取每个文件
    # for path, dirs, files in os.walk(tombo_output_path):
    #     for file in files:
    #         filelist.append(os.path.join(path, file))
    count = 0
    for i in range(0,8):
        tombo_output_dir = tombo_output_path + str(i) + '/'
        files = os.listdir(tombo_output_dir)
        print('文件个数：{}'.format(len(files)))

        for file in files:
            hdf = h5py.File(tombo_output_dir + file, 'r')
            print('---------     {}     ------------'.format(tombo_output_dir + file))
            signal_csv = file.split('.')[0] + '.csv'
            perSignal_Extrace, exist = signal_Extract(tombo_output_dir + file)
            if exist:
                perSignal_Extrace.to_csv(csv_Path + signal_csv, index=False,encoding='utf-8')
            count += 1
    print('共提取{}个文件'.format(count))
