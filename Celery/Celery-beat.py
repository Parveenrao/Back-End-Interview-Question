"""  
=> Celery Beat
   
    -> Celery beat is a scheduler for celery 
    
    -> It let you run task periodically (like cron jobs)
    
    -> Run this task every 5 min / every day / every hour

----------------------------------------------------------------------------------

=> Celey worker =  execute taks 
=> Celery Beat =   schedule task

---------------------------------------------------------------------------------

 => Real-world things  do with Celery Beat:

     Send daily emails (reports, reminders)
     Clean expired sessions/tokens
     Sync data from APIs every hour
     Generate analytics reports
     Retry failed payments   



"""


# celery_app.py
from celery import Celery

app = Celery(
    "myapp",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)




@app.task
def print_hello():
    print("Hello every 10 seconds!")
    
# add beat schedule 

# celery_app.py

from celery.schedules import crontab

app.conf.beat_schedule = {
    'say-hello-every-10-seconds': {
        'task': 'tasks.print_hello',
        'schedule': 10.0,  # seconds
    },
    'daily-task': {
        'task': 'tasks.print_hello',
        'schedule': crontab(hour=7, minute=30),  # every day 7:30 AM
    },
}    