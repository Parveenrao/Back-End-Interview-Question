""" 


=> CronJob

   -> Kubernetes CronJOb run Jobs automatically according to a schedule

       Job = run a task

       CronJob = run that job on a schedule


=> Why do we need CronJob

   -> Suppose we have database backup script , python backup.py

   -> you need it to run every day at 2.00 AM


   -> A job can execute the backup

       job -> pod -> backup.py -> complete

   -> But who create the job every day , Cron job

       Every day at 2 AM -> Cronjob -> Creates a job -> pod -> backup.py -> complete


=> A cronjob does not directly create a pod. It creates a pod and the job manages its Pods


=> Cron schedule syntax 


* * * * *
│ │ │ │ │
│ │ │ │ └── Day of week
│ │ │ └──── Month
│ │ └────── Day of month
│ └──────── Hour
└────────── Minute


=> */5 * * * *     Every 5 minutes

0 * * * *       Every hour

0 2 * * *       Every day at 2 AM

0 9 * * 1       Every Monday at 9 AM

0 0 1 * *       First day of every month at midnight



"""