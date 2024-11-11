import os
import zipfile
import py7zr
from zip_file_info import zip_file_list, z7_file_list

def extract_7z(env):
    files_list = z7_file_list(env)
    for i in files_list:
        print(i)
        z7_files_name = 'C:\\Win_sharefolder_summary\\'+i
        print("zip_files_name = ", z7_files_name)
        extract_to_path = 'C:\\Win_sharefolder_summary\\'
        print("extract_to_path = ", extract_to_path)
        #建立解压目录
        os.makedirs(extract_to_path, exist_ok=True)
        # 使用 py7zr 解压
        with py7zr.SevenZipFile(z7_files_name, mode='r') as archive:
            archive.extractall(path= extract_to_path)
    print("######unzip end######")

def extract_zip(env):
    files_list = zip_file_list(env)
    for i in files_list:
        zip_files_name = 'C:\\Win_sharefolder_summary\\'+i
        extract_to_path = 'C:\\Win_sharefolder_summary\\'+os.path.splitext(i)[0]
        #使用 zipfile 解压
        try:
            os.makedirs(extract_to_path, exist_ok=True)  # exist_ok=True 表示如果目录存在不会抛出异常
            print(f"目录已创建：{os.path.abspath(extract_to_path)}")
        except Exception as e:
            print(f"创建目录时出错: {e}")
        with zipfile.ZipFile(zip_files_name, 'r') as zip_ref:
            zip_ref.extractall(extract_to_path)
            print(f"文件已解压缩到: {os.path.abspath(extract_to_path)}")
        print("######unzip end######")

# extract_zip("test")