#!/bin/bash
# run with gunicorn (http://docs.gunicorn.org/en/stable/run.html#gunicorn)
pwd
exec gunicorn --chdir app  -b :5000 flask-api:app