from flask import Flask, render_template, request
import os
from samp_stdout_insertdb import insert_db
os.environ['config_env'] = "localhost"
app = Flask(__name__)
db_name = os.environ.get('config_env')
print(db_name)

@app.route("/")
def index():
    flask_data = 'infra-数据接口,运行环境:%s' % (os.environ.get('config_env'))
    return render_template('index.html', flask_data=flask_data)

@app.route('/insert_stdout', methods=['POST'])
def insert_stdout():
    # 在这里编写触发的脚本逻辑
    print("开始插入")
    insert_db('test')
    return render_template('insert_stdout.html')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8090,
        debug=True
    )
