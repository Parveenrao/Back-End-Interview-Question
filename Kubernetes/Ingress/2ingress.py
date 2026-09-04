""" 


=> TLS(HTTPS) Support

   -> Ingress can terminate SSL/TLS


   Internet -> HTTPS -> Ingress Decrypt SSL -> Service -> Pods

   Instead of configuring certificates in every application, 
   you can manage them centrally at the Ingress.


=>                    Internet
                        │
                 https://myapp.com
                        │
                LoadBalancer Service
                        │
              NGINX Ingress Controller
                        │
                  Reads Ingress Rules
             ┌──────────┴──────────┐
             │                     │
         /api                  /shop
             │                     │
      api-service          shop-service
             │                     │
        API Pods             Shop Pods   

        
=> What is Ingress?

    -> An API object that manages external HTTP/HTTPS access to services in a 
       Kubernetes cluster using routing rules.        

=> Does Ingress expose Pods directly?

    -> No. It routes traffic to Services, which then forward traffic to Pods.   

=> Can Ingress work without an Ingress Controller?

    -> No. The Ingress resource only defines rules. An Ingress Controller 
       is required to implement those rules and route traffic.        

"""