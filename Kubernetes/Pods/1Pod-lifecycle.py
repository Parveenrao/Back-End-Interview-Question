""" 

=> Pod Lifecycle

    -> The Pod lifecycle is the sequence of states a pod goes thorugh from creation to 
        deletion

Create Pod
    │
    ▼
Pending
    │
    ▼
ContainerCreating
    │
    ▼
Running
    │
    ├─────────────► CrashLoopBackOff (if app keeps crashing)
    │
    ├─────────────► Completed (for Jobs)
    │
    ├─────────────► Failed
    │
    ▼
Terminating
    │
    ▼
Deleted




=> Complete flow


kubectl

    │
    ▼

API Server

    │

Stores Pod in etcd

    │

Scheduler selects a Node

    │

kubelet notices new Pod

    │

containerd starts Pod Sandbox

    │

Downloads image

    │

Creates containers

    │

Starts containers

    │

Pod becomes Running


=> Phase 1 Pending

    -> This is the first state

    -> Kubernetes knows about the pod , but it is not running yet 


    -> Why pod stays pending

       1. No Resources 

          Node Ram -> 8 GB 

          7.9 GB Used 

       2. No matching Node 


       3. PVC waiting

          -> if storage is not ready 

          pods wait 

       4. Image Pull Delay

          -> Large image 5 GB

          still downloading 



=> Phase 2 Running 

    -> At least one container is running

=> Phase 3 Succeeded

    -> This happens mostly for job pods 


=> Phase 4 Failed 

   -> Application exits with an error


=> CrashLoopbackoff

    -> This is not pod phase 

    -> it is a container restart status 

    -> why this happen 

       1. Wrond db credentials 
       2. Missing env variables 
       3. Port already is use
       4. Invalid configuration 
       5. Application big 
       6. Missing secret / configmap


=> ImagePullBackOff

    image: nginx:does-not-exist

    Pull image -> Image no found -> Retry -> Retry -> ImagePullBackoff

    -> Common reason

       1. Wrong image tag
       2. Typo in image name 
       3. Private registry authentication failure 
       4. Registry unavailable


=> ErrImagePull

    -> before kubernetes starts backing off , we see 

        ErrImagePull

        Then after repeated retries 

        ImagePullBackoff

    
First Failure

↓

ErrImagePull

↓

Retry Many Times

↓

ImagePullBackOff


=> Unknown


   -> Rare

   -> Node cannot communicate with API server 


=> Terminatiing 

   -> when  we run 


       kubectl delete pod nginx

   -> pod is not deleting immediately 


Running

↓

SIGTERM

↓

Wait

↓

Grace Period

↓

SIGKILL

↓

Delete


-> Default grace periond = 30 second






"""