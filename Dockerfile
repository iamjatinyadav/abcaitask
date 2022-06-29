FROM python:3.10.0
ENV PYTHONUNBUFFERED=1
RUN mkdir /abcai
WORKDIR /abcai
ADD . /abcai
COPY ./requirements.txt /abcai/requirements.txt
RUN pip install -r requirements.txt
COPY . /abcai/