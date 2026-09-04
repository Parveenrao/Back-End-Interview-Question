""" 

=> Security Group 

   -> A security group is a virutal firewall that controls the traffic allowed to and from an EC2
      instance

    -> Think of a security guard standing at the door of your server 

    -> Every request must pass through the Security group before reaching your instance 


=> Why do we need Security Groups

    -> Imagine EC2 instance is running 

       SSH   (Port 22)
       HTTP  (Port 80)
       HTTPS (Port 443)
       MySQL (Port 3306)

       shoudl everyone on the internet be able to access all of these , No 


     We decide 

      -> Allow SSH only from your laptop 
      -> Allow HTTP from everyone 
      -> Allow HTTPS from everyone 

      -> Allow MySql only from your application server 


=> How Security Group works 

                Internet
                  │
      ┌───────────▼───────────┐
      │     Security Group    │
      │                       │
      │  Allow Port 22 ✓      │
      │  Allow Port 80 ✓      │
      │  Block Others ✗       │
      └───────────┬───────────┘
                  │
             EC2 Instance


=> Stateful firewall

    -> Security groups are stateful

    -> If an incoming request is allowed , response is automatically allowed 

    -> we do not need to create a separate outbound rule for the response 


=> Inbound Rules 

   -> Inbound rules controll traffic coming to your EC2 instance 

     Internet -> Port 80 -> EC2 instance 

     SSh -> only you connect
    
     website -> only you connect 

=> Outbound Rules 

   -> Control traffic leaving your EC2 instance 



=> Port Numbers You Should Know
      Port	Service
      22	SSH
      80	HTTP
      443	HTTPS
      3389	RDP
      3306	MySQL
      5432	PostgreSQL
      6379	Redis
      27017	MongoDB   

=> Multiple Security Groups

    -> An EC2 instance can have multiple Security groups


    EC2 -> web security groups 

        -> SSH security groups 

        -> Monitoring security groups


=> Real Architecture 



                    Internet
                       │
                Port 80 / 443
                       │
                Web Security Group
                       │
                  EC2 Web Server
                       │
              Port 3306 (Private)
                       │
          Database Security Group
                       │
                 EC2 MySQL Server


"""