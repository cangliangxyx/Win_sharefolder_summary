# 使用官方Python运行时作为父镜像
#FROM win_sharefolder_summary-app:latest
FROM cangliangxyx/python38:v1.0
# 设置工作目录
WORKDIR /app
# 复制项目文件到容器内
COPY . .
# 复制requirements.txt并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#挂载点
VOLUME /opt
# 声明运行时端口
EXPOSE 8090
# 定义环境变量
ENV NAME=dev
# 运行项目
CMD ["/bin/bash","/app/run.sh"]