from uzip_samp_folder import extract_zip
from samp_stdout_insertdb import insert_db
from clear_samp_folder import clear_directories
from common.config import uzip_folder
from traverse_folder import traverse_directory
import os

def main():
    env = os.environ.get("python_variable", "default")
    print("Please confirm the current environment. = ", env)
    input("Press Enter to continue...")
    # 解压
    extract_zip(env)
    #插入数据
    file_path = uzip_folder(env)
    print("工作目录 = ", file_path)
    # 获取zip文件列表
    zip_files = [f for f in os.listdir(file_path) if
                 f.endswith('.zip') and os.path.isfile(os.path.join(file_path, f))]
    for i in zip_files:
        extract_to_path = 'C:\\Win_sharefolder_summary\\' + os.path.splitext(i)[0]
        print("extract_to_path = ", extract_to_path)
        tabes_name = 'samp_' + os.path.splitext(i)[0][-4:]
        print("tabes_name = ", tabes_name)
        # 遍历
        folder_info = traverse_directory(extract_to_path)
        print("folder_info = ", folder_info)
        insert_db(env, folder_info, tabes_name)
    #清理
    clear_directories(env)

# 如果当前模块是主程序，就运行 main() 函数
if __name__ == "__main__":
    main()