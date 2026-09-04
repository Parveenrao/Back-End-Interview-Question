""" 

=> Persistent Storage 

    -> Data continue to exist even after the computer or server is turned of , restarted or
       crash

     -> RAM(Memory)

        -> If power goes off , everything disappers.
        -> Non-persistent (volatile)

     -> Hard Disk/SSD

        -> Persistent (Volatile)


=> In AWS EC2 , without EBS

   -> suppose we launch an instance  and save a file

   -> EC2 = Temporary Storage = report.pdf

   -> if instance is terminated , report.pdf is gone 


=> With EBS 

   EC2 = EBS Volumes = report.pdf

   Restart , Stop , start -> file is still there






"""