""" 
=> AWS Lambda Invoke Phase

   -> The invoke phase is the phase in which AWS actually executes your lambda handler

   -> Inovke phase 
      
      Invoke phase = the period when your lambda_handler(event , context) function is runnig


   -> INIT phase = prepare the env 

   -> Invoke phase execute the code



=> Event object 

    -> During the invoke phase , lambda pass event 

=> Context object 

     -> Lambda also pass a context object 

     -> context contain metadata about

         1. function name 
         2. function version
         3. aws request id 
         4. remaining execution time 

         5. invoked arn 

         6. memory limit


=> Performance object

     1. Reuse resources


         -> create reusable resouces outside the handler


         -> creating client on every invocation adds necessary overhead


=> What is the Invoke Phase?

    -> The Invoke Phase is the stage where Lambda executes your handler function (lambda_handler) with the provided event and context.         

=> Does the Invoke Phase occur on every request?

    -> Yes. Every invocation executes the handler. Only the INIT phase may be skipped during warm starts.

    
=>  What arguments are passed to the handler?

      The handler receives:

       event - the input payload.
       context - metadata about the current invocation and execution environment.  

=> What happens if the handler exceeds the timeout?

    -> Lambda terminates the execution and reports a timeout error. 

=> What happens after the Invoke Phase?

   -> Lambda returns the response (or error), then freezes the execution environment for possible reuse or eventually destroys it if it's no longer needed.            
"""