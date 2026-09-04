""" 


=> Endpoint-Endservice 

    -> A service only knows which pods it should send traffic to 

    -> Endpoints and EndpointsSlices store the actual Ip addresses of those Pods


=> Idea 
   
   -> Suppose we have 

        3 pods 
        1 ClusterIP Service 

   -> How does service know the Ip addresses of Pod1 , Pod2 , Pod3

   -> Endpoint or Endpointslices

=> What is Endpoint 

    -> A endpoint is simply a list of Pod Ips addresses that belong to a service 

    -> Example 

       Pod 1 -> 10.244.1.5

       Pod 2 -> 10.244.1.6

       Pod3 -> 10.244.1.3

       Endpoint object 

       nginx-service 

       10.244.1.5

       10.244.1.6


       when traffic reaches the service , kubernetes choose one of those IPs and forward the request 


=> Architecture       


Client
   |
ClusterIP Service
   |
Endpoints
   |
+------+-------+------+
|      |       |      |
Pod1  Pod2   Pod3

The service itself does not store pods Ips

it Looks up  from the Endpoint/endpointslice resources


=> view endpoints 


kubectl get endpoints



=> what is endpointslice 


     -> As kubernetes cluster grew larger , EndPoint become inefficient

     -> Imagine  , 10000 Pods


     -> One endpoint object would containe 


        Pod 1  , Pod 1, Pod 3 .... Pod1000


        every update require changing this single large object 

        to solve this , kubernetes introduced endpointslice 

    -> instead of one huge list 


    -> kubernetes creates multiple smaller endpointslices


    -> Endpointslice 1

       POd 1 , Pod2 ..... Pod101

    -> Endpointslice 2 

      Pod 102 , Pod 103 ...... Pod 200

    -> endpointslice 3


=> By default, Kubernetes creates a new EndpointSlice when an existing 
   one reaches around 100 endpoints.             

   
=> Architecture with endpointslices 


               Service
                  |
      +-----------+-----------+
      |           |           |
 Slice1       Slice2      Slice3
      |           |           |
   Pods        Pods        Pods

   

=> Viewendpointslices 


kubectl get endpointslices


"""