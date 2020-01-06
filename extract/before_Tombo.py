import shutil
import os

tombo_input_path = './passFast5/'
'''
将albacore识别成功的文件复制到passFast5下
'''
shutil.rmtree(tombo_input_path)
for i in range(0,8):
    input_dir = tombo_input_path + str(i)
    albacore_output_files = './fast5_albacore/{}/workspace/pass/0/*'.format(i)
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
    os.system('cp -r {} {}'.format(albacore_output_files, input_dir))
