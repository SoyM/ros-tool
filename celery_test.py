from __future__ import absolute_import, unicode_literals

import celery

app = celery.Celery('tasks', backend='redis', broker='redis://192.168.1.106:6379')

app.conf.update(
    result_expires=3600,
)



@app.task
def first():
    print("hello world")
    
@app.task
def add(x, y):
    return x + y
