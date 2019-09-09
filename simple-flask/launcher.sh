#!/bin/bash

if [ ! -f /debug0 ]; then
  touch /debug0

  while getopts 'hd:' flag; do
    case "${flag}" in
      h)
        echo "options:"
        echo "-h        show brief help"
        echo "-d        debug mode, no nginx or uwsgi, direct start with 'python3 app/app.py'"
        exit 0
        ;;
      d)
        touch /debug1
        ;;
      *)
        break
        ;;
    esac
  done
fi

if [ -e /debug1 ]; then
  echo "Running app in debug mode!"
  python app/app.py
else
  echo "Running app in production mode!"
  nginx && uwsgi --ini /app.ini
fi