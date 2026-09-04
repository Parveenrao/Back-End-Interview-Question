"""" 

=> Amazon ELB (Elastic Load Balancer)

   -> It ditribute incoming traffic across multiple targets (EC2 instance  , containers , Lambda function)
      Ip address , making application highly available, fault tolerant , and scalable


=> What is Elastic Load Balancer 

   -> Is a managed AWS service that automatically distributes traffic among healthy targets.

   -> AWS manage 

      1. Scaling 
      2. High Availability 
      3. Health check
      4. SSL certificates 
      5. Failover 


      we don't manager server for elb

=> Why do we need ELB 

   1. Suppose we have only one EC2 instance 

      Internet -> EC2 instance 

      -> single point of failure 
      -> Server crash -> website down 
      -> cannot handle millions of users



   2. Instead 

             Internet
                 |
          Elastic Load Balancer
          /          |          \
      EC2-1       EC2-2      EC2-3   


      -> High availability 
      -> Better performance 
      -> Fault tolerant 
      -> Auto scaling support   


"""