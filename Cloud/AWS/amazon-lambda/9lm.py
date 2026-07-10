""" 

=> AWS Lmabda Firecracker MicroVM Architecture

 
    -> Lambda primaruily used containers for isloation. As lambda scaled to millions of concurrent
       executions , AWS developed Firecracker

    -> A lightweight virtualization technology that combine the security of virtual machine with
       startup speeds close to containers


=> What if Firecracker 

   -> Firecracker is a open-source Virtual machine monirot(VMM) developed by AWS to run serverless
      workload like lambda and aws fargate.


    -> It contains MicroVMs that:
        1. Boot millisecond
        2. Use very little memory 
        3. Provide strong VM-level isolation 
        4. Scale to millions of instance 


    -> A tiny virtual machine designed specifically for cloud workloads


=> Why AWS did not use Traditional VM

   -> Traditional VM are secure but heavy

   application -> virtual machine -> Guest operating system -> Hypervisor -> Physical server

   -> Problems 

      1. Boots slowly (seconds to minute)
      2. Use lots of RAM
      3. Large operting system 
      4. Heavy virtualization overhead

    -> Not suitable for lambda where functions should start almost instantly


=> WHy not docker container

   -> Container are lightweight

   application -> Docker container -> Host operting system

   -> Problem 

     1. container share host kernel

     2. if there is a kernel vulnerability , isolation may be weaker than a VM


=> Firecracker Solution

   Application --> Firecracker MicroVM -> Minimal GuestOs -> Firecracker VMM -> KVm -> Linux host 

   -> Physical hardware


   -> firecracker provide 
     
      1. VM isolation 
      2. Very fast startup 
      3. small memory footprint 
      4. high density


=> MicroVM

   -> microvm is a minimal virtual machine

   -> remove necessary hardware

   -> Traditional VM

      virutal machine -> CPU -> Memory -> USB -> Sound card -> CD-ROM -> PCI Device -> Graphics

      -> Network -> Storage 

   -> fircracker keeps only what required

      MicroVM -> CPU -> memory -> Network -> Stroage

      nthng else 

      thats why it boots so quickly


=> Firecracker Internal Architecture

                    Lambda Invocation
                          │
                          ▼
               Lambda Data Plane
                          │
                          ▼
          Firecracker MicroVM Manager
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼
     MicroVM 1                      MicroVM 2
          │                               │
     Python Runtime                 Java Runtime
          │                               │
          ▼                               ▼
     Lambda Function A             Lambda Function B

     

     -> each lambda execution environment runs inside its own MircroVM


=> What happen during Cold start


     Request arrive -> Allocat Resource -> Create firecracker MicroVM -> boot minimal linus kernel 

     load runtime -> Load lambda code -> Run initialization -> execute handler


=> WHy AWS Built Firecracker 

   1 AWS needed to support 

      -> millions of lmabda invocations 
      -> Strong tenant isolation 
      -> Low latency 
      -> High server utilization 
      -> Fast scaling


=> Traditional VMs were too heavy, while containers alone did not provide the 
    isolation AWS wanted for multi-tenant serverless computing.      


=> Does every Lambda function run inside a Firecracker MicroVM?

    Yes. Each Lambda execution environment runs inside its own 
    Firecracker MicroVM, providing isolation between workloads.    


"""