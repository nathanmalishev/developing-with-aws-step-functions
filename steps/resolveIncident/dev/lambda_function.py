from __future__ import print_function
from datetime import datetime
import os
import uuid
import boto3

incidents_table = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(incidents_table)


def lambda_handler(event, context):

    event['incident_resolved'] = True
    event['resolution_date'] = (datetime.now()).strftime('%Y-%m-%dT%H:%M:%SZ')

    # update incident
    # table.update_item(
    #     Key={
    #         'incident_id': event['incident_id']
    #     },
    #     UpdateExpression='SET incident_resolved = :val1, resolution_date = :val2',
    #     ExpressionAttributeValues={
    #         ':val1': True,
    #         ':val2': (datetime.now()).strftime('%Y-%m-%dT%H:%M:%SZ')
    #     }
    # )

    # updated_event = table.get_item(
    #     Key={
    #         'incident_id': event['incident_id'] 
    #     }
    # )
    
    # return updated_event
    return event