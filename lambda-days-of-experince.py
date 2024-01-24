import time
import math
import datetime
from datetime import date


def lambda_handler(event, context):
    print("This is my AWSlambda function")
    today = date.today()
    print(today)
    start = datetime.date(2009, 1, 8)
    days_of_expreince = today - start
    print("I have")
    print(days_of_expreince.days)
    print("days of experince")