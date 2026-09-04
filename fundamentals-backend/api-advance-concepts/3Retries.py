""" 


=> Retries In APIS

    -> Retry is a mechanism where a client automtically send the same API request again if the
       first fails due to temporary problem


    -> Example 

        1. I call my friend 

        2. The network is busy 

        3. You wait a few second and call again 

        4. The second call succeeds

      APIs work the same way 


    -> Why are retries needed 

       1. Sometime failure are temporary

           -> Network timeout
           -> Server overload 
           -> Database temporarily unavailabe 
           -> Connection reset 
           -> gateway timeout 

       2. Instead of immediately showing error to the user , client retires



=> Which http method are safe to retryn

   1. GET -> It Reads data

   2. HEAD -> Yes 

   3. OPTIONS -> Retry YEs 

   4. POST -> Not always safe , post require idempotency

   5. PUT -> set the same data again , usually safe because put is idempotent

   6. DELETE -> acceptable because the final state is the same 


=> Simple Retry 

    -> If a request fail , try again immediately or after a small fixed of delay


import requests

MAX_RETRIES = 3

for attempt in range(MAX_RETRIES):
    try:
        response = requests.get(
            "http://localhost:8000/users/1",
            timeout=5
        )

        print("Success!")
        print(response.json())
        break

    except requests.Timeout:
        print(f"Attempt {attempt + 1} failed.")


    -> why simple retry cannot be good option 

        1. Imagine 10,000 clients call API at a time 

        2. Ther server crashes for moment

        3. All 10,000 client retries immedaitely 

           server busy -> 10000 client retry together -> server become more overloaded

           called retry storm or thundering herd poblem    

    

=> Fixed Dealy Return 

   -> Immediatley return is not a good option . we can wait for a fixed amount of time before trying again

       timeout(5 seconds)


=> Exponential backoff

    -> Suppose 10000 users are using my app

    -> Database crash for 5 second

    -> ALl client send a request 

    -> everyone gets,  503 Service unavailable 

    -> Now every client retry immediately 

       Server -> 10000 Retry request 

       The server is alreay overloaded and now it receives another flood of request


    -> Solution , wait longer after each delay 


       -> Instead of retrying immediatley , increasing the watiting time after every failure

       Attempt 1 -> wait 1 second 

       Attempt 2 -> wait 2 second 

       Attempt 3 -> wait 4 second 

       Attempt 4 -> Wait 8 second

       Wait time doubles after each failure 

       This is called Exponential backoffs

      Formulae =  wait = base_delay × (2^attempt)   

      
      Attempt	Calculation	 Wait
           0	 1 × 2⁰	     1 sec
           1	 1 × 2¹	     2 sec
           2	 1 × 2²	     4 sec
           3	 1 × 2³	     8 sec
           4	 1 × 2⁴	     16 sec

    -> Important

         Since this is a POST request , it should also include an Idempotency-Key so that 
         retry does not create multiple payments


    -> One Limitation 

       1. Imagine 10000 client all failt at exactly 10:00:00

       2. Every client use exponential backoff

          Retry after 1 second

       3. All retry at 10::00::01

          then all wait -> 2 second


       4. All retry at 10:0:03

           then all wait 

       5. They are still synchronized causing repeated spike in traffic 


       6. this is why production system usualy add jitter(randomness) to the dealy , so 
           each client waits a slightly different amount of time                      


"""