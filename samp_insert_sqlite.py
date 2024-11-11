import csv
from datetime import date
# from common.config import file_dir_config
# from common.sqlite_db import SQLiteConn
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
                # dbconn = SQLiteConn(env)    # sqlite
                row[4] = ('%s'+'/') % row[4]
                row.append(date_str)
                stdout_data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                # print("stdout_data = ", stdout_data)
                # sql = 'INSERT INTO {} ({}) VALUES ({}{}{})'.format(
                #     table_name,
                #     ', '.join(columns),
                #     '"',
                #     '","'.join(stdout_data),
                #     '"') # mysql
                # sql = 'INSERT OR IGNORE INTO {} ({}) VALUES ({}{}{})'.format(
                sql = 'INSERT INTO {} ({}) VALUES ({}{}{})'.format(
                    table_name,
                    ', '.join(columns),
                    '"',
                    '","'.join(stdout_data),
                    '"'
                ) # sqlite
                print("update_sql =", sql)
                try:
                    dbconn.update_by_sql(sql)   #mysql
                    # dbconn.execute_query(sql)   #sqlite
                except Error as e:
                    print("插入失败:", e)
            print("插入数据完成")

# insert_db('test')
