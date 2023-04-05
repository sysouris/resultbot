FROM python:3.10-slim

WORKDIR /ResultBot

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "ResultBot.py"]

EXPOSE 8051/tcp
