"""

                        Users
                          │
                          │ kubectl / API Request
                          ▼
                 +-----------------------+
                 |    Control Plane      |
                 |-----------------------|
                 | API Server            |
                 | Scheduler             |
                 | Controller Manager    |
                 | etcd                  |
                 +-----------------------+
                          │
          ------------------------------------------
          │                    │                    │
          ▼                    ▼                    ▼
+----------------+    +----------------+    +----------------+
|  Worker Node 1 |    |  Worker Node 2 |    |  Worker Node 3 |
|----------------|    |----------------|    |----------------|
| kubelet        |    | kubelet        |    | kubelet        |
| kube-proxy     |    | kube-proxy     |    | kube-proxy     |
| Container RT   |    | Container RT   |    | Container RT   |
| Pods           |    | Pods           |    | Pods           |
+----------------+    +----------------+    +----------------+


=> A kubernetes cluster is made up of 

    1. Control Plane (brain)
    2. Worker node (the workers that run your application)



=> Control Plane 

   -> The Control Plane is the collection of component that manage the entire kubernetes cluster 

   -> It usually does not run application , Instead it decide 

      1. Which application shoudl run 
      2. Where they shoudl run 
      3. How many copies shoudl run
      4. What to do if something fails


               Control Plane
        +-------------------------+
        |      API Server         |
        |-------------------------|
        |        etcd             |
        |-------------------------|
        |      Scheduler          |
        |-------------------------|
        | Controller Manager      |
        +-------------------------+


=> API Server 

   -> The API Server is the front door of kubernetes 

   -> Every request goes through it

      Developer -> Kubectl apply -> API server 

   -> The API server is the only component that client talk to directly 

   -> API Server is the single controlled entry point


   -> Responsibilities 

       1. Authentication 

          -> Who are you , if the token is valid , allowed 

       2. Authorization 

       3. Validation 

           suppose we create = -10

           API server validates the request 

       4. Store desired state 


=> Flow

kubectl apply

↓

API Server

↓

Authentication

↓

Authorization

↓

Validation

↓

Store in etcd

↓

Return Success


"""