from __future__ import print_function
import os
import boto3

client = boto3.client('sns')
topic = os.environ['TOPIC_ARN']


def lambda_handler(event, context):

    message = "Sending exam notification for %s" % event['student_id']
    subject = "Exam Notification for %s" % event['student_id']
    print(message)

    client.publish(
        TopicArn=topic,
        Message=message,
        Subject=subject
    )

    return event
