""" 

=> Job 

   -> A job is a kubernetes resources used to run a task that should finish and stop ,
     rather than keep running forever

     job = Run this task until it completed successfully 


   -> jobs are usefull  for things like , database migration , backups , batch processing ,
      data imports , report generation , ML processing and other finite task


   -> Deployment = make sure something keeps running , deployment is for lon running applications

   -> Jobs = make sure something finishes successfully     

   
=> Job Lifecycle 


             Job created
                  │
                  ▼
          Job Controller
                  │
                  ▼
              Create Pod
                  │
                  ▼
            Run Container
                  │
          ┌───────┴───────┐
          ▼               ▼
       exit 0          non-zero exit
          │               │
          ▼               ▼
      Succeeded          Failed
          │               │
          ▼               ▼
   Job Complete       Retry according
                   to Job settings


"""