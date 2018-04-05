from __future__ import print_function


def lambda_handler(event, context):
    print("Taking administrative action against %s", event['student_id'])
    return event
