# -*-coding:utf-8-*-
import pymysql
from DBUtils.PooledDB import PooledDB
from common.config import db_config

class MysqlConn(object):
    def __init__(self, db_con_info):
        try:
            self.db_info = db_config(db_con_info)
            self.pool = self.create_pool
            self.con = self.pool.connection()
            self.cur = self.con.cursor(cursor=pymysql.cursors.DictCursor)
        except pymysql.MySQLError as e:
            print(e.args)

    @property
    def create_pool(self):
        """
        创建数据库连接池
        :return: 连接池
        """
        pool = PooledDB(creator=pymysql,
                        maxconnections=15,  # 连接池允许的最大连接数，0和None表示不限制连接数
                        mincached=10,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
                        maxcached=0,  # 链接池中最多闲置的链接，0和None不限制
                        maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
                        blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
                        use_unicode=True,
                        host=self.db_info[0],
                        port=int(self.db_info[1]),
                        db=self.db_info[2],
                        user=self.db_info[3],
                        passwd=self.db_info[4],
                        charset=self.db_info[5])
        return pool

    def find_key_val(self, table, key_val):
        sql = None
        if isinstance(key_val, str):
            sql = 'SELECT * FROM `%s` WHERE %s ;' % (table, key_val)
            print('SQL = ', sql)
        elif isinstance(key_val, dict):
            sql_where = ''
            for item in key_val.items():
                row_str = str(item[0]) + '=' + str(item[1]) + ' and '
                sql_where += row_str
            sql_where = sql_where[:-4]
            sql = 'SELECT * FROM `%s` WHERE %s ;' % (table, sql_where)
            print(sql)
        if sql:
            try:
                self.cur.execute(sql)
                data = self.cur.fetchall()
                if len(data) > 0:
                    return data
                return None
            except pymysql.MySQLError as e:
                print(e.args)
            finally:
                self.cur.close()
                self.con.close()
        return None

    def find_by_sql(self, sql):
        if sql:
            try:
                self.cur.execute(sql)
                data = self.cur.fetchall()
                if len(data) > 0:
                    return data
                return None
            except pymysql.MySQLError as e:
                print(e.args)
            finally:
                self.cur.close()
                self.con.close()
        return None

    def update_by_sql(self, sql):
        if sql:
            try:
                self.cur.execute(sql)
                self.con.commit()
                return True
            except pymysql.MySQLError as e:
                print(e.args)
                self.con.rollback()
            finally:
                self.cur.close()
                self.con.close()
        return

    def del_by_sql(self, sql):
        if sql:
            try:
                self.cur.execute(sql)
                self.con.commit()
                return True
            except pymysql.MySQLError as e:
                print(e.args)
                self.con.rollback()
            finally:
                self.cur.close()
                self.con.close()
        return None

    def truncate_by_sql(self, sql):
        if sql:
            try:
                self.cur.execute(sql)
                self.con.commit()
                return True
            except pymysql.MySQLError as e:
                print(e.args)
                self.con.rollback()
            finally:
                self.cur.close()
                self.con.close()
        return None#读取配

# dbconn = MysqlConn('test')
# sql1 = "INSERT INTO azure_uuid (uuid, name, id) VALUES ('test_id4', 'test_name4', 'test_uuid4')"
# sql2 = "select * from samp_stdout"
# dbconn.update_by_sql(sql1)
# file_json = dbconn.find_by_sql(sql2)
# for i in file_json:
#     print(i)
# print(dbconn.find_key_val("samp_stdout","hostname = 'VDI-T-VM-VDA01' ")[0])
# print(dbconn.db_info())