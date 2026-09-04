""" 


=> Resource Limit
 
    -> A resource limit tells kubernetes
      
        This container must not use more than this amount of CPU or memory

        resource:
           limits:
              cpu : "1"
              memory : "512Mi"

    1. CPU Limit

        resources:
             request:
                cpu : "500m"

            limits:

               cpu : "1"

           if the application tries to use more than 1 CPU , k8s/linux does not normally kill container

           instead , cpu usuage is throttled

           CPU limit excedd -> throttled

    2. Memory Limit

         resources:
            request:
               memory : "256Mi"    
            limits:

               memory : "512Mi"

        A container cannot simply have its memory usuage 

        is exceed the memory limit , kernel may teriminate the process because of OOM                         



"""