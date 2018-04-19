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

    exam = {
        "exam_id": str(uuid.uuid4()),
        "exam_date": (datetime.now() + timedelta(seconds=10)).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "score": 0
    }

    if 'exams' in event:
        if len(event['exams']) >= 3:
            raise StudentExceededAllowableExamRetries('Student cannot take more than 3 exams')
        else:
            event['exams'].append(exam)
    else:
        event['exams'] = [exam]

    return event


class StudentExceededAllowableExamRetries(Exception):
    pass