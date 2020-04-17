#!/bin/bash

docker run -it --rm -v "$PWD":/usr/src/app -w /usr/src/app python:3 python main.py