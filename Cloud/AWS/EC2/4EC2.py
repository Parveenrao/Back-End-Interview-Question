""" 

=> EC2 User Data

   -> Is a script or set of commands that automatically runs when an EC2 instance launches for the
      first time

   -> Instead of manually logging in and installing software we tell EC2:

       when you start run these command automatically 


=> Why do we Need User data 

   1. Imagine we are launching Ubuntu EC2 instance 

       -> without User data

       Launch EC2 -> SSH into server -> sudo apt update -> Install nginx -> Install Git -> Install python -> start server 

       we repeat these steps every time when we create a new server 

   2. With user data 

       -> Launch EC2

       -> EC2 automatically  runs the script

       -> Everything is installed 

       -> Server is ready



=> How it is working 

  1. When an EC2 instance boots

      -> Launch instance 

      -> Operating system starts 

      -> Cloud-init reads user data 

      -> Executes command

      -> Instance Ready


    On-Linux , the cloud-init service is responsible for processing User data 

=> Where is User Data stored 

   -> User Data is stored as instance metadata by AWS and can be retrieved from within the

      instance using instnace Metadata Service 

=> Can we modify user data -> yes 

    1. we can stop the instance 
    2. Edit the user data 
    3. Start the instance again

=> what is User Data 


   ->  User Data is a startup script that automatically runs when an EC2 instance launches, 
       allowing you to automate software installation and configuration.

       
=> Which service executes User Data on Linux?

      -> cloud-init.

=> Why is User Data useful?

    -> It automates server provisioning, reduces manual work, ensures consistent configuration, 
       and speeds up deployments.             
"""