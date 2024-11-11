import os
from common.config import uzip_folder

def zip_file_list(env):
    file_path = uzip_folder(env)
    #获取zip文件列表
    files_list = [f for f in os.listdir(file_path) if
                 f.endswith('.zip') and os.path.isfile(os.path.join(file_path, f))]
    return files_list

def z7_file_list(env):
    file_path = uzip_folder(env)
    #获取7z文件列表
    files_list = [f for f in os.listdir(file_path) if
                 f.endswith('.7z') and os.path.isfile(os.path.join(file_path, f))]
    return files_list