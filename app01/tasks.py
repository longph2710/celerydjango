# ce/taks.py
# Create your tasks here
from celery import shared_task

import time
from datetime import datetime
import requests
import json

@shared_task
def add(x, y):
    time.sleep(5)
    return x + y

@shared_task
def mul(x, y):
    time.sleep(5)
    return x * y

@shared_task
def xsum(numbers):
    time.sleep(5)
    return sum(numbers)

@shared_task
def perform_backup(database_id, url):
    time_start = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+07:00")
    time.sleep(5)
    backup_id = database_id
    time_finish = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+07:00")
    data = {
        "database_id": database_id,
        "backup_id": backup_id,
        "time_start": time_start,
        "time_finish": time_finish
    }
    print(data)
    requests.post(url=url, json=data)