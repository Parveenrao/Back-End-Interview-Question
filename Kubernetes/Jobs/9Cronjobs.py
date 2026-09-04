""" 

=> ConcurrencyPolicy in Kubernetes 

    -> What should kubernetes shoudl do when its time to start a new job , but the previous
       job from the same Cronjob is still running


    -> THere are three ways 

       1. ALlow -> This is the default

          spec:
             ConcurrencyPolicy : ALlow

          It allows Job from the same CronJob to overlap

             10:00 → Job A starts
             │
             │ still running
             │
             10:05 → Job B starts
             │
             │
            A and B running
            at the same time    


            -> This is usefull when execution are independent and overlapping does not 
               causing problems


        2. Forbid 

             spec:
                CocurrencyPolicy : Forbid

            -> Do not start a new job if previous job from this CronJob is still running

            -> Forbid does not queue JOb B and wait for job A

            -> conceptually , that scheduled execution is missed / skipped because 
               another job was active 

        3. Replace 

            spec:
              concurrency : Replace

              when the next scheduled time arrives , replace the currently running job with 
              the new job

              10:00
  ↓
Job A starts
  │
  │ still running
  │
10:05
  ↓
new schedule
  ↓
Job A terminated
  ↓
Job B starts

            -> This is usefull when the latest execution matters more than completing
               the old one


"""