""" 

=> Controller Manager

    -> Controller Manager is kubernetes brain that take action


    -> Controller manager runs a collection of controllers that continuously monitor the cluster 
       and make sure the actual state match the desired state 

    -> It follows a simple prinicple 

        Observe -> Compare -> Act -> Repeat 

        It never stop checking cluster 


=> Example 

   1. Imagine a hotel

   2. I am the hotel manager 

   3. I decide 

        There should be always 

        10 cleaners 
        5 Receptionists
        2 Security guards

   4. One cleaner resign

       Current staff

         Cleaners = 9

         I hire another cleaner 

         I don want to wait for someone to complain


=> Desired State Vs Actual State 

   1. Suppose we create

       replicas = 3

       Desired state , Pod A , Pod B , Pod C

       Actual State , Pod A , Pod B

   2. Controller Manager notice 

       Desired = 3

       Acutal = 2

       Action Create one more pod


=> Architecture 


             API Server
                  │
                  ▼
          Controller Manager
                  │
      -------------------------
      │       │       │
      ▼       ▼       ▼
 Deployment Replica Node ...
 Controller Controller Controller


 => Controller manager is a process that runs many different controller 

 => Each controller has a specific responsibility


=> Controller Loop

    -> Each controller runs a loop similar to this

    while True:
    
        desired_state = get_desired_state()

        acutal_state = get_acutal_state()

        if desired != actual:
        
            reconcile

        sleep

    This is called Reconciliation Loop


=> What is Reconciliation 

   -> Making Reality match the desired state 


=> How does Controller know something has changed

   -> controller does not ask directly to etcd directly 

   -> instead controller watch api server 

       API server notify controllers when relevant resources change 


-------------------------------------------------------------------------------------

1. Deployment Controller 

     -> Deployment controller creates a replica set 

        Deployment -> Replicset

        It does not creates pod directly 

        Deployment -> Replicaset -> Pods


2. ReplicaSet Controller 

    -> Maintain correct number of pods


3. Node Controller 

   -> This controller monitors worker nodes 

4. Job Controller 

    -> Job controller tracks completetion and retries failed pods according to the job
       specification


5. Statefulset Controller 

    -> Used for database 

    -> Pods have fixed indentities 

        mysql-0
        mysql-1
        mysql-2


    -> if mysql-1 fails,  it is recreated with the same identity and can reattach its storage 

6 DaemonSet Controller 

   -> Suppose 5 nodes 

   -> we want exactly one monitoring agent on every node 

   -> DaemonSet ensure 


       Node 1 -> Monitorin Pod 

       Node 2 -> Monitoring Pod 

       Node 3 -> Monitoring Pod 

       
 





"""