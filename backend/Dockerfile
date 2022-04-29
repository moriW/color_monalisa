FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8888

CMD ["python", "app.py"]