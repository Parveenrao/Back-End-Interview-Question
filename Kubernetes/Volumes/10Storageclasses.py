""" 


=> Allowvolumeexpansion

    -> allowvolumeexpansion tells kubernetes whether a PVC created from a storageclasses
       can be resized after it has already been created

         alllowvolumeexpansion : True

        if it enabled , we can increase the storage requested by the PVC

    -> why do we need it 

       1. Imagine application  start with a 20Gi disk

           application -> PVC -> 20Gi

           after few months , application store more data 


           without volume expansion , we would have to 

            1. Create new larger volume 
            2. copy all the data
            3. stop the application 
            4. attach new volume


            User Updates PVC
       │
       ▼
API Server
       │
       ▼
PVC Size Changed
       │
       ▼
CSI Controller
       │
       ▼
Cloud Provider Expands Disk
       │
       ▼
Filesystem Expanded
       │
       ▼
Application Gets More Space


=> Requirements for volume expansion

allowVolumeExpansion = true
            ✔

CSI Driver Supports Expansion
            ✔

Storage Backend Supports Expansion
            ✔

Filesystem Supports Resize
            ✔

            
============================================================================

=> VolumeBinding Mode

    -> It determine when kubernetes bind a persistentvolume pv to pvc 

    -> There are two values

       1. Immediate 
       2. Waitforfirstcustomer


=> why do we need volumebindingmode

    -> Suppose you have kubernetes cluster with nodes in different availability zone

            
             
               Kubernetes Cluster

       Zone A                    Zone B
   +------------+            +------------+
   | Node-1     |            | Node-3     |
   | Node-2     |            | Node-4     |
   +------------+            +------------+

         Your storage (for example, an AWS EBS volume) is zonal.


         That means a volume created in Zone A can only be attached to nodes in Zone A.


         -> suppose we create a pvc , kubernetes creates a volume immedaitely 

         -> but later scheduler decide to run pod on Node-3

         -> now kubernetes tries to attach disk

             pod remains pending because disk in the wrong zone


        -> Option 1 Immediate

           volumebindingmode : immedaite 

           as soon as the pvc is created , kubernetes provision and binds a pV

           volume is created before kubernetes knows where the pod will run


        -> option 2 waitforfirstcustomer

           do not create or bind pv until a pod actually use the pvc

           now the storage is created after kubernetes knows where the pod will run

           
Deployment

↓

PVC Created

↓

No PV Yet

↓

Scheduler Picks Node

↓

Create Disk in Same Zone

↓

Attach Disk

↓

Start MySQL        



"""