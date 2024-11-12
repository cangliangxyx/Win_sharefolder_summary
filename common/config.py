def db_config(type):
    # DB_HOST, DB_PORT, DB_DATABASE, DB_USER, DB_PASSWORD, DB_CHARSET
    if type is None:
        db_info = ['localhost', '3306', 'samp_scan_db', 'changliang', '123123', 'utf8']
        return db_info
    if type == 'test':
        db_info = ['localhost', '3306', 'samp_scan_db', 'root', 'root', 'utf8']
        return db_info
    if type == 'dev':
        db_info = ['10.36.24.253', '3306', 'samp', 'dbpa_elp_samp', 'tmCL*b*CfC3HTwV9', 'utf8']
        return db_info
    if type == 'prod':
        db_info = ['10.36.24.253', '3306', 'samp', 'dbpa_elp_samp', 'tmCL*b*CfC3HTwV9', 'utf8']
        return db_info

def file_dir_config(type):
    if type is None:
        file_dir = 'C:\\Win_sharefolder_summary\\'
        return file_dir
    if type == 'test':
        file_dir = 'C:\\Win_sharefolder_summary\\'
        return file_dir
    if type == 'dev':
        file_dir = 'C:\\Win_sharefolder_summary\\'
        return file_dir
    if type == 'prod':
        file_dir = 'D:\\Win_sharefolder_summary\\'
        return file_dir

def uzip_folder(type):
    if type == 'test':
        file_dir = 'C:\\Win_sharefolder_summary'
        return file_dir
    if type == 'dev':
        file_dir = 'C:\\Win_sharefolder_summary'
        return file_dir
    if type == 'prod':
        file_dir = 'D:\\Win_sharefolder_summary'
        return file_dir

###sqltie_config###
def sqlite_config(type):
    if type is None:
        db_info = "C:\\sqlite_db\\example.db"
        return db_info
    if type == 'test':
        db_info = "C:\\sqlite_db\\example.db"
        return db_info
    if type == 'dev':
        db_info = "/opt/db/example.db"
    if type == 'prod':
        db_info = "D:\\sqlite_db\\samp_info.db"
        return db_info