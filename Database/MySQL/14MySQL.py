""" 
=> How to add user and grant permission to user 

  
  1. User can connect from same machine 
     
     Create USER 'parveen@localhost' IDENTIFIED BY 'mypassword123'
       
       parveen -> username 
       localhost -> only connect from same machine 
  
  2. User can connect from anywhere 
     
     CREATE USER 'parveen@%' IDENTIFIED BY 'mypasssword'
  
  
  3. To Specific user 
     
     CREATE USER 'parveen@192.xxx.xxx' BY 'mypassword' 

----------------------------------------------------------------------------------------------------

=> Grant Permission 
     
     1. GIVE all permission on data base
               
               GRANT ALL PRIVILEGES ON mydb.* TO 'parveen'@'localhost';
     
     2. GIVE limited permission 
                
                GRANT ALL PRIVILEGES ON mydb.* TO 'parveen'@'localhost';
     
     3. APPly permission 
         
         FLUSH priviliges
     
     
     4. LOgin with new user
               
               mysql -u parveen -p
     
     5. CHeck user 
              
              SELECT user, host FROM mysql.user;                                               

"""