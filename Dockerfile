FROM python:3.13.0a4

COPY ./ /workspace

WORKDIR /workspace

RUN apt update && apt install time
RUN python setup.py install
