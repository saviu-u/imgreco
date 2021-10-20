FROM python:3.8

ENV LANG C.UTF-8
ENV TZ=America/Sao_Paulo
ENV xterm=xterm-256color
ENV TF_CPP_MIN_LOG_LEVEL=2

# Opencv dependencies
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

RUN pip3 install Pillow Flask opencv-python requests imageai numpy tensorflow

RUN mkdir /app
COPY . /app
WORKDIR /app

ENTRYPOINT [ "python", "main.py" ]