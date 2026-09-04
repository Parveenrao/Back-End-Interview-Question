""" 

=> Exponenital Backoff  + jitter 

 
    base = 2 ** attempt 

    wait = random.uniform(, base)

    

    with jitter 

    Client A -> 5.3 seconds 

    Client B -> 7.8 seconds 


    CLient C -> 2.1 seconds 

    CLient D -> 6.6 seconds 

    Client E -> 1.2 seconds


import requests
import random
import time

MAX_RETRIES = 5

for attempt in range(MAX_RETRIES):
    try:
        response = requests.get(
            "http://localhost:8000/users/1",
            timeout=5
        )

        response.raise_for_status()
        print("Success!")
        break

    except requests.RequestException:
        max_wait = 2 ** attempt
        wait = random.uniform(0, max_wait)

        print(f"Retrying in {wait:.2f} seconds...")
        time.sleep(wait)    




"""