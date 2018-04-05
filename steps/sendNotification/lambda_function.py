from __future__ import print_function


def lambda_handler(event, context):
    print ("Sending exam notification for %s", event['student_id'])
    return event
