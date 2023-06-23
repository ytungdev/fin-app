#!/bin/bash

python3 manage.py makemigrations accounts
python3 manage.py makemigrations cashs
python3 manage.py makemigrations currencies
python3 manage.py makemigrations stocks

python3 manage.py migrate