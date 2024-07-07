FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=food.py

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]