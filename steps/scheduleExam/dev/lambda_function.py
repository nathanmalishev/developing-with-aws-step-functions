from __future__ import print_function
from datetime import datetime
from datetime import timedelta
import uuid
import boto3

incidents_table = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(incidents_table)


def lambda_handler(event, context):
    print(event)


    response = table.get_item(
        Key={
            'incident_id': event['incident_id']
        }
    )

    incident = response['Item']

    exam = {
        exam_id = str(uuid.uuid4()),
        exam_date = (datetime.now() + timedelta(seconds=10)).strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    incident['exams'].append(exam)

    table.update_item(
        Key={
            'username': 'janedoe',
            'last_name': 'Doe'
        },
        UpdateExpression='SET age = :val1',
        ExpressionAttributeValues={
            ':val1': 26
        }
    )

    return event
