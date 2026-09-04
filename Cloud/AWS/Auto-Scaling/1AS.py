""" 

=> Auto Scaling 

    -> Amazon EC2 Auto-Scaling automatically adds or removes EC2 instance based on your application
      workload 

    -> instead of manually launching or terminating EC2 instance , AWS does it automatically to 
       rule you define.

     -> It helps ensure the right number of EC2 instance are availabe , maintains availability
        replace unhealthy instance , and can reduce cost by scaling down when demands drop

=> Why do we need Auto-Scaling 

   1. Imagine an e-commerce website 

      Normal Day

      user = 500

      Need only EC2 instance

      EC2-1
      EC2-2

      Everything work perfectly


      Festival Sale 

       Users = 50,000

       2 EC instance cannot handle traffic

       CPU = 100%

       Memory = Full

       Website become slow 

   2. Benefit 

      -> high availability 

      -> Fault tolerance 

      -> Automatic scaling 

      -> Lower cost 

      -> No manual intervention

      -> Automatic replacement of unhealthy instance 

      -> Multi-availability Zone support     



"""