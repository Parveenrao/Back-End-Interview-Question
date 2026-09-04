""" 

=> Secrets 

    -> A secret in kubernetes is a object used to store sensitive information such as
      
        1. Passwords 
        2. API keys 
        3. Database credentials 
        4. Oauth tokens 
        5. SSH private keys 
        6. TLS certificate 

    -> Instead of putting them in Pod yaml or configmap , we store them in a Secret and let 
       application read them securely 

=> WHy do we need Secrets 

   1. Imagine application connects to a MySQL database 

   2. Aynone who can read the Deployment YAML now knows your password

   3. Instead created a secret , password is stored separately from the application 
      configuration

=> Secrets are not encrypted , but they are base64 encoded 



=> Types of secrets 

    1. Opaque (Most commmon)

       -> Generic key-value data 

          type : Opaque

       -> Used for database , API keys , Tokens

    2. TLS certificate 

       -> Store SSL certificate 

    3. Docker registry secrets


=> For real security , enable Encryption At Rest in kubernetes

=> What is the maximum size of a Secret?

       -> A Secret is limited to 1 MiB.




"""