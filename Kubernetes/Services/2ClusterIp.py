""" 

=> ClusterIP 

     -> A ClusterIP Service expose application only inside the kubernetes cluster

     -> cannot be access directly from our laptop  or the internet

     -> Think of like internal private network


=> WHy do we need cluster IP 

   -> Suppose we have  frontend , backend , database

   -> frontend needs to talk to the backend 

   -> backend needs to talk with to the database 



=> What Ip Does the Service get 

    -> Pods receive IPs from the POD CIDR

    -> Service receive IPs from the Service CIDR


=> backend Deployment 


apiVersion: apps/v1
kind: Deployment

metadata:
  name: backend

spec:
  replicas: 3

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
        image: nginx
        ports:
        - containerPort: 80

=> Cluster Ip 


apiVersion: v1
kind: Service

metadata:
  name: backend-service

spec:
  selector:
    app: backend

  ports:
  - port: 80               # service listen on port 80
    targetPort: 80         # traffic is forwarded to port 80 inside the PoD

  type: ClusterIP


  
=> List services 


kubectl get svc


=> describe service

kubectl describe svc backend-service


"""