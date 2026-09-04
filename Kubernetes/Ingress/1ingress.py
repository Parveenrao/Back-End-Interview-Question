""" 

=> Ingress

   -> Ingress is an API object that manages external HTTP/HTTPS traffic into a kubernetes cluster

   -> like , traffic manager or reverse proxy

   -> Instead of exposing every application with its own Loadbalancer or Node port , we expose 
       one Ingress Controller and it routes request to differnet request 


       
=> Why do we need Ingress

    -> Imagine cluster have three application

        frontend 
        backend 
        admin dashboard

    -> without ingress

        Frontend -> LoadBalancer -> 35.1.1.1

        Backend -> LoadBalancer -> 35.1.1.2

        Admin -> LoadBalancer -> 35.1.1.3


    -> Problems 

        1. THree load balancer 

        2. Three external Ips 

        3. Higher cloud cost 

        4. Diffuct SSL management



=> What exactly ingress do

    -> Ingress perfrom routing based on 

        1. URL path 
        2. Hostname 
        3. HTTP header

        4. TSL/SSL termination


=> what is Ingress Controller 

   -> Ingress itself does not route traffic 

   -> Ingress is just of rules 

   -> Something has to read this rules and actually route the traffic

   -> componenet is called Ingress Controller 


=> Popular Ingress Controller

    1. NGINX Ingress Controller 

    2. HAPorxy

    3. Kong 


=> Example ingress file 


apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress

spec:
  rules:
  - host: myapp.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-service
            port:
              number: 80

      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 8080

"""