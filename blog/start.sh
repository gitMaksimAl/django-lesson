#! /bin/bash

source ../.venv/bin/activate;
while read -r line;
do
    export $line;
done < ".env";
gunicorn -D blog.wsgi -b $HOST:$PORT
