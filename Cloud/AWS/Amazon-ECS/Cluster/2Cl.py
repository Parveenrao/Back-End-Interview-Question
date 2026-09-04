""" 

=> Cluster Component

     1. Compute

        -> could be EC2 or Fargate or External Service

     2. ECS Agent

        -> every EC2 instance runs

             ECS agent

        -> Responsibilities:

            1. Register the instance with the cluster 
            2. Reports available CPU , memory and  status

            3. Pulls conatiner images 

            4. Start and stop container

            5. send logs and health information back to ECS

    3. Scheduler

       -> Every EC2 instance runs

       -> Responsibility 

           -> Scheduler constantly ask

                where should this task run

           -> it task

              1. CPU 
              2. RAM
              3. Availability Zone 
              4. Placement Rules 
              5. Task containers

    4. Task

       -> Container never run directly 

       task definition -> task -> container

       the cluster run task , and each task can continue one or more containers

    5. Service 

       -> A service continuously maintains the desired number of running task


           desired = 10

           if one crash

           10 -> 9 -> scheduler launches another


=> Differenet Cluster Types


    1. EC2 cluster

       cluster -> ec2 instance -> docker -> containers

       you manage 

         EC2 instance 
         os patch 
         scaling

         aws manage ecs

    2. Fargate cluster

        cluster -> aws -> hidden server -> containers

        no ec2 instance are visible to you

    3. External cluster

        -> useful for 

           on-premise 

           bare metal

           other clouds

=> What happen when we create a cluster  

   -> aws create metadata such as

      1. cluster id 
      2. cluster arn
      3. cluster name 
      4. cluster state

    at this point

      cluster -> empty


      we then add capacity

       ec2 or fargate or external node

=> Internal metadata


-> aws store information


Cluster Name

Available CPU

Available Memory

Registered Instances

Running Tasks

Services

Capacity Providers

Network Configuration

this state is managed by ECS control plane
"""

