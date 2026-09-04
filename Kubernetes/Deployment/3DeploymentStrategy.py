""" 

=> Deployment Strategy 

    1. Rolling Update 

        -> Replace pods Gradually 

        -> Zero or near-zero downtime 

        -> Safe deployments 

        -> Easy rollback 

        -> Default in k8s

       -> Disadvantage 

       1. Old and new version run together during the udpate 

       2. If the application is not backward compatible , this can cause issue

    2. Recreate Strategy

        -> Kubernetes delete all old Pods first , then creates the new pods 

        -> during the gap , user cannot access application , cause downtime


=> Example 



apiVersion: apps/v1
kind: Deployment

metadata:
  name: nginx

spec:
  replicas: 3

  strategy:
    type: Recreate

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
        image: nginx:1.26


=> When shoud we use Recreate 


   1. Database schema change 

   2. Exclusive Resource excess

       -> Suppose application control a machine or hardware device 

       -> only one version should communicate with it at time

       -> running both version together cause conflict 




"""