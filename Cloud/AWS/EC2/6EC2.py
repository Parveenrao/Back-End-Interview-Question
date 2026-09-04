""" 

=> SSH And RDP

   -> When we launch an EC2 instance , we need a way to connect to it and manage it 

   -> The method depends on operating system 

       Linux   -> SSH 
       Windows -> RDP 

       

=> SSH (Secure Shell)

   -> Is a secure protocol used to access a Linux-server remotely through command line

      laptop -> Internet -> Linux EC2 instance


    -> Why SSH 

       1. without SSH

        Data Centre -> Need physical keyboard and monitor -> manage server

    -> SSH use port 22


    -> SSH Authentication 

        When you launch a Linux EC2 instance , AWS ask you to choose or create a key pair 


        key pair -> my-key.pem

        The public is placed on the instance  and we download the private .pem file

    -> Connecting with SSH

         ssh -i my-key.pem ubuntu@54.201.100.25

         ssh -> SSH client 

         -i  -> identify file 

         my-key.pem -> Private key 

         ubuntu -> Username 

         54.x.x.x -> Elastic IP

=> RDP 

    -> Remote Desktop Protocol

    -> RDP is a Microsoft protocol for connecting to a Windows server with graphical desktop


       Laptop -> internet -> Windows EC2 -> Desktop screen

    -> RDP use port 3389

=> Why is SSH considered more secure than Telnet?

   -> SSH encrypts all communication between the client and server.
   -> Telnet sends data, including usernames and passwords, in plain text.
   -> Because of encryption, SSH is the standard choice for secure remote administration.

   

"""