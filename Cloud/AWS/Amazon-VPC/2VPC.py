""" 

=> Network(Subnet) In a VPC

   -> A VPC is your private network in AWS

   -> inside vpc , we divide the ip address range into subnets

   -> a subnet can be either public or private

   -> the difference is whether resource inside it can directly communicate with the internet



1. Public Subnet

   -> A public subnet has a route to an internet gateway (IGW)

      Internet -> Internet Gateway -> Public subnet -> EC2 instance


      | Destination | Target           |
      | ----------- | ---------------- |
      | 10.0.0.0/16 | local            |
      | 0.0.0.0/0   | Internet Gateway |

      
      the route 0.0.0.0/0 -> Send all internet traffic to the internet gateway


    -> Resources usually placed in Public Subnet 

        1. Web server 
        2. Load balancer 
        3. Bastion Host 
        4. NAT Gateway

2. Private Gateway 

   -> A private subnet does not have a route to the internet gateway

   -> therefor aws no idea where internet traffic should go

=>  Public Subnet
      Application Load Balancer
      NAT Gateway
      Bastion Host (if used)

=> Private Subnet
     Application Servers
     Backend Services
     Databases
     Cache servers
     Internal APIs

     This design reduces the attack surface because only the load balancer is 
     exposed to the internet.   



"""