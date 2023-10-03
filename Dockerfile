# 使用基础镜像
FROM python:3.9

# 在容器中创建一个工作目录
WORKDIR /app

# 将代码复制到工作目录中
COPY . /app

# Install necessary dependencies
RUN apt-get update && apt-get install -y ffmpeg


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# 运行处理逻辑的命令
CMD ["python", "audio_processing.py"]
