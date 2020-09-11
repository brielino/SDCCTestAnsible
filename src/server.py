import json
from decimal import Decimal

import boto3

#import dbConnection
from dbConnection import loadItems
from dbConnection import database
from flask import Flask

from dbConnection.MovieQuery import query_movies

server = Flask(__name__)


@server.route("/populateDb")
def populateDb():
    """
    movies = query_movies(2013)
    finalist = []
    for movie in movies:
        finalist.append(str(movie['year']) + ":" + movie['title'])
    return "<p>" + "</p><p>".join(finalist) + "</p>"
    """
    # database.create_movie_table()
    with open("/home/paolo/PycharmProjects/SDCC/dbConnection/moviedata.json") as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)
    loadItems.load_movies(movie_list)
    movies = query_movies(2013)
    finalist = []
    for movie in movies:
        finalist.append(str(movie['year']) + ":" + movie['title'])
    return "<p>" + "</p><p>".join(finalist) + "</p>"


@server.route("/pollQueue")
def pollQueue():
    # Create SQS client
    sqs = boto3.client('sqs', region_name= "us-east-2")

    queue_url = 'https://sqs.us-east-2.amazonaws.com/419579575170/FogQueue.fifo'

    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=60,
        WaitTimeSeconds=0
    )
    print(response)
    if 'Messages' in response :
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']

        # Delete received message from queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        print('Received and deleted message: %s' % message)
        return ('Received and deleted message: %s' % message)
    return("Empty")

@server.route("/")
def hello():
    return("Hello from aws")


if __name__ == "__main__":
    server.run(host='0.0.0.0', port=8080)
