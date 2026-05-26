""" 
=> Port 
   
   -> A port is just a number assigned to process on a machine 
   
   IP_address = house address
   Port = room number inside the house
   
   192.168.1.10:80
   
   go to that computer
   enter through room 80(port)


-----------------------------------------------------------------------------------------

=> Common Ports
   
   Port	  Service	  Use
    80	  HTTP	   Normal websites
    443	  HTTPS	   Secure websites
    22	  SSH	   Remote login
  3306	           MySQL Database
  5432	           PostgreSQL Database
  6379	           Redis	Cache
  27017	           MongoDB	NoSQL DB   


--------------------------------------------------------------------------------------------

=> Important COncepts
  
  1.Well-knows ports 
    
       used by standard ports (0-1023)
    
      used by standard service
  
  2. Registered ports (1024 - 49151)
     
       used by apps 
  
  3.Ephermeral ports (49152 - 65535)
      Temporary ports (client side)   


----------------------------------------------------------------------------------------

=> Real-world relevance (don't skip this)

       When you deploy apps (Docker, cloud, APIs):

       You map ports:

        localhost:3000 → container:80        

"""