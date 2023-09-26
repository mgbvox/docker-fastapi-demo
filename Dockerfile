FROM python:3.7

RUN mkdir "api"

WORKDIR api

COPY src/* .

RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["python", "main.py"]



