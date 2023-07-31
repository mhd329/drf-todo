FROM python:alpine3.10

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

COPY . .

EXPOSE 8000