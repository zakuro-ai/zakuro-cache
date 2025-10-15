FROM python:3.14.0

COPY ./ /workspace

WORKDIR /workspace

RUN apt update && apt install time
RUN python setup.py install
