#!/usr/bin/env sh

pipenv lock -r > requirements.txt
docker build -t pablogomez/eth_scrapper:latest .
