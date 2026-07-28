""" 

=> Autoscaling In Kubernetes 

      -> Autoscaling means kubernetes automatically adjust resources according to workload demand

      -> Imagine your application normally needs 2 Pods

         user -> Service -> Pod -> Pod 

      -> Suddenly traffic increase heavily. Instead of manually creating more Pods , Kubernetes 
         can scale 


         User -> Service -> Pod , Pod , Pod , Pod , Pod , Pod , Pod 

         when traffic fails , kubernetes can reduce Pods again



=> HPA (horizontal Pod Autoscaler)

   -> HPA automatically increase or decrease the number of replicas of a scalable
      kuberetes workload based on observed metrics


   -> what exactly HPA do

      -> Suppose deployment starts with

           replias : 2

      -> each pod request 

           resources:
               request:
                  cpu : 500m

      -> we create an HPA

            minReplica : 2
            maxReplica : 10
            target CPU = 50%
            
            HPA decides that 2 Pods aren't enough and increases the desired replica count.

            HPA doesn't process traffic itself. It changes the desired replica count 
            of the target workload, such as a Deployment.      

      -> HPA Architecture

               Application Pods
                    │
                    │ resource usage
                    ▼
                  kubelet
                    │
                    ▼
              Metrics Server
                    │
                    │ Metrics API
                    ▼
             HPA Controller
                    │
                    │ calculates desired replicas
                    ▼
                Deployment
                    │
                    ▼
               ReplicaSet
                    │
                    ▼
              More/Fewer Pods     

        -> Metrics server

             HPA need information 

              POD A -> CPU usuage 

              POD B -> CPU usuage 

              POD C -> CPU usuage

           For standard CPU/memory resource metrics , this commonly comes through kubernetes
           resources metrics pipeline using Metrics Server

        -> CPU Utilization 

            1. Suppse Pod has 

                  resources:
                      request:
                         cpu : 500m

            2. And currently use 

                 250m CPU

            3. CPU utilization 

                 CPU usuage / CPU Request * 100

                 250 m / 500m * 100 => 50%


                 50 % of entire node 

        -> Request Matter

             resources:
                  request:
                     cpu : 1000m

            current CPU usuage = 500m


            HPA sees 

            500 / 1000 * 100 => 50%


            now only change to request


=> How HPA calculate Replicas 

   desired replicas = ceil(currentReplicas * currentMetricvalue / desiredMetricValue)

   current Pod = 4 
   Current CPU = 80%
   Target CPU = 50%


   desiredReplicas =
    ceil(4 × 80 / 50)

     = ceil(6.4)

    = 7

    

=> Minireplicas and maxreplica 

    miniReplica = 2
    MaxReplica = 10

    even if calculation says

    desiredReplica = 15

    HPA caps it = 10 Pods


    and if calculates 

    desiredReplica = 1

    it remains at 2


=> Basic HPA file 

apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
spec:
  replicas: 2

  selector:
    matchLabels:
      app: backend

  template:
    metadata:
      labels:
        app: backend

    spec:
      containers:
        - name: backend
          image: my-backend:1.0

          resources:
            requests:
              cpu: 500m
              memory: 256Mi

            limits:
              cpu: "1"
              memory: 512Mi


=> HPA 


apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler

metadata:
  name: backend-hpa

spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: backend

  minReplicas: 2
  maxReplicas: 10

  metrics:
    - type: Resource
      resource:
        name: cpu

        target:
          type: Utilization
          averageUtilization: 60


    -> scaleTragetRef

        This tells HPA

        which workload am I Scaling

     -> average utilization 

        means target averge  resource utilization across relevant pod         



"""