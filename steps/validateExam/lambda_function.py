from __future__ import print_function
import random


def get_random_score():
    options = [67, 0, 60]
    return options[random.randint(0, len(options)-1)]


def lambda_handler(event, context):
    event['score'] = get_random_score()
    return event
