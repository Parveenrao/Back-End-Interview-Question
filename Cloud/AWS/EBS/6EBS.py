""" 

=> Resize EBS Volumes 

    -> Resizing an EBS volume mean increasing it storage capacity and optionally its 

       performance (IOPS and throughput) without replacing the volume


    -> Example 

       Suppose you launch an EC2 instance with 50GB EBS volume


       EC2 instance -> EBS volume (50Gb)

       After few moths 

       Operating system -> 20GB 

       Application   -> 10GB

       Database    -> 15GB

       Logs       -> 5GB

       disk become full


       instead of creating a new volume, we can resize it 


=> What we can modify 

   1. Volume size (50Gb -> 200Gb)

   2. Volume Type (gp2 -> gp3)

   3. IOPS 

   4. Throughput


=> Can we reduce size 

   -> No, we can only increase the size of EBS volume


=> Can you resize while EC2 is running

    -> AWS supports modifying EBS volumes while they are attached to a running EC2 
       instance in most cases.



"""