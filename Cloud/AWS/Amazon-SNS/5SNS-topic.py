""" 

=> Topic Policies

    -> A topic policy is a resource based policy IAM policy attached directly to an SNS topic

                   Publisher
                     |
                     |
                     V
             +----------------+
             | Topic Policy   |
             +----------------+
                    |
               Allow / Deny
                    |
                    V
             +----------------+
             |   SNS Topic    |
             +----------------+
 
    every request to this topic is checked against this policy


=> Why do we need topic policy

    1. without topic policy

       -> anyone with the right IAM permissions in their own context could potentially attempt 
          operation

    2. Topic policy answer 

       -> can account b publish 

       -> can cloudwatch publish alarms 

       -> can eventbridge publish event

       -> can someone subscribe an http endpoint 

       -> can a lambda function subscribe


=> Resource based policy Vs. identity based policy

    1. Identity  based policy

        attached to iam user

        IAM user 
        IAM role 
        IAM group


     developer role -> can publish to sns

     this identity carries its permission

    2. Resource based policy

        attached to 

          -> sns topic 
          -> s3 bucket 
          -> sqs queue
          -> kms queue    

"""