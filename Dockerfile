FROM python:3-alpine

# Recommended for Python in Docker
ENV PYTHONUNBUFFERED 1

# Copy from (local) to (container docker) 
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Source code
RUN mkdir /src
WORKDIR /src
COPY ./src /src

# Create user for safety
RUN adduser -D user
USER user