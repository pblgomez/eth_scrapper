#!/usr/bin/env sh


poetry export -f requirements.txt -o requirements.txt

docker build -t pablogomez/${PWD##*/} .