from __future__ import print_function
from datetime import datetime
from datetime import timedelta
import os
import uuid
import boto3

incidents_table = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(incidents_table)


def lambda_handler(event, context):

    response = table.get_item(
        Key={
            'incident_id': event['incident_id']
        }
    )

    incident = response['Item']
    exam = {
        "exam_id": str(uuid.uuid4()),
        "exam_date": (datetime.now() + timedelta(seconds=10)).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "score": 0
    }

    if 'exams' in incident:
        if len(incident['exams']) > 3:
            raise Exception() # Student cant take mor ethan 3 exams
        else:
            incident['exams'].append(exam)
    else:
        incident['exams'] = [exam]

    table.put_item(
        Item=incident
    )

    return event
