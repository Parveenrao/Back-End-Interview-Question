""" 

=> Amazon-ECS

   -> Amazon Elastic Container service is a fully managed container orchestration service.

   -> It allows to run , manage , scale and monitor docker container without having 
      to build and maintain our orchestration platform


=> Why do we need ECS

    -> Imagine we are running a backend application

       User -> Backend API (Docker)

       one docker container

       but application become popular , 1000 user , 5000 users , 10000 users


     -> Problem 

        1. Need multiple container copies 
        2. Need load balancing 
        3. Need auto scaling 
        4. Container crash 
        5. Need restart 
        6. Need deployment 
        7. Need monitoring 
        8. Need rolling updates

    -> Before ECS 

       1. Suppose we have docker container

          docker run backend : v1

          containers runs

          if it crash, oops

          you manually restart it

          if traffic increase 

          docker run container:v1
          docker run container:v1
          docker run container:v1


      Now we have three containers

      how will user know which one to use 

      need load balancer

      how will container communicate

      need networking 

      how will logs collected

      need monitoring 

      how will deployment happen

    -> ECS does this automatically

        1. schedule containers 
        2. restart failed task
        3. scaling
        4. deployment 
        5. health check
        6. networking 
        7. IAM
        8. Logging
        9. monitoring

    -> what ECS actually manage 

       1.It does not

          -> Build docker image 
          -> Write dockerfiles
          -> write code 

       2. It manage
           container lifecycle

           such as

             1. where to run 
             2. when to run
             3. how many copies 
             4. restart if failed 

             5. update version 

             6. remove old version               



"""