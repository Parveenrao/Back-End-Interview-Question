""" 


=> Container Runtime


                 Control Plane
                      │
                 API Server
                      │
                  Scheduler
                      │
          Pod assigned to Node
                      │
                      ▼
                Worker Node
                      │
                 kubelet
                      │
          Container Runtime Interface (CRI)
                      │
                 containerd
                      │
                    runc
                      │
               Linux Kernel
                      │
                Containers

=> Kubelet never create containers 

    -> It ask the container runtime to do it 


=> What is Container Runtime 

   -> A container Runtime is a software responsible for 

      1. Pulling container image 
      2. Creating containers 
      3. Stopping containers 
      4. Starting containers 
      5. Deleting containers


=> Why kubelet does not run container

    Kubelet has to understand

    1. Docker 
    2. containered
    3. CRI-O
    4. Future runtimes

    Kubelet become large 


=> What is Containered

   -> Containered is a high performance container runtime

   -> Pull image , store imgae ,manage snapshot , create container , mange container lifecycle


=> What is runc 

    Containered -> container (No)


    -> Actually 

    containered -> runc -> Linux Namespace -> Linux cgroups -> containers 




"""