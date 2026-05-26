"""  
_format_version: "3.0"

services:
  - name: user-service
    url: http://localhost:8000
    routes:
      - name: user-route
        paths:
          - /users




1. services : 
    
    -> Start defining your services 

2. -name : user-service 
     
     -> just a label , not visible to others 

3. Backend URL ( url: http://localhost:8000)
      
      -> where your actual backend lives

4. routes :

     -> Define how user accesss services

5. - name: user-route    
     
     -> just an label 

6. Path: 
    -> This is the entry points for all clients
    
    
=> When client calls 
    
    GET/user 
    
    -> Kong find route /user 
    -> map to user service 
    -> forward request to         http://localhost:8000/users              










"""
