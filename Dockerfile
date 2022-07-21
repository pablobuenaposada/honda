FROM python:3.10.4

WORKDIR /usr/src/app

COPY src /usr/src/app/src
COPY Makefile requirements.txt requirements-tests.txt /usr/src/app/

RUN make venv
