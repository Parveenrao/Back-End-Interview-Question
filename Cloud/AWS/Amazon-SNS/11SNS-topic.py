""" 

=> Cross Region Topics

   -> cross Region means message published in one AWS region are consumed or forwarded to
      services in another AWS Region


   -> Primarily used for

       1. Diaster Recovery(DR)

       2. Multi Region architecture 

       3. Gloabl application

       4. low-latency system

       5. Data replication

=> WHy do  we need Cross Region

   1. Suppose application runs in mumbai

       Region:
       ap-south-1 (Mumabi)

       SNS Topic

       if the mumbai region become unaviable , all notification stop

       to improve , we can replicate or forward event to another Region


=> How can we implement cross-region SNS?

    -> Typically by using a component such as AWS Lambda to subscribe to one topic 
        and publish to another topic in the destination Region.       

        

"""