""" 

=> ttlSecondsAfterFinished In Kubernetes Jobs

    -> After this job finish , wait N second , then automatically delete the job and its dependent resources


apiVersion: batch/v1
kind: Job
metadata:
  name: report-job

spec:
  ttlSecondsAfterFinished: 60

  template:
    spec:
      restartPolicy: Never

      containers:
        - name: worker
          image: busybox
          command: ["sh", "-c", "echo 'Report generated'"]



    -> kubernetes wait 60 second afther the job finish, then clean its up                      



"""