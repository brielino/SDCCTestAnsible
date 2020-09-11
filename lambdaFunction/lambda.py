import json

# Create SQS client
import boto3

sqs = boto3.client('sqs', region_name= "us-east-2")

def lambda_handler(event,context):
    print("Hello Lambda")
    queue_url = 'https://sqs.us-east-2.amazonaws.com/419579575170/FogQueue.fifo'

    # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageGroupId="1",
        MessageDeduplicationId="1",
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'The Whistler'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'John Grisham'
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody=(
            'Information about current NY Times fiction bestseller for '
            'week of 12/11/2016.'
        )
    )
    print(response['MessageId'])
    return{
        'statusCode':200,
        'body': json.dumps("Hello from Lambda")
    }