""" 

=> startingdeadlinestarting

    -> How late a CronJob is allowed to start after its scheduled time

    -> this matter when k8s misses the original schedule

    -> example 
      
       1. Job should start at
          
           02:00

       2. But for some reason kubernetes could not start it at 2:00

       3. May be the controller was unavailable or Cronjob as suspended

       4. when kubernetes can process it again , it has to decide 

              should i still run this missed job , or it is too late 

=> spec:
  schedule: "0 2 * * *"
  startingDeadlineSeconds: 300

  -> So the scheduled Job is allowed to start up to 5 minutes late.                 



"""