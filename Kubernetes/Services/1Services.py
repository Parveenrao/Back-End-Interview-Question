""" 

=> Services 

    -> Why do we need Services

       1. Imagine we deployed an application

          Deployment -> Replicaset 
                          |-> Pod1 10.244.1.2
                          |-> Pod2 10.244.1.3
                          |-> Pod3 10.244.1.4

       2. Suppose frontend calls 

            http:// 10.244.1.2 

            everything works 

            and now pod 1 crash

            new pod -> 10.244.1.8

            frontend still calling -> 10.244.1.2

            which is no longer exist 

            pods are ephemeral

            They are constantly created and destroyed

            Their Ip address are not permanent 


=> Kubernetes Solution 

  -> kubernetes introduce service 

  -> A service provide a stable IP address and stable DNS name for a group of Pods

  -> Instead of talking directly to pods 

      frontend -> pod 

      frontend -> my-service

      The service automatically forwards traffic to one of matching pods 


=> Services 

   -> A service is an abstraction thats sits in front of pods 

                               Service
                               10.96.0.5
                                 │
                         ┌───────┼────────┐
                         │       │        │
                       Pod1     Pod2     Pod3


   -> Client connect only to the serives 

   -> They never care about Pod IPs

=> Service Component 

   1. Stable IP (Cluster Ip)

   2. Stable DNS

   3. Load balancing 

   4. Pod Discovery


=> How does service know which pod

    -> Using label selector
        
        pods
        labels:
           app : backend
 
        services

           selectors:
              app : backend


=> Basic service yaml 


apiVersion: v1
kind: Service

metadata:
  name: backend-service

spec:
  selector:
    app: backend

  ports:
    - port: 80
      targetPort: 8080

      
=> Key Interview Points 

    1. Pods are empemeral , their Ips change 

    2. Service provides a stable Virutal IP and DNS name 

    3. Services do not create pods 

    4. Service distribute traffic across matching pods (basic load balancing)

    5. Application shoudl communicate using services not Pod Ips

"""