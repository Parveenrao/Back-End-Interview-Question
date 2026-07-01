""" 
=> EC2 (Elastic Computing CLoud)
    
    -> Is a service that gives you virtual serivce (computers) in the cloud
    
    -> Instead of buying a physical machine , you rent one online and control it


----------------------------------------------------------------------------------------------

=> WHy EC2
   
   1. Launch server in one minute 
   2. Pay for only usage
   3. scale any time

-------------------------------------------------------------------------------------------------

=> Core Concept 
  
  1. Instance 
     
     -> A running virutal machine 
   
   example 
    
    small app -> t2.micro
    AI workload -> GPU instance
  
  
  2. AMI
    
    -> Amazon layer machine 
    
     -> A pre-configure template used to launch an EC2 instance
          
          ready - made snapshot of a computer 
    
    
    -> IF EC2 = computer
        
        AMI = operating system + setup
   
   
   -> What inside in AMI 
      
      1. Operating system
      2. installed software
      3. Configuration(settings , fireWALL) 



1. Basic AMI 
    
    -> choose ununtu ami
    -> install everythig manually

2. Custom AMI
     
     -> setup everything once(Pyhthon, Redis)
     -> Create ami from that instance
     -> Next time == launch server instantly with everything ready



=> Type of AMI
   
   1. Public AMI 
        -> Provided by ami
        -> free to use
        example : Ubuntu , Amazon linux
   
   2. Private AMIs
       
       -> Created by you
       -> used in your projects 
   
   3. Marketplace AMI
        
        -> Paid , pre-configured        



----------------------------------------------------------------------------------------------

=> 3.  key Pair 
        
        -> In amazon EC2 a key pair  is used to securely log into you EC2 instance
            
            it replace password
            
            public key = stored in ec2
            private key = (.pem file) given to u
           
           we use to private key to unlock server  

=> 4. Elastic IP 
      
      -> A static fixed IP address that you can attach to EC instance
      
      -> its an ip that cannot change , evern server restart 
      
      
      -> Why exist 
      
         1. By default in EC2 instance , when stop , start instance , ip changes
            
            so client cannot connect
            
         2. So Elastic Ip solve this
             
             -> Aws give you static ip
             -> You attach it to your EC2 instance
             -> THe Ip stays until you release
      
      
      -> Important Points
          
          1. Not always free
                                                                       


"""