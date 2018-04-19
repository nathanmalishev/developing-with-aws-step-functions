from __future__ import print_function
import random

def lambda_handler(event, context):
    # Generating a ramdom score. This would otherwise be calling an external system.
    exam_score = random.randint(0,100)
    event['exams'][-1]['score'] = exam_score
    event['last_exam_score'] = exam_score
    return event