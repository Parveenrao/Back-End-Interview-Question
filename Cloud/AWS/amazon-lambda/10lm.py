""" 

=> Sandbox In AWS lambda

   -> A sandbox is an isloation execution environment where lambda function runs securely 
      without affecting other functions or customers

    -> Sandbox = A secure , isloated workspace where one lambda function execute 


    -> think of like hotel room 

        1. Every guest gets a separate room
        2. Guest cannot enter another guest room

        3. if one room has problem , the others are unaffected


    -> Similary  every lambda execution environment  runs inside its own sandbox

=> Why Lambda Need a sandbox

   -> AWS lambda is a multi tenant service 

   -> Imagine million of customer

       Customer A 
       Customer B 
       Customer C

    all are using Lambda simulataneously on AWS infrastructure 


    -> without isolation 

       Custome A function -> can access -> Customer B memory

       sandbox prevent this


=> Sandbox Architecture


        Physical Server
────────────────────────────────────────

   Firecracker MicroVM (Sandbox A)

   ├── Python Runtime
   ├── Your Lambda Code
   ├── Memory
   └── /tmp

────────────────────────────────────────

   Firecracker MicroVM (Sandbox B)

   ├── Java Runtime
   ├── Another Customer's Code
   ├── Memory
   └── /tmp

────────────────────────────────────────

   Firecracker MicroVM (Sandbox C)

   ├── Node.js Runtime
   ├── Another Function
   ├── Memory
   └── /tmp

   
each MicroVM acts a sandbox


=> What is isloated

   -> each sandbox has its own:

      1. Memory 
      2. Runtime (Python , java , Node)

      3. CPU allocation 

      4. Env variables 

      5. Process space 

      6. Network namespace

   It cannot directly access another sandbox

=> What happen inside sandbox 


Event

↓

Create/Re-use Sandbox

↓

Load Runtime

↓

Load Function Code

↓

Execute Handler

↓

Return Response

↓

Freeze Sandbox



=> What Sandbox can acess

   -> AWs services(using IAM permission)
   -> The internet (if networking allows)
   -> VPC resources

   -> Temporary /tmp storage 

   -> Env varibales

=> What lambda cannot acess  

   1. Another lambda sandbox's memory 
   2. another customer processes 

   3. underlying host operating system

   4. Physical hardware directly

=> Sandbox	                                       Firecracker MicroVM
     Logical isolated execution environment	   Technology used to implement the sandbox
             Concept	                           Implementation
             Runs Lambda code                	Provides virtualization and isolation   

"""