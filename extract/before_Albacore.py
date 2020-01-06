import shutil
import os

source_path = './source/'
source = os.listdir(source_path) # 0-7999
albacore_input = './rawSignal/'
albacore_output = './fast5_albacore/'

'''
将source目录下的复制到fast5_albacore下面，1000个一组
'''
shutil.rmtree(albacore_input)
shutil.rmtree(albacore_output)
for i in range(0, len(source)):
    input_dir = albacore_input + str(int(i/1000))
    ouput_dir = albacore_output + str(int(i/1000))
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
    shutil.copy(source_path + source[i], input_dir)

    if not os.path.exists(ouput_dir):
        os.makedirs(ouput_dir)