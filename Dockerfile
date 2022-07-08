FROM python:3.8.10-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./app/store.py ./
CMD ["python3","store.py"]
