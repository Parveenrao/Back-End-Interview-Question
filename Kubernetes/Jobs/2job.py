""" 

=> Restart Policy In Kubernetes

    -> For Jobs pod , restart policy control what happens to a container when it fails

    -> A job allow two values

        restartpolicy : Never 


        restartpolicy : OnFailure


=> 1. Restartpolicy : Never

apiVersion: batch/v1
kind: Job
metadata:
  name: demo-job

spec:
  backoffLimit: 3

  template:
    spec:
      restartPolicy: Never

      containers:
        - name: worker
          image: busybox
          command: ["sh", "-c", "echo Running; exit 1"]

    -> k8s does not restart that failed container inside the same Pod

   Job
 │
 ▼
Pod #1
 │
 └── Container
        ↓
      exit 1 
        ↓
Pod #1 → Failed

Job Controller
      ↓
creates another Pod

Pod #2
 │
 └── New Container       


=> RestartPolicy : OnFailure 

   -> When the container fails , kubernetes can restart the container inside the same Pod


   Job
 │
 ▼
Pod #1
 │
 ├── Container attempt #1
 │        ↓
 │      exit 1 ❌
 │
 ├── Container attempt #2
 │        ↓
 │      exit 1 ❌
 │
 ├── Container attempt #3
 │        ↓
 │      ...


 -> Pod itself can remain the same while its container is restarted

 -> This is handled by the kubelet on the node


 




"""