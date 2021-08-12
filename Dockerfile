FROM python:3.9.1
ADD . /flask-project
WORKDIR /flask-project
RUN pip install -r requirements.txt