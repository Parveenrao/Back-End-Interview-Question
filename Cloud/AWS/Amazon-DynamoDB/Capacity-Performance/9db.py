""" 
=> Backoff and Retries

   -> backoff and retries are techniques used in distributed system to handle temporary failures 
      without overwhelming the service 

   -> API request , Database request , Network communication , DynamoDB operation , S3 uploads ,Payment Processing



   -> Why do we need retries

       1. Imagine your application send a request to DynamoDB

           Client -> PutItem -> DynamoDB

           Request -> Network timeout / Temporarily Throttling

       2. Request failed , but the service is still healthy



=> Retry 

   -> Try same request again and again

      Attempt 1 -> Timeout -> Attempt 2 -> Success

   -> Problem with immediate Retries

      1. Suppose 10,000 clients get throttled

      2. Without delay 

         Client 1 -> Retry immediately 

         Client 2 -> Retry immediately 

         Client 3 -> Retry ummediately


         Client 10000 -> Retry immediately


      3. Now the server  recieve another 10000 request instantly

      4. Server become more overloaded

      5. This is called Retry storm


=> Solution 

    1. Instead of retrying immediately

    2. wait a little 

        attempt 1 -> wait 100ms -> attempt 2 


    3. if it still fails 

        attempt 2 -> wait 200ms -> attempt 3

    4. still fails then 

        attempt 3 -> wait 400ms -> attempt 4

    This increasing delay is called backoff

=> Types of backoff 

   1. Fixed backoff

      -> Always wait the same amount

         Retry 1 -> wait 1 sec 

         Retry 2 -> wait 1 sec 

         Retry 3 -> wait 1 sec

    2. Linear backoff 

       -> Increase delay by a constant amount 

         Retry 1 -> 1 sec 

         Retry 2 -> 2 sec 

         Retry 3 -> 3 sec 

         Retry 4 -> 4 sec


    3. Exponential Backoff

        -> delay backoffs every retry


        -> base 100 ms 


        Retry 1 -> 100 ms 

        Retry 2 -> 200 ms 

        Rery 3 ->  400 ms


=> What is jitter 


   -> Imagine 10000 clients all fail at the same time 

   -> without jitter 

       everyone waits 100ms

       every one retry together

       traffic spike again

   -> exponential backoff with jitter



=> Retry Limits 

    -> Never retry forever 

    -> max retry  = 5



"""