""" 

=> Types Of ELB


   1. Application Load Balancer 

      -> Layer 7(Application Layer )

      -> Protocol supported

         HTTP 
         HTTPS
         HTTP/2

         websocket
         grpc

       -> Working 

          It understand the content of HTTP request and can make routing decision based on:

          1. url path 
          2. Host name 
          3. HTTp header 
          4. Query parameter

        -> Features 

          1. Path-based routing 
          2. Host based routing 
          3. SSL termination 
          4. Sticky session
          5. Websocket support 
          6. grpc support 
          7. Health check 
          8. Integrate with Auto scaling 
          9. Support container (ECS/EKS)

       -> Use case 

         1. Web application 
         2. Rest API
         3. Microservice 
         4. Kubernetes 
         5. Container-based applications

    2. Network Load balancer 

       -> Layer 4 (Transport Layer)

       -> Protocol supported 

          1. TCP
          2. UDP
          3. TLS

       -> it does not inspect HTTP request . It forward traffic based on IP address and ports


       -> Features 

         1. very low latency 
         2. handle millions of request per second 
         3. Preserve the client original IP address
         4. Static IP address
         5. High performance

       -> Use case 

          1. Gaming server 
          2. VoIp
          3. Financial application
          4. Real-time system 
          5. Database traffic 
          6. IoT application

    3. Gateway Load Balancer (GWLB)

       -> Layer (3/4) (network)

       -> GWLB is used to distribute traffic across virtual network appliances such as 

          1. Firewall
          2. Intrusion Detection system 
          3. Intrusion Prevention system 
          4. Deep packet inspection system

       -> Use 

          1. Enterprise security 
          2. Firewall farms 
          3. Network monitoring 
          4. Packet inspection

    4. Classic Load Balancer 

       -> Legacy service 

       -> Support 

         1. HTTP
         2. HTTPS
         3. TCP
         4. SSL

       Internet -> Classic LB -> EC2 instance 


       -> Limitation

         1. No path based routing 
         2. No host based routing 
         3. Fewer feature than ALB
         4. Manily for older application                                   

"""