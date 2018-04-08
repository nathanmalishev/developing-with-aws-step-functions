from __future__ import print_function
import os
import uuid
from datetime import datetime
import boto3
# from aws_xray_sdk.core import patch_all, xray_recorder

# Patch all supported libraries for X-Ray - More info: https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-patching.html
# patch_all()

incidents_table = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(incidents_table)


def lambda_handler(event, context):

    incident_date = datetime.strptime(event['incident_date'], "%Y-%m-%d").strftime('%Y-%m-%dT%H:%M:%SZ')
    student_id = event['student_id']

    return create_incident(incident_date, student_id)

#@xray_recorder.capture('put_item')
def create_incident(incident_date, student_id):

    # Persist new incident
    new_incident = {
        "incident_id": str(uuid.uuid4()),
        "incident_date": incident_date,
        "student_id": student_id,
        "incident_resolved": False
    }

    table.put_item(
        Item=new_incident
    )

    return new_incident
