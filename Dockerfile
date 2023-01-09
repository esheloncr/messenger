FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /messenger
COPY requirements.txt /messenger/
RUN pip3 install -r requirements.txt
COPY . /messenger/