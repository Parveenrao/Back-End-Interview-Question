""" 

=> Health-Check In Kubernetes 


     -> kubernetes health check determine whether a container is working correctly ,
        ready to receieve traffic or still starting


     -> A container being Running does not mean , the application is healthy


=> 1 LiveNess Probe

     -> A Livenessprobe check whether the application inside container is still healthy and
        functioning

     -> Core rule is 

         Liveness fails repeatedly = Kubelet restart the container


Kubelet
   │
   │ periodically checks
   ▼
Container :8080/health
   │
   ├── Success → do nothing
   │
   └── Repeated failure
            ↓
       Restart container   

       
=> Example 



apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  containers:
    - name: app
      image: my-app:1.0
      ports:
        - containerPort: 8080

      livenessProbe:
        httpGet:
          path: /health
          port: 8080

        initialDelaySeconds: 10
        periodSeconds: 5
        timeoutSeconds: 2
        failureThreshold: 3


=> HttpGet

   -> kubelete send an HTTP request to the container

   -> if the endpoint respond successfully , such as 200ok

=> intialdealysecond

   -> This tells kubernetes how long to wait after the container start before beginning liveness
      check

   -> This prevent a normal startup period from being mistaken for a dead application

=> periodsecond 

    -> This control approximately how often the liveness probe runs 

 10s     15s     20s     25s
 │       │       │       │
Check   Check   Check   Check


=> timeoutsecond 

    -> This control how long kubernetes waits for an individual probe before treating it as 
       failed

=> Failedthreshold 

    -> One failed threshold check does not immediately mean restart 

    -> k8s allow consecutive failure up to configured threshold

=> livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 5
  timeoutSeconds: 2
  failureThreshold: 3



=> What exactly get restarted

   -> if one container inside a multi-container pod fails its liveness probe

   -> kubernetes does not necessarily recreate the entire pod

   -> kubelet restart the failing container according to the pods restart policy


=> Types Of Liveness Probe

    1. HTTP Probe

      -> Use this when application expose endpoint HTTP/HTTPS such as GO Gin , FastAPI


      -> Important point is that liveness should answer whether restarting this container would 
          help

          do not make liveness endpoint depend unnecessarily on external system


    2. TCP Liveness Probe 

       -> When application does not expose /health http endpoint , listen on
          port 6379


   3. Exec liveness Probe

       -> An exec probe runs a command inside the container


   4. grpc Liveness Probe

       -> For a grpc application , kubernetes can use the standard health-checking protocol                 

"""