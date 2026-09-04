""" 

=> CNI 

   -> Kubernetes define what networking should look like , CNI plugins configure the networking 
      needed to make it happen


   -> What is CNI

       -> COntainer Network Interface

       -> CNI is a specification for configuring networking for containers

       -> when kubernetes creates a pod , something has to

          1. Connect the Pod to network 
          2. assign / configure its Ip 
          3. configure interface and routes 
          4. and clean up networking when Pod disapper

Kubernetes networking model
        │
        │ "Every Pod needs networking"
        ▼
Container Runtime
        │
        │ invokes CNI
        ▼
CNI Plugin
        │
        ├── Configure interface
        ├── Configure IP
        ├── Configure routes
        └── Configure connectivity



=> Who actually calls CNI

   API Server -> Scheduler -> choose node 1 -> kubelet -> container Runtime -> CNI netorking


   modern k8s use CRI to interact with the container runtime




"""