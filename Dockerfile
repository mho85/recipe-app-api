FROM python:3-alpine

# Recommended for Python in Docker
ENV PYTHONUNBUFFERED 1

# Copy from (local) to (container docker) 
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Source code
RUN mkdir /src
WORKDIR /src
COPY ./src /src

# Create user for safety
RUN adduser -D user
USER user