import zipfile
# import py7zr
import os
from common.config import uzip_folder

def extract_zip(env):
    print("当前环境 = ", env)
    file_path = uzip_folder(env)
    print("工作目录 = ", file_path)
    #获取zip文件列表
    zip_files = [f for f in os.listdir(file_path) if
                 f.endswith('.zip') and os.path.isfile(os.path.join(file_path, f))]

    for i in zip_files:
        # extract_to = file_path+'\\'+extract_to
        zip_files_name = 'C:\\Win_sharefolder_summary\\'+i
        print("zip_files_name = ", zip_files_name)
        extract_to_path = 'C:\\Win_sharefolder_summary\\'+os.path.splitext(i)[0]
        print("extract_to_path = ", extract_to_path)
        #建立解压目录
        os.makedirs(extract_to_path, exist_ok=True)

        # 使用 py7zr 解压
        # with py7zr.SevenZipFile(file_path+'\Win_sharefolder_summary.7z', mode='r') as archive:
        #     archive.extractall(path=extract_to)
        #     print(f"Extracted {file_path} to {extract_to}")

        # 使用 zip 解压
        try:
            os.makedirs(extract_to_path, exist_ok=True)  # exist_ok=True 表示如果目录存在不会抛出异常
            print(f"目录已创建：{os.path.abspath(extract_to_path)}")
        except Exception as e:
            print(f"创建目录时出错: {e}")
        with zipfile.ZipFile(zip_files_name, 'r') as zip_ref:
            zip_ref.extractall(extract_to_path)
            print(f"文件已解压缩到: {os.path.abspath(extract_to_path)}")
        print("######unzip end######")

# extract_zip('test')

# 示例，指定 .7z 文件路径和解压目标目录
# extract_7z('test')