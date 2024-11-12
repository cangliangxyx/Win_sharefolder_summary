import csv, os
from datetime import date
from common.query_db import MysqlConn
from aifc import Error

today = date.today()
date_str = today.strftime('%Y-%m-%d')
columns = ['Hostname', 'ScopeName', 'ShareState', 'Name', 'Path', 'Description', 'date_time']

def insert_mysql(env,file_info, table_name):
    for i in file_info:
        with open(i, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                dbconn = MysqlConn(env)   # mysql
                row[4] = ('%s'+'/') % row[4]
                row.append(date_str)
                stdout_data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                sql = 'INSERT INTO {} ({}) VALUES ({}{}{})'.format(table_name, ', '.join(columns), '"', '","'.join(stdout_data), '"')
                # print("update_sql =", sql)
                try:
                    dbconn.update_by_sql(sql)
                except Error as e:
                    print("插入失败:", e)
    print(table_name , "表完成插入数据" )


# from zip_file_info import zip_file_list
# from samp_traverse_folder import traverse_directory
# from common.config import file_dir_config
#
# env = "dev"
# file_path = file_dir_config(env)
# print("工作目录 = ", file_path)
#
# # 获取zip文件列表
# zip_files = zip_file_list(env)
# for i in zip_files:
#     print(i)
#     traverse_to_path = file_path + os.path.splitext(i)[0]
#     print("traverse_to_path = ", traverse_to_path)
#     # 遍历目录
#     insert_file_list = traverse_directory(traverse_to_path)
#     print("folder_info = ", insert_file_list)
#     # 开始插入(表明忽略大小写)
#     tabes_name = 'samp_' + os.path.splitext(i)[0][-4:]
#     print("tabes_name = ", tabes_name)
#     insert_mysql(env, insert_file_list, tabes_name.lower())
