""" 

=> Isloation In Lambda 

    -> Isolation means that every lambda function runs it own secure enviornment , 
       completely separated from other functions and other AWS customers


    -> Isolation ensure that one Lambda function cannot interfare with another lambda
       function


=> Why Isolation Needed 

    -> Imagine AWS has one physical server

        Physical Server 
           |-> Customer A
           |-> Customer B
           |-> Customer C
           |-> Customer D

    all customer share the same hardware

    -> without isolation 

       1. Customer A read customer b memory 
       2. Customer b could modify customer c file

       3. one customer crash could effect everyone

     would be massive security and reliability problem

=> Isolation

    -> Aws create a separate execution env(sandbox) for each lambda execution env


              Physical Server
────────────────────────────────────

Sandbox A
├── Firecracker MicroVM
├── Python Runtime
├── Lambda Function A
└── Memory A

────────────────────────────────────

Sandbox B
├── Firecracker MicroVM
├── Node.js Runtime
├── Lambda Function B
└── Memory B

────────────────────────────────────

Sandbox C
├── Firecracker MicroVM
├── Java Runtime
├── Lambda Function C
└── Memory C


-> Each sandbox is isolated from the others


=> What is Isloated 

1. Memory Isolation 

   1. Every function get its own memory


2. Process isolation 

   -> Suppose Lambda A start with python process

   -> Lambda B cannot 

       1. stop it 
       2. read it 
       3. modify it 

    each sandbox has its own process space


3. File system isolation


   -> each sandbox gets its own temporary storage

4. Runtime Isolation

   -> each lambda has its own runtime

      Sandbox A -> python 

      Sandbox B -> Node.js

      Sandbox C -> java 

  -> One runtime cannot affect another


5. Network Isolation 

   -> each execution environment has isolated networking

   -> if a lambda is attached to VPC

      sandbox -> Elastic Network Interface ENI -> VPC

   -> Network traffic is controlled by


       1. Security groups 
       2. Route tables 
       3. Network ACLs
       4. IAM

6. CPU Isolation

   -> Suppose Lambda A , 1024 memory

   aws allocate cpu resource based on the configured memory

   -> it cannot "steal" cpu resource allocated to lambda A


=> Firecracker Enables Isloation

   -> Firecracker provide virtualization for each execution env


   lambda -> firecracker microVM -> linux kernel -> hardware


   each mircrovm has 

      1. Virtual CPU

      2. Virtual memory 

      3. virtual network 

      4. virtual storage

   gives vm-level isloation


=> isloation during scaling

    -> Suppose 1000 uses invoke function


    1000 -> request -> 1000 execution env(as needed) -> 1000 firecracker microvm      



"""