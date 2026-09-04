""" 

=> StorageClasses 

   -> Storageclasses is a automation layer between PVC and the actual storage system 


=> Why was storageclasses introduced 

    -> Imagine you are kubernetes administrator

    -> There are 100 developers

    -> each developers creates a pvc


    -> without storageclasses

        1. Developer creates a PVC

        2. Admin manually creates a PVC

        3. Admin connect the PV to AWS EBS/NFS

        4. PVC finally binds

    This is called static provisioing


=> StorageClasses solve this problem 

   -> Instead of creating PV manually

   -> Developer simply creates a PVC

   -> kubernetes automatically creates the required storage

   Developer -> Create PVC -> Storageclasses -> Provisioners -> Create disk automatically 

   -> Creates PV automatically -> PVC bound

   This is called dynamic Provisioning


   When someone ask for storage like this ,  create it automatically


=> Example 


    1. Suppose you are using AWS

       Developers writes

        PVC

        20Gi SSD

       StorageClasses says

       Use AWS EBS

       SSD
       gp3
       20Gi


       Kubernetes talks to AWS API

       AWS creates an EBS volume

       Kubernetes creates a pv

       PVC bind it automatically

       Developer never see os this






"""