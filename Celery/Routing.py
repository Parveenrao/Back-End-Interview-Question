"""   
   => In real systems, not all tasks are equal:

            Payment → 🔥 HIGH priority
            Email → 🐢 LOW priority
            Analytics → 💤 VERY LOW priority

            If everything goes into one queue → critical tasks get delayed
            
        
        -> ou create multiple queues, and route tasks based on importance.    

"""

# Define queue 

from celery import Celery

app = Celery('app', broker='redis://localhost:6379/0')

app.conf.task_routes = {
    'tasks.payment.*': {'queue': 'high_priority'},
    'tasks.email.*': {'queue': 'low_priority'},
}

# Task

@app.task
def send_email():
    print("Sending email...")


@app.task
def process_payment():
    print("Processing payment...")