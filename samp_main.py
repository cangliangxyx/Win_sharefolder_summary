import os
from samp_insert_mysql import insert_mysql
from samp_clear_folder import clear_directories
from samp_traverse_folder import traverse_directory
from zip_file_info import zip_file_list
from extract_files import extract_zip

def main():
    env = os.environ.get("python_variable", "default")
    print("Please confirm the current environment. = ", env)
    input("Press Enter to continue...")
    # 解压
    extract_zip(env)

    # 获取zip文件列表
    zip_files = zip_file_list("test")
    for i in zip_files:
        traverse_to_path = 'C:\\Win_sharefolder_summary\\' + os.path.splitext(i)[0]
        # 遍历目录
        insert_file_list = traverse_directory(traverse_to_path)
        # 获取表名
        tabes_name = 'samp_' + os.path.splitext(i)[0][-4:]
        #开始插入
        insert_mysql("test", insert_file_list, tabes_name)

    #清理
    clear_directories(env)

# 如果当前模块是主程序，就运行 main() 函数
if __name__ == "__main__":
    main()