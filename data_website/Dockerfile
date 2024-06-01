# Dockerfile
FROM python:3.9

# 設置工作目錄
WORKDIR /code

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# 複製當前目錄的所有內容到 /code
COPY . /code/

# 暴露8000端口
EXPOSE 8000

# Migration
RUN python manage.py makemigrations
# 默認命令
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
