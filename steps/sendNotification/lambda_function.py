from __future__ import print_function
import os
import boto3

incidents_table = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(incidents_table)
client = boto3.client('sns')
topic = os.environ['TOPIC_ARN']


def lambda_handler(event, context):

    response = table.get_item(
        Key={
            'incident_id': event['incident_id']
        }
    )
    
    incident = response['Item']
    
    scheduled_exam = {
        "incident_id": incident['incident_id'],
        "exam": incident['exams'][-1]
    }
    
    message = "Dear Student ID {0}, you have until {1} to complete you Plagiarism Violation test. Thank you.".format(event['student_id'], scheduled_exam['exam']['exam_date'])
    subject = "Exam Notification for %s" % event['student_id']

    client.publish(
        TopicArn=topic,
        Message=message,
        Subject=subject
    )

    return  scheduled_exam