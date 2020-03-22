"""Platzigram URLs module."""
# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs'))
    ))


def sort_integers(request):
    """Return a JSON response with sorted integers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_insts = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_insts,
        'message': 'Integers sorted successfully.'
    }

    return HttpResponse(
        json.dumps(data, indent=2),
        content_type='application/json')


def say_hi(request, name, age):
    """Return a greetin"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)
