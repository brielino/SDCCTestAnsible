#!/bin/sh
export FLASK_APP=server.py
sudo -E python3 -m flask run -h 0.0.0.0 -p 80
#python3 -m flask run -h 0.0.0.0 -p 5000
