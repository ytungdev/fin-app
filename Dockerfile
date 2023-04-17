FROM python:latest
COPY . /opt/app/
WORKDIR /opt/app
RUN python3 -m pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

