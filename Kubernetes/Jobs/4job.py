""" 


=> Complettion 

    -> How many successfull Pod executions are required before the job is considered
       compelete


apiVersion: batch/v1
kind: Job
metadata:
  name: batch-job

spec:
  completions: 5

  template:
    spec:
      restartPolicy: Never

      containers:
        - name: worker
          image: busybox
          command: ["sh", "-c", "echo Processing; sleep 5"]



    Kubernetes need 5 successfull Pods runs

    by default , setting parallelism they run one at a time


    Pod 1 -> Success

    Pod 2 -> Success 

    Pod 3 -> Success

    Pod 4 -> Success

    Pod 5 -> Success

    Successfull completion = 5

    Job complete

=> WHy do we need multiple completetion 

   -> Imagine we have 1 million image to process and your worker takes one batch of
      image per execution



=> ===================================================================================


=> Parallelism 

   -> How many Pod of a job may run at the same time

      spec:

         parallelism : 3


         means kubernetes can run upto 3 Pods concurrently for that job

      spec:
        completions: 10
        parallelism: 3 


        Need 10 successfull executions total 

        Upto 3 Pods can run at the same time


        100 successful completions are required, with up to 10 Pods running concurrently.

        It does not mean 10 total Pods.  



"""