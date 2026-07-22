""" 

=> What is Kubernetes 

    -> Kubernetes(K8s) is an open-source container orchestration platform that automates 
       the deployment , networking and management of containerized applications


    -> If Docker is used to package your application into containers , Kubernetes is used to 
       run and manage thousand of those containers


=> Why Kubernetes Created 

    -> Imagine we have fastapi application

        with Docker , docker run fastapi-app

        One container starts 

    -> But what happens if 

        1. 10 million user visti your application 
        2. The container crash 
        3. We need 20 copies of our application 
        4. We want zero downtime during deployment
        5. We have 50 servers 


        Managing this manually become nearly impossible 

        Kubernetes solves these problems automatically 


=> Problem Kubernetes solves 

    1. Automatic Deployment

        can start container automatically 


   2. Auto scaling

       -> Morning

           Users = 50
           Pods  = 2


        -> Night 

           users = 100000
           Pods = 50 

        -> Traffic decrease , Pods = 3


        Kubernetes scale automatically 

    3. Self Healing 

       Suppose one container crash

       Pod 1 
       Pod 2
       Pod 3

       Kubernetes Notice 

       Desired Pod = 3

       Runnig = 2

       Immediately creates new pod


    4. Load Balancing

       Imagine 4 pods 

       Request 1 -> Pod A 

       Request 2 -> Pod B

       Request 3 -> Pod C

       Request 4 -> Pod D

       Traffic is distributed evenly 


   5. Rolling Updates 

      -> Suppose version 1 is running 

          v1 , 

          deploye version 2

          stop all -> Deploy -> User see downtime

      -> with kubernetes 

          v1 -> v2 


          users experience or little downtime


    6. Rollback 

        If version 2 has bug 

        Rollback

        Kubernetes restores version 1 automatically                                  




"""