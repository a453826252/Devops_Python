# 以python3.9.7为基础镜像
FROM python:3.9.7
# 将工作目录文件拷贝到镜像内的/DevOps_python目录下
COPY . /DevOps_python
# 声明暴露5000端口
EXPOSE 5000
# 在镜像内运行以下命令
RUN  python -m pip install --upgrade pip &&  pip install -r /DevOps_python/requirements.txt
# 在容器内运行以下命令：
CMD ["/bin/sh","-c","cd DevOps_python/src && flask run --host=0.0.0.0"]