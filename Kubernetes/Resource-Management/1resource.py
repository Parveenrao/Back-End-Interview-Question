""" 

=> Resource Managment In Kubernetes 

    -> Resource Management is a core production topic in kubernetes.

    -> How much CPU and memory shoudl each container get and what happen when the cluster runs short 

    -> without Resources management 

        one badly behaving container could consume a huge amount of CPU or 
        memory and hurt other workload 


        
=> 1. Resource Request 

      -> A resource request tells kubernetes that this container need this much CPU and memory
         to run properly

      -> The kubernetes scheduler use request to decide which node should run a POD.


      -> why does k8s need  request 

          Node A = 2   CPU available 
          Node B = 1   CPU available 
          Node C = 0.2 CPU available 


          New pod request 

            resource:
                request:
                   cpu : "500m"
                   memory : "256Mi"

         SO Node A and Node B

         Scheduler can place Pod on A or B

         This is the main purpose of request : scheduling



       -> CPU Request 

           -> CPU is commonly expressed using millisecond

               1000m = 1 CPU
               500m  = 0.5 cpu
               250m =  0.2 cpu
               100m = 0.1 cpu


               resource:
                   request:
                     cpu : "250m"

                This container request 25% of one CPU core 

            A request is not necessarily the maximum CPU the container can use

       -> Memory Request 

          ki = kibibytes
          Mi = Megibytes 
          Gi = gibibytes

          memory : "1Gi"

          means container request approximately 1GiB RAM

          Pods do not necessarily consume their requested memory immediately. Request represet
          the amount account for when scheduling

       -> Request are defined per container


       spec:
  containers:

    - name: backend
      image: backend:v1
      resources:
        requests:
          cpu: "500m"
          memory: "512Mi"

    - name: sidecar
      image: sidecar:v1
      resources:
        requests:
          cpu: "100m"
          memory: "128Mi"                                    


"""