""" 

=> PVC (Persistebt Volume Claim)

    -> A Persistent Volume Claim is a request made by a Pod for storage

    -> Developer says , i need 10GB of fast SSD storage

        Kubernetes finds a matching PV automatically

=> PVC is a request for storage by a user , It is similar how a POD request CPU and Memory


=>                   Developer

                        │

                    Create PVC
                        │

                        ▼

      +-----------------------------+
      | PersistentVolumeClaim (PVC) |
      +-----------------------------+
               Requests

            20Gi Storage
            ReadWriteOnce
            StorageClass=fast

                        │

            Kubernetes Control Plane

                        │

          Finds matching PersistentVolume

                        ▼

      +-----------------------------+
      | Persistent Volume (PV)      |
      | 20Gi                        |
      | ReadWriteOnce               |
      +-----------------------------+

                        │

                        ▼

                 Physical Storage

             AWS EBS / Azure Disk
             NFS
             Ceph
             Local Disk

             

=> Component Of PVC

   ->  A PVC mainly specifies

        1. Storage size 
        2. Access Mode
        3. Storage class


=> Binding Process

    -> Let say we have three PVs

        PV-1

        5Gi
        ReadWriteOnce 


        PV-2

        10Gi
        ReadWriteMany


        PV-3

        20Gi
        ReadWriteOnce

        Now developer creates

        PVC

        Need
        10Gi
        ReadWriteMany


        Kubernetes searches

        PV-1 Too small

        Pv-2 Perfect 

        Pv-3 Wrong access Mode


=> Binding Rules


   -> A Pv matches only if all required conditions are satisfied


      1. Enough storage 

      2. Access mode 

      3. Storage classes 

=> PVC State 

   1. Pending

        PVC pending -> no matching PV

   2. Bound 

       PVC bound 

       PVC -> PV      Storage Ready 

   3. Lost 

       Occurs when underlying storage disappers


=> How Pods Use PVC

   -> Pods do not mount a PV directly. They mount a PVC

      Pod -> PVC -> PV -> Disk


=> Can one PVC bind to multiple PVs?

    -> No. A PVC binds to only one PV.   


=> What happens if no matching PV exists?

    -> The PVC remains in the Pending state until a suitable PV is available 
       or one is dynamically provisioned (if a StorageClass is configured).    

=> Can a PVC request less storage than the PV provides?

     -> Yes. For example, a PVC requesting 5Gi can bind to a 10Gi PV 
        if all other requirements (access mode, storage class, etc.) also match.          



"""