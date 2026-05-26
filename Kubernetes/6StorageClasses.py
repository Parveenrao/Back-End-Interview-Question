""" 
=> Storage Classes  
     
     -> A storage class define how storage should be dynamically created in kubernetes 
     
     -> When someone ask for storage , what type , speed , provider  , configuration  should kuberenetes used
     
     -> WIth storage classes = Kubernetes create volume automatically

---------------------------------------------------------------------------------------------------------------------

-> Why StorageClasses exist 
    
    1. Before storage classes
       
       -> Admin create PersistentVolume manually
       
       -> Devs request via PersistentVolumeClaim
       
       -> Match is static
    
    
    2. After storage classes 
        
        -> Dev create PVC
        
        -> Kubernetes dynamically provisions storage via storageclasses
        
        called Dynamic Provision

------------------------------------------------------------------------------------------------------------------

-> Core Component

    1. Persistent Volume 
        -> Acutal storage
    
    2.PersistenVolumeClaim
        
        -> Request for storage
    
    3. Storage Classes
         
         -> Blueprint for creating PVs dynamically

-----------------------------------------------------------------------------------------------------------------

=> Storage classes yaml
          apiVersion: storage.k8s.io/v1
          kind: StorageClass
          metadata:
             name: fast-storage
                 provisioner: kubernetes.io/aws-ebs
             parameters:
                  type: gp3
             reclaimPolicy: Delete
             volumeBindingMode: WaitForFirstConsumer   


=> PVC using it

           apiVersion: v1
           kind: PersistentVolumeClaim
               metadata:
                name: my-claim
           spec:
             storageClassName: fast-storage
                 accessModes:
                 - ReadWriteOnce
                 resources:
                      requests:
                       storage: 5Gi     
    
    
    -> Provisioner = Define who create volumne , AWS , GCP , AZURE
    
    -> Parameters 
          
          Provider config 
           
          Disk 
          Encryption
    
    -> reclaimpolicy
        
        what happens when pvc deleted 
           
           retain -> storage kept
    
    -> Volume Binding Mode
         1. Immdiate  = volume created instantly after PVC 
         
         2. Wait for First Consumer  = volume created when pod is scheduled
    
    -> Allowed volume expansion : true
         
         Allow resize pvc later                                                              
                    


"""