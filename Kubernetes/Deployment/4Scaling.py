""" 

=> Scaling 

    -> Scaling means changin number of pods replica running for an application

        Deployment -> Replicaset Pod1 / Pod2

        If traffic increase , we can scale to 5


=> Why do we Scale 

    1. More user

        100 user -> 2 Pods are enough 

        10,000 users -> Need more pods 

    2. High availability

        if one pod crash

        application still available 


    3. Better Load distribution

       -> Traffic is distributed across all pods 


=> Types Of Scaling 

    1. Maunal 

       -> We decide how many replicas run

          kubectl scale deployement nginx -replica = 5

    2. Automatic Scaling

        -> Kubernetes decide based on metrics 

            1. CPU Usuage 
            2. Memory usuage 
            3. Customer metrics 
            4. External metrics 

        THis is done using Horizontal Pod AutoScaler (HPA)


=> Does scaling create a new ReplicaSet?

    -> Scaling only changes the replica count of the existing ReplicaSet. 
       A new ReplicaSet is created only when the Pod template changes 
       (for example, changing the container image).    

=> What component actually creates or removes Pods during scaling?

    -> The ReplicaSet controller updates the number of Pods to match the desired replica count.                     

=> Can we scale to zero?

     -> Yes. Setting replicas: 0 stops all Pods while keeping the Deployment object.

"""