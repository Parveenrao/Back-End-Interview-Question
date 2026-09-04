""" 

=> Container Instance 
  
    -> A container instance is an EC2 virtual machine that has been registered into an 

       ECS cluster so ECS can schedule and run Docker container on it



       physical server -> hypervisior -> EC2 instance -> Docker engine -> ecs agent 

       registered as container instance -> run ecs task

=> What actually is container instance

   -> A normal EC2 instance is simply a virtual machine

       EC2 instance 

        CPU
        Memory 
        Disk
        network 
        operating system

    it knows nthng about ecs

    when we install

       Docker 
       Ecs agent

       and register it with an ecs cluster

       That EC2 become Container Instance

       EC2 + Docker + ECS agent + Registered TO ECS -> container instance


=> Why does ECS need Container Instance

   -> suppose we create a task

      Task 

      Container A 

      Container B

      where should these container run

      someone need to provide

      1. CPU
      2. RAM
      3. Disk
      4. Network


      Task ->  Container instance -> Ec2 hardware resources

      without container instances , ecs has nowhere to launch your container


=> Inside a Container Instance

    1. EC2 instance 
    2. Ubuntu / Amzon-linux
    3. Docker engine
    4. ECS agent 
    5. docker image 
    6. running container

=> ECS agent 

   -> it continuously communicate with the ECS control plane

      ecs control plan -> https -> ecs agent -> docker engine -> containers

      agent tells ecs

       1. cpu available 
       2. memory available 
       3. running task
       4. health status 
       5. logs 
       6. container lifecycle

=> Registration Process

   -> when the EC2 boots

     Boot ec2 -> docker starts -> ecs agent start -> reads cluster name -> call ecs api 

     -> register itself -> appears in ecs cluster 


"""