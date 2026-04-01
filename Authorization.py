""" 
=> Authorization is the process of determining what actions an authenticated user is allowed to perform. 
It happens after authentication and is typically implemented using roles, permissions, or policies.

--------------------------------------------------------------------------------------------------------------------

1. RBAC -> ROle Based Access Control 
    
    Admin --> full access 
    User  --> Limited access 
    
    We predefined roles 

---------------------------------------------------------------------------------------------------------------------

2. Permission Based Access  

    -> Instead of Access 
       
       we gave permission , like Read , Write , Delete 
       
       more control 

-----------------------------------------------------------------------------------------------------------------------

3. ABAC -> Access Decision  based on attributes

      ->  Types of Attributes (VERY IMPORTANT)
            1. User Attributes
               id
               role
               department
               location         

            2. Resource Attributes
               owner_id
               department
               type
            
            3. Action
               read
               write
               delete
               
            4. Environment Attributes
                 time
                 IP address
                
                device
        
        =>  Real Example
  
             Allow access if:
            - user.department == resource.department
            - AND action == "read"
            - AND time < 6 PM

        
         This is ABAC (dynamic decision)

       => How It Works (Backend Flow)
 
           1. User sends request
           2. Backend authenticates (JWT/session)
           3. Fetch user attributes
           4. Fetch resource attributes
           5. Evaluate policy
           6. Allow or deny

"""