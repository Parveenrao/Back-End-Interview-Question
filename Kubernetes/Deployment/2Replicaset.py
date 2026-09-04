""" 


=> Replicaset

    -> Replicaset ensure that a specified number of identical Pods are always running 

    -> It only job is 

        Maintain the desired number of Pod Replicas 


    -> suppose , replicas = 3

        Replicaset continuously check 

        Are 3 pods running 

        if yes -> do nothing 

        if fewer than 3 -> create new pods 

        if more than 3 -> delete extra pods 


=> Replicaset YAMl


apiVersion: apps/v1
kind: ReplicaSet

metadata:
  name: nginx-rs

spec:
  replicas: 3

  selector:
    matchLabels:
      app: nginx

  template:
    metadata:
      labels:
        app: nginx

    spec:
      containers:
      - name: nginx
        image: nginx:latest



"""