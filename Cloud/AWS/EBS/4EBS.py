""" 
=> Amazon EBS Snapshot

    -> An EBS snapshot is a point-in-time backup of an EBS volume

    -> AWS store snapshot in Amazon S3 , we don't see manage the S3 bucket directly .

      They are used for backup , diaster recovery and creating new EBS volume


=> Why do we Need snapshot

   -> Imagine your EC2 instance has 

     EBS volume

       1. Ubuntu OS
       2. MySQL database 
       3. Images 
       4. Application code 

       if the volume is accidently deleted 

       data become corrupted

       the instance failed


       without snapshot , data may be lost

       with snapshot , you can restore anything to the state it was in when the snapshot was taken


=> Working 

  1. Create an EBS volume

 EC2 Instance
      │
      ▼
+----------------+
| EBS Volume     |
| OS             |
| Database       |
| Logs           |
+----------------+


2. Create snapshot 


  EC2 Instance
      │
      ▼
+----------------+
| EBS Volume     |
+----------------+
      │
      ▼
 Snapshot (stored by AWS in S3)


3. Volume fails


4. Restore 


Snapshot
    │
    ▼
New EBS Volume
    │
    ▼
Attach to EC2



=> Incremental snapshot 

    -> One of the biggest advantage of EBS snapshot is that they are incremental


       1. First snapshot

          Volume 100 Gb

          Snapshot 1

          100 Gb stored 

       2. Second snapshot

          suppose you only 5 gb of data 

          instead of storing another 100gb

          snapshot 2 

          5gb data stored 

        AWS stores only the blocks that changed since the previous snapshot.

        This saves both storage space and cost. 



=> Can we create multiple volumes from one snapshot = Yes 

   Snapshot 
      |->    volume 1
      |->    volume 2
      |->    volume 3

    this is useful when you want multiple server with same data 


=> Can we take snapshot while EC2 is running = yes 

    AWS allows snapshots of attached EBS volumes while instance is running


=> Where are EBS snapshot stored

   -> They are stored by AWS in Amazon S3 , managed internally by AWS

=> Can you restore a deleted EBS volume?

    ->  Yes, if you have a snapshot. You create a new EBS volume from the snapshot and 
        attach it to an EC2 instance.   


=> Can one snapshot create multiple volumes?
 
      -> Yes. A single snapshot can be used to create multiple EBS volumes.        
      
      """  