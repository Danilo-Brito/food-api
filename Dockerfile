FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

ENV FLASK_APP=food.py

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]
