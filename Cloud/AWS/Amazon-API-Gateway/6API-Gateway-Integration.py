""" 

=> API Gateway Integrtions

   -> An integration define how API gateway communicates with the backend after processing
     
     the incoming  request


     client -> api gateway -> integration -> backend


=> Lambda Proxy Integration 

    -> Lambda proxy integration means API gateway forwards the entire HTTP request to the 
       lambda function with minimal modification

    -> lambda receives all request information and is responsible for generating the 

       completing HTTP response

       client -> HTTP request -> API gateway -> forward entire request -> lambda


    -> Why it is called proxy 

       -> A proxy forward request without changing much

       -> instead of mapping every header , query parameter , and body individually.

         API gateway packages everything into a standard event object


=> Lmabda Non-Proxy Integration 

    -> In Lambda Non proxy Integration , API gateway does not send the complete HTTP request 
       to lambda.

       -> API Gateway creates a custome payload using mapping technique


       client -> http request -> API gateway -> mapping template -> custom json 

       lambda


    -> proxy = lambda receive everything 

       non proxy -> lambda receive only what api gateway choose to send   



"""