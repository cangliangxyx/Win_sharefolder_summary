import os
import shutil
from common.config import uzip_folder

#数据插入完成后进行清理
def clear_directories(env):
    path = uzip_folder(env)
    # 列出指定路径下的所有文件和目录.
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        # 判断是否为目录
        if os.path.isdir(item_path):
            try:
                shutil.rmtree(item_path)  # 删除目录及其所有内容
                print(f"Deleted directory: {item_path}")
            except Exception as e:
                print(f"Error deleting directory {item_path}: {e}")
    print("clear end")

