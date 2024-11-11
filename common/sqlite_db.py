import sqlite3
from common.config import sqlite_config

class SQLiteConn:
    def __init__(self, env):
        """
        初始化连接并创建数据库连接。
        """

        self.db_name = sqlite_config(env)
        self.connection = None
        self.connect()

    def connect(self):
        """
        创建数据库连接。
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            print(f"Connected to database '{self.db_name}'.")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def execute_query(self, query, params=()):
        """
        执行 SQL 查询并提交更改。适用于插入、更新、删除操作。
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully.")
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
        finally:
            cursor.close()

    def fetch_all(self, query, params=()):
        """
        执行 SQL 查询并返回所有结果。适用于 SELECT 查询。
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return []
        finally:
            cursor.close()

    def close(self):
        """
        关闭数据库连接。
        """
        if self.connection:
            self.connection.close()
            print(f"Connection to '{self.db_name}' closed.")
            self.connection = None

    def __del__(self):
        """
        析构方法，确保对象被销毁时关闭连接。
        """
        self.close()

#
# 示例使用
# if __name__ == "__main__":
#     # 创建数据库连接对象
#     db = SQLiteConn('test')
#
#     # 查询数据
#     sql = "SELECT count(*) FROM samp_stdout"
#     results = db.fetch_all(sql)
#     for row in results:
#         print(row)
#
#     # 关闭连接
#     db.close()
