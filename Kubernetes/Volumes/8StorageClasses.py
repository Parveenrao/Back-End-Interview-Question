""" 

=> Componenet Of StorageClasses 

   
    1. Provisioner

        -> A Provisioner is a software component that knows how to create storage on a specific 
           system , think of it as a storage manager

        -> When kubernetes receives a storage request , it does not know how to create an 
           AWS EBS volume , Azure volume or an NFS share 


         -> Kubernetes does not know 

              1. How to create an AWS EBS volume 

              2. How to create an Azure disk 

              3. How to create an persistent disk 


             every storage system has different APIs

             kubernetes cannot implement all of these himself

             instead it delegates the work to a provisioner 


User creates PVC

        │
        ▼
Kubernetes API Server

        │
        ▼
StorageClass Found

        │
        ▼
Provisioner Selected

        │
        ▼
Provisioner Calls Storage API

        │
        ▼
Disk Created

        │
        ▼
PV Created

        │
        ▼
PVC Bound

        │
        ▼
Pod Starts


=> What does Provisioner Actually do 

    1. Create new storage volume 

    2. Deleting the volume when required 

    3. Expanding the volume 

    4. Creating snapshot

    5. Cloning volumes

    6. Returning details like the volume ID and capacity to kubernetes

=> Type of Provisioners


   1. In-tree Provisioners

       In older kubernetes version , storage code was built inside kubernetes itself 

       Problem 

        1. Every cloud providers code lived inside kubernetes 

        2. adding a new storage backend require changing kubernetes itself 

        3. Release become harder itself 


    2. CSI Provisioners 

       -> Today kubernetes , Container Storage Interface


       kubernetes -> CSI Drivers -> Storage System

       Now storage vendor , maintain their own CSI drivers 


=> Can multiple StorageClasses use the same provisioner?

     -> Yes.           


"""