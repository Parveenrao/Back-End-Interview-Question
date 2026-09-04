""" 

=> CloudWatch Logs

   -> Metric show numbers

   -> Logs show detailed text 

       10:00  Login success

       10:01  User Added Product 

       10:03  Payment Failed 

       10:05  Database Timeout 

       10:06  Server Error


       CloudWatch store all logs

    -> Log Groups 

       1. Logs are organized 


           -> EC2 Logs
           -> Lambda Logs
           -> Application Logs 
           -> Database Logs

           Each folder is called Log Group

    -> Log Stream 

       -> Inside a log group 

         Application log

            server 1 
            server 2
            server 3

        each server creates a log stream


    -> Cloudwatch agent 

       The agent is software installed on EC2

       Without agent , cloudwatch receives:

       CPU 

       Disk 

       Network


       with agent 

       CPU 

       DISK 

       Memory 

       Swap

       processes

       custom logs                  


"""