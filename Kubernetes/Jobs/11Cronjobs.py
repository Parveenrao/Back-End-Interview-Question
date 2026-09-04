""" 

=> Successfulljobhistorylimit And Failedjobhistorylimit

      -> These are the cronJobs that control how many old jobs kubernetes keep after 
         scheduled execution finish


      1. successfullhistorylimit

           successfullhistorylimit : 3


           keep the 3 most recent successfully completed jobs created by this CronJob

           suppose cronjob daily runs 

            Monday     → Job-1 ✅
            Tuesday    → Job-2 ✅
            Wednesday  → Job-3 ✅
            Thursday   → Job-4 ✅   



            Job-2 ✅
            Job-3 ✅
            Job-4 ✅

            Job-1 → deleted

            This prevents successful Job history from growing forever.

    2. failedjobhistoryLimit

         failedjobhistorylimit : 2

         keep the 2 most recent failed jobs created by this cronjob




apiVersion: batch/v1
kind: CronJob
metadata:
  name: database-backup

spec:
  schedule: "0 2 * * *"

  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 2

  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: Never

          containers:
            - name: backup
              image: my-backup:v1                 


"""