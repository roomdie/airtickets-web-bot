FROM python:3.9-slim

WORKDIR /services/bot/
COPY requirements.txt /services/bot/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /services/bot/

CMD ["python3", "main.py"]