""" 

=> API-Gateway With Load balancer

    -> Suppose you have many backend services

     
       client -> API Gateway -> User Service -> Order Service -> Payment Service


    -> Now imagine

       each services each services runs on multiple EC2 instance


       API Gateway cannot efficiently manage which instance should receive traffic

       isntead , api gateway send request to a load balancer



                Client
                  │
                  ▼
            API Gateway
                  │
                  ▼
       Application Load Balancer
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
      EC2-1     EC2-2     EC2-3   


=> What does API Gateway do

    1. Authentication 

    2. Authorization 

    3. Rate limiting

    4. Request validation 

    5. API keys 

    6. Logging 

    7. Monitoring


=> What does Load Balancer do

   1. Load balancing

   2. Health check 

   3. Routing to healthy instance 

   4. Removing failed instance 

   5. Supporting auto scaling


=> API gateway -> Security -> Load balancer -> Traffic distribution -> Server


=> Integration With ECS 

   Client -> API Gateway -> Application load balancer -> Amazon ECS -> Containers


   -> ALB distribute request across containers task

=> Integration with EKS

   Client -> API Gateway -> Application load balancer -> Kubernetes pods


   load balancer forwards request to healthy pods


=> Integration with EC2

    Client -> API Gateway -> Application load balancer -> EC2 auto scaling group


    ec2 -> 10 ec2


    ALB automatically start routing taffic to the new instance 

=> Real Production Example 

    
   Customer -> API Gateway -> ALB -> Order Service (5 EC2) -> DB


=> Advantage 

    1. Support Auto scaling 

    2. High availability 

    3. Health checks 

    4. Decouple API gateway

    5. Easy scaling

    6. Centralized API management


=> When should be use ALB integration 

    1. EC2 instance 

    2. ECS containers 

    3. Kubernetes (EKS)

    4. Traditional web application

    5. Multiple backend server

"""