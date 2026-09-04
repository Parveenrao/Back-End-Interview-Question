""" 

=> Amazon Cloudwatch 

    -> Monitoring and obervability service of AWS


=> What is Amazon Cloudwatch 

    1. Imagine you own a company with 500 servers 

    2. We ask question like 

        1. Is CPU usuage to high 
        2. Is memory running out 
        3. Is disk full
        4. Is my application healthy 
        5. Did a server crash 
        6. How many user visited today 
        7. which EC2 instance is slow 
    
     Cloudwatch answer of all these


   3. Amazon cloudwatch is a monitoring service that collects , stores , visualizes  metrics logs 
      and events from AWS resources and application


 => CloudWatch Architecture 


          EC2
           │
           │ Metrics
           ▼
      CloudWatch
     /     |      \
 Metrics  Logs   Events
    |       |       |
 Dashboard Alarm  Automation           


"""