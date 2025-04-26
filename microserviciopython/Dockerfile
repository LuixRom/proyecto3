FROM python:3-slim
WORKDIR /app
COPY . .
RUN pip3 install flask
RUN mkdir /data
RUN python3 db.py
CMD ["python3", "app.py"]
