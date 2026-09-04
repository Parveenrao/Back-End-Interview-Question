""" 
=> CloudWatch ALarms 


    -> Most important features 

    -> Suppose CPU exceed 80%

    -> Cloudwatch checks continuously

       CPU -> 20% -> 35% -> 55%-> 81% -> 90% -> Alarm

       Alarm become alarm


    -> Alarm status

       There are three states

       1. OK -> Everything is healthy

                CPU = 35%

       2. ALARM  -> Threshold exceed 

             CPU = 95%

       3. Insufficent data

           Cloudwatach doesn't have enough data 

           New Instance -> No metrics yet 

    -> Alarm Action 

        1. Send email 
        2. Trigget auto scaling 
        3. Restart EC2
        4. Stop EC2 
        5. Terminate EC2
        6. Recover EC2
        7. Invoke Lambda 
        8. Send SNS Notification


    -> Cloudwatch SNS

       Coudwatch cannot send emails directly 


       Cloduwatch alarm -> SNS topic -> Email , SMS , Lambda , HTTP endpoint                                


"""