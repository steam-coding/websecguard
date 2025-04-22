## 使用官方 Python 运行时镜像作为基础镜像
#FROM python:3.10
#
## 设置工作目录
#WORKDIR /app
#
## 复制所有项目文件到容器中
#COPY . .
#
## 安装依赖
#RUN pip install --no-cache-dir -r requirements.txt
#
## 初始化数据库（可选：写成 shell 启动脚本）
#RUN python -c "import app; app.init_db()"
#
## 容器启动时运行 Flask 服务
#CMD ["python", "app.py"]
#---------------------------------------------------------------------------------------------
# 使用官方 Python 镜像作为基础镜像
FROM python:3.10-slim

# 设置容器中的工作目录
WORKDIR /app

# 复制所有项目文件到容器中
COPY . .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 初始化数据库（首次运行）
RUN python -c "import app; app.init_db()"

# 启动应用
CMD ["python", "app.py"]
