""" 

=> MultiContainer Pods 

     -> We think 

        1 Pod = 1 Container


     -> A pod can contain one or more containers

     -> Question is why we put multiple containers in the same pod instead of running them 
        in separate pods


=> what is multi-container pod 

   -> A multi container pod is simply a pod that contains two or more containers


                Pod
      ┌─────────────────────┐
      │                     │
      │  App Container      │
      │                     │
      │---------------------│
      │  Sidecar Container  │
      │                     │
      └─────────────────────┘


    -> Both containers runs on same worker node


=> WHy Use Multiple containers 

   -> If containers are tightly coupled and always need to run together 

        Logging agent
        Monitoring agent 
        Proxy 
        Certificate loader 
        Metrics exporter




"""