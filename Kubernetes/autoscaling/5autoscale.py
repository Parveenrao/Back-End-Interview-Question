""" 

=> Vertical Autoscaler 


    -> It changes , how much CPU and memory each Pod gets


    -> VPA working 

       1. Recommeneder 

           -> Analyze CPU/memory usuage and calculates recommendations such as 

              Lower bound 
              Target 
              upper bound

       2. Updater 

          -> Determine whether existing pod need their resource changes 


       3. Admission Controller

           -> Intercepts creation of a new / recreated Pod and applies the VPA
              recommendations before the pod starts           



"""