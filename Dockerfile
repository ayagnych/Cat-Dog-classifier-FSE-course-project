FROM ubuntu:22.04

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app
RUN apt-get update && apt-get install -y make
COPY Makefile preprocessing.cpp script.py model.h5 requirements.txt postprocessing.cpp /app/
COPY input_raw /app/input_raw
COPY test /app/test

RUN make prereqs

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
