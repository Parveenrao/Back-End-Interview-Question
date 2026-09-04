""" 
=> Cluster In Amazon-ECS

  

=> What is an ECS cluster 

    -> A logical group of compute resources where ECS runs your container

    -> container managemnet boundary

    -> instead of directly running container on Ec2 machines
     
         tells ecs , here is my. Run my application here


    -> Simply example 

       1. A company has 

          -> Authentication service 
          -> Payment service 
          -> Recommendation service 
          -> Notification service

      2. Instead of manually deciding

         -> Run auth on Server A 

         -> Run payment on Server B

         -> Run notification on Server C

         we simply create

         Production Cluster

         and tells ECS

         Run Auth

         Run Payment

         Run Recommendation

         Run Notification

         ECS decide where each container should run


=>                    ECS Control Plane
                           │
                           │
                        Scheduler
                        Placement Engine
                        Service Manager
                           API
                           │
──────────────────────────────────────────

             Production Cluster

      ┌─────────────────────────┐
      │                         │
      │ EC2 Instance 1          │
      │                         │
      │ Docker                  │
      │ ECS Agent               │
      │ Task A                  │
      │ Task B                  │
      └─────────────────────────┘

      ┌─────────────────────────┐
      │                         │
      │ EC2 Instance 2          │
      │                         │
      │ Docker                  │
      │ ECS Agent               │
      │ Task C                  │
      │ Task D                  │
      └─────────────────────────┘

      ┌─────────────────────────┐
      │                         │
      │ EC2 Instance 3          │
      │                         │
      │ Docker                  │
      │ ECS Agent               │
      │ Task E                  │
      └─────────────────────────┘                  



"""