""" 


=> AccessMethod 

   -> An access Mode define how a Persistent Volume (PV) can be mounted by Pods

   -> It answer question like 

      1. Can only one pod use this storage 
      2. Can many pods use it 
      3. Can many pods write it to simultaneously 
      4. can it only be read

      
   -> Think of access mode as permission for mouting a disk 



1. ReadWriteOnce (RWO) 

    -> The volume can be mounted as read-write by  a single node


    -> Suppose we have , 

        Node-1

        Pod A

        Pod B

        Node -2 

        Pod - C

    both Pod A and Pod B and use the disk because they are on the same node

    Pod C cannot because it is on another node


2. ReadOnlyMany

   -> Many pod can mount the volume , but no one can write 


3. ReadWriteMany 

    -> Mulitple pods can read and write simultaneously 


4. ReadWriteOncePod

   -> Some application require exactly one pod


"""