""" 

=> AWS Lambda Shutdown phase

    -> shutdown phase is the final stage of the lambda execution env lifecycle

    -> it occurs when AWS decide that an execution env is no longer needed and 

       permanently destroy it



       shutdown phase = aws permanently  terminates the lambda execution env and release all
        resources

=>            Lambda Lifecycle

                  Request
                    │
                    ▼
           INIT Phase (Cold Start)
                    │
                    ▼
             INVOKE Phase
                    │
                    ▼
              FREEZE Phase
                    │
                    ▼
             SHUTDOWN Phase   

=> Lambda does not immediately shut down after every invocation.

=> Normally, it first freezes the execution environment so it can potentially be reused.                     

=> Freeze Vs. Shutdown 

    1. Freeze 

        -> handler -> freeze execution env -> wait for next req 

    2. shutdown 

       -> execute env -> terminate -> release resouces -> gone forever


=> How does AWS Shut down an env

    1. Long period of inactivity

       request -> Function executes -> idle -> idle -> idle -> shutdown


    2. new deployment 

       suppose we upload a new code 

         version 1 -> deploye version2 -> old env shutdown -> new env created

      existing warm env using the old code are eventually replaced

    3. Configuration change 

       -> changing settins such as 

           1. Memory 
           2. timeout 
           3. runtime 
           4. env variable
           5. architecture

    4. AWS infra maintenance


    5. Scaling down 

       -> suppose traffic down 


         5000 env -> 1000 env -> 100 -> 10

         unused env shutdown

       AWS removes excess execution environments to free resources.

=> what happen during shutdown

    execution finished -> terminate runtime -> terminate process -> release memory -> delete /tmp storage 

    -> destroy firecracker micro vm -> release cpu done

    -> Everything inside that execution environment is removed.

=> What is lost

    -> When the env is shutdown


        1. memory 

        2. global variables

        3. db connection 

        4. /tmp -> file stored in

=> What trigger the next cold start 


   -> once env has been shut down

      new request -> no existing env -> create new firecracker microvm -> cold start


      because the old env no longer exist 

"""