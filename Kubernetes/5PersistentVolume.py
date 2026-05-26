""" 
=> Persistent Volume
   
   1. Containers are ephermeral
   2. If pod dies -> data gone
   
   3. Thats unacceptable for logs , databases , user uploads
   
   4. so kuberneted separater 
        
        -> Compute pod 
        -> Storage volumes



======================================================================================================

1. PV (Persistent Volume)
    
    -> Disk on node
    -> actual storage (disk)
    
    -> created by admin or dynamically
    
    -> can be network storage (NFS)
    
    -> CLoud storage(EBS , GCE)
    
    -> Pv exist independently of PODS


=> PV architecture
       
       1. PV         = storage resource 
       2. Kubernetes = manager    
       3. POD        = consumer (indirect via PVC)
       
       
       apiVersion :v1
       kind : PersistentVolume
       
       metadata:
         name : my-pv
       
       spec : 
         capcacity:
            storage : 1Gi
         accessMode:
            - ReadWriteOnce
         
         hostpath:
           path : /data/my-app
      
      
      -> Capacity 
          
          how much storage 
      
      -> accessMode
          
          how this volume can be used 
          
          ReadWriteOnce -> One Node
          ReadWriteMany -> multiple node
          ReadonlyMany  -> read-only shared
       
       -> hostpath
           
           use node local disk
    
    
--------------------------------------------------------------------------------------------------------

-> PV Lifecycle 
    
    Available -> read to use
    Bounded  -> connecte to PVC
    Released -> PVC deleted 
    Failed  -> Something wrong


=> Reclaim Policy 
     
     persistentVolumeReclaimPolicy: Retain
     
     Retain → data stays (manual cleanup)
     Delete → auto delete storage
     Recycle → deprecated        


============================================================================================

-> Create pv
     
     apiversion : v1
     kind  :  PersistentVolume
     metadata:
        name : testing-pv
     
     spec:
       capacity:
          storage : 1Gi
       accessMode:
            ReadWriteOnce
       
       hostpath:
          path : /tmp/data
    
    
    kubectl apply -f pv.ymal
    kubectl get pv                                                         



==========================================================================================================
==========================================================================================================

=> PVC (Persistent Volume Claim)
    
    PVC = request for storage 
    
    not storage itself -> It is demand
    
    “I need 2Gi storage with ReadWriteOnce access”
    
    Kubernetes then:
    finds a matching PV
    binds it to the PVC
    
  
  -> Flow
      
      POD ---> PVC --> PV
      
      pod never directly to pv
      
      apiVersion: v1
      kind: PersistentVolumeClaim
      metadata:
        name: my-pvc
      spec:
        resources:
         requests:
           storage: 1Gi
      accessModes:
        - ReadWriteOnce  
        
     1. Resource.request.storage 
         
         -> How much storage you want
         
         pVC <= PV
         
         if PVC ask more than availabe pv , it wont bind
     
     2. accessMode:
          
          must match PV
          
        PVC = ReadWriteOnce
        PV = ReadWriteOnce
          
          binds 
       
       mismatch -> no bind
     
     3. storageclassName : standard
         
         -> This enable dynamic provisioning
         
         -> if not specified
              kubernetes tries to match existing(PV)
         
         -> If specified
             
             kubernetes creates PV automatically

--------------------------------------------------------------------------------------------------

=> BInding Process
    
    1. PVC created 
    2. kubernetes search for PV where
         
         capacity > request
         accessMode match 
         storageclass match
    
    3. if found -> Bound state
    
    4. if not
        
        wait(pending)
        or create new pv(if storageclass exist)


=> PVC Lifecycle 
   
   Pending = waiting for pv
   Bound = connected to pv
   lost = pv deleted/problem

==============================================================================================================

=> Step 1 create PV
               
               
               apiVersion: v1
               kind: PersistentVolume
               metadata:
                 name: my-pv
               spec:
                 capacity:
                     storage: 2Gi
               accessModes:
                    - ReadWriteOnce
               hostPath:
                path: /tmp/data                

=> Step 2  Create PVC
                      
                      
                      apiVersion: v1
                         kind: PersistentVolumeClaim
                      metadata:
                          name: my-pvc
                      spec:
                         resources:
                       requests:
                        storage: 1Gi
                        accessModes:
                           - ReadWriteOnce      
        
        PVC binds to PV
        1Gi requested 2Gi availabe -> OK


=> Using PVC in pOd
                     
                     
                     apiVersion: v1
                       kind: Pod
                     metadata:
                       name: my-pod
                    spec:
                      containers:
                        - name: app
                           image: nginx
                            volumeMounts:
                            - mountPath: /data
                              name: storage
                                volumes:
                              - name: storage
                          persistentVolumeClaim:
                        claimName: my-pvc        
                                                                  
"""