""" 
=> Elastic IP 

   -> An Elastic IP is static public IPv4 address that you can allocate to your AWS account 
      and associate with an EC2 instance  

   -> Elastic IP does not change when you stop and start the instance 


=> Why do we need Elastic IP

   -> Suppose you launch an EC3 instance 

   -> AWS automatically assigns a public IP

      EC2  -> Public Ip -> 54.218.10.25

      even if the instance is restarted , Elastic IP remains the same when it is attached 
      to that instance 


=> Can One Elastic Ip be attached to multiple instance 

   -> One Elastic IP can be associated with only one network interface at a time

   -> We can 

     1. Disassociate if from one instance 
     2. Reassociate it with another instance 


=> Can one EC2 instance have multiple Elastic IPs?

    -> Yes, if the instance has multiple network interfaces or multiple private IP 
       addresses configured appropriately, you can associate multiple Elastic IPs.


=>  Is Elastic IP free?

    -> AWS encourages efficient use of public IPv4 addresses.


    -> Elastic IPs that are allocated but not being used incur charges.
    -> Public IPv4 addresses (including Elastic IPs) are billed under current AWS IPv4 pricing.


"""