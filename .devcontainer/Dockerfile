FROM python:latest
COPY requirements.txt /opt/app/requirements.txt
COPY secrets.json /opt/app/secrets.json
WORKDIR /opt/app
RUN python3 -m pip install -r requirements.txt

