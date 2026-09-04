""" 

=> ActiveDeadlineSeconds in Kubernetes Jobs

   -> how long a job is allowed to run before kubernetes stops it marks it Failed

   -> think of maximum execution time for whole job


apiVersion: batch/v1
kind: Job
metadata:
  name: data-processing

spec:
  activeDeadlineSeconds: 60

  template:
    spec:
      restartPolicy: Never

      containers:
        - name: worker
          image: busybox
          command: ["sh", "-c", "sleep 120"]


    -> Container wants to run 120 second 

    -> but the job allow only 60 seconds

 Job starts
      ↓
Pod starts
    ↓
0s ─────────────── 60s
                       ↓
                Deadline reached
                       ↓
                Running Pod stopped
                       ↓
                  Job Failed ❌    


=> WHy do we need it

   -> Imagine a batch processing job is supposed to take around 5 minutes , but because of bug it gets stuck 

   -> without a deadline it could keep running indefinitely 


        activeDeadlineSecond : 600

        Now the job gets at most 600 second = 10 minutes of active runtime


=> backoffLimit vs activeDeadlineSeconds

    backofflimit -> How many failure should I tolerate

    activedeadlineSeconds -> How long should i allow this job to run



"""