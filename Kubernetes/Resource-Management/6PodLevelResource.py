""" 

=> Pod Level Resource 

    -> Modern kubernetes also support Pod-level resource request and limit , where you
       definne budget for the whole pod


    -> Why Pod-level resources

        suppose a pod can  three container

        Pod -> API/Logger/Metrics


        containers:
  - name: api
    resources:
      requests:
        cpu: "500m"
        memory: "512Mi"

  - name: logger
    resources:
      requests:
        cpu: "100m"
        memory: "128Mi"

  - name: metrics
    resources:
      requests:
        cpu: "100m"
        memory: "128Mi"

    -> with pod level resource , we can define budget at spec.resources


apiVersion: v1
kind: Pod
metadata:
  name: backend
spec:

  resources:
    requests:
      cpu: "1"
      memory: "1Gi"
    limits:
      cpu: "2"
      memory: "2Gi"

  containers:
    - name: api
      image: my-api

    - name: logger
      image: my-logger

    - name: metrics
      image: my-metrics          



"""