from flask import Flask, request
import socket
import json

data = ""
SensorID = 0
Name = ""
Surname = ""
Sensors = []
Lat = 0
Long = 0


def createSensor():
    global data, Name, Surname, SensorID, Sensors
    with open('attributes.json') as configFile:
        data = json.load(configFile)
        SensorID = data['Id']
        Name = data['Name']
        Surname = data['Surname']
        Sensors = data['Sensors']
        configFile.close()


createSensor()
