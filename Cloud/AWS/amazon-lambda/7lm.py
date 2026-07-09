""" 

=> Stateless Nature of AWS lambda

   -> Lambda function are stateless


=> What does Statelesss mean

    -> A stateless application does not rely on data stored in memory from previous executions

    -> Every invocations should be able to execute independently using only 

        1. Incoming event 

        2. External data sources (database , cache , object storage)


    -> in simple terms 

        each lambda function invocation should be treated as if it is running for the first time



=> Why lambda Stateless

   -> AWS automatically 

       1. Create execution env
       2. Reuse them when possible 
       3. Destory them at any time



"""