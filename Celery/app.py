from celery import Celery
import time

# create celery app

app = Celery("app" , 
             broker="redis://localhost:6379/0",
            backend="redis://localhost:6379/0")


# Define task 

@app.task
def add(x , y):
    print(f"Adding {x} + {y}")
    time.sleep(3)   # stimuate heavy work
    
    return x + y

if __name__ == "__main__":
    # Call task
    result = add.delay(5, 7)

    print("Task ID:", result.id)
    print("Status:", result.status)

    # Wait for result
    print("Result:", result.get(timeout=10))
