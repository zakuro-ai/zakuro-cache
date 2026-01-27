FROM python:3.7

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

COPY ./ /workspace

WORKDIR /workspace

RUN apt update && apt install time
RUN uv pip install --system .
