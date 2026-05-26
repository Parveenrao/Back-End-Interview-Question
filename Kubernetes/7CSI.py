""" 
=> Container Storage Interface
    
    -> Standard api that let kubernetes talk to any storage system (AWS , EBS , GCP) without hardoding support
    
    -> Before CSI 
        
        Kubernetes had in-tree plugins (tight coupling)
    
    -> After CSI
        
        Storage vendors built their own drivers
        
        kubernetes just call standard apis
        
        
        Kubernetes Control Plane
                   ↓
     CSI Driver (Controller + Node components)
                   ↓
   Storage Backend (EBS / Disk / Network Storage)  

---------------------------------------------------------------------------------------------------------------

=> CSI Component 
    
    1. Controller Plugin
        
        -> Run as pod in cluster 
        
        -> Responsibility 
         
         Create volume
         delete volume
         attach volume to node
    
    
    2. Node Plugin
        
        -> Run as DaemonSet
        
        -> Responsibility 
        
          mount volume to nod
          unmount volume
          make it available to containers
    
    
    3. Side car containers
    
        -> External-provisioner
            
            watches pvc
            
            call csi-create volume
        
        -> external attacher 
            
            Attach volume to node
        
        -> external-resizzer
        
            handle volume expansion
        
        -> external snapshotter
            
            create volume snapshot

-------------------------------------------------------------------------------------------
  
-> Flow 
    
    1. PVC Created 
    
    2. external-provisioner wakes up 
       
       see new pvc
       
       call csi driver 
    
    3. csi talk to cloud
       
       AWS -> create EBS volume
       
       GCP -> creates persistent disk
    
    4. PV is created 
        
        PVC get bound
    
    5. POD scheduled 
        
        Now kubernetes knows
          
          which node will run the pod
    
    6. external-attacher  
        
        calls - 
           
           ControllerPublishvolume()
           
           attach disk to node
    
    7. Node plugin
        
        calls , node pulishvolume
        
        
        mount volume to pod                                                                

"""