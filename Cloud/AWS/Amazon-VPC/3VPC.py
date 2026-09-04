""" 

=> Route Table 

   -> A route table is a set of rules (routes) that tells AWS:

            "If a packet going to this destination , send it here"

   -> Without a route table, EC2 instance would not know where to send traffic

=> Where does it exist

      VPC
       │
       ├── Route Table
       │
       ├── Public Subnet
       │      │
       │      └── EC2
       │
       └── Private Subnet
       │
       └── EC2

      a subnet is associated with one route table at a time , and multiple subnet can share the 
      same route table

=> Structur of Route Table 

    A route has two parts 


    Destination                               Target 

    Where is traffic going                     Where shoudl aws send it 



    Example:

     Destination	                            Target
        10.0.0.0/16                         	local
         0.0.0.0/0	                            Internet Gateway


   1. Route Local Route

      -> Every VPC automatically gets a local route

      -> any traffic destined for another IP address inside the VPC stays within the VPC

   2. Route Internet Route

      Destination 0.0.0.0/0 

      Target : Internet Gateway


      Means -> any IPv4 destination


=> Longest Prefix match 

   -> Aws always picks the most specific route



       Destination	      Target
       10.0.0.0/16	       local
       10.0.1.0/24	       Firewall
       0.0.0.0/0	       Internet Gateway


       if the destination is 10.0.1.25

       it match 

       10.0.0.0/16
       10.0.1.0/24


       aws choose 10.0.1.0/24


       /24 is more specific than /16

"""