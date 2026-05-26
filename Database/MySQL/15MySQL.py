""" 
=> Backup In Mysql 
    
    -> A backup = copy of your database so you can restore it 
       
       1. server crash
       2. data get deleted
       3. buc corrupts your db


---------------------------------------------------------------------------------------------

=> Backup A Single Database       

    -> In mysql server there are multiple database
        
        users_db , orders_db , analytic_db
        
    mysqldump -u root -p users_db > users_db_backup.sql 
    
    -> This create a file      users_db_backup.sql 
    
    -> inside that backup 
       
       table structure 
       data
       indexes
       
       for one single db
       
       
    -> Restore 
     
     
     mysql -u root -p users_db < users_db_backup.sql



=> Backup all db 
   
      mysqldump -u root -p --all-databases > all_databases_backup.sql
      
      -> Dump every database
      
      -> include table , data + structure 
      
      -> store everything in one .sql file
      
      -> what get included 
          
          1. All your database user 
          
          2. System db 
          
               mysql ( users and permissions) 
               
               information schema 
               
               performance schema
     
     
     -> Better 
     
         mysqldump -u root -p --all-databases --single-transaction --quick > backup.sql 
         
           --single txn = no locking 
           
           --quick handle large data 
     
      
      -> backup with compression 
          
          mysqldump -u root -p --all-databases | gzip > backup.sql.gz


=> Backup only table 
    
    mysqldump -u root -p database_name  table_name  > table_backup.sql
    
    mysqldump -u root -p mydb users > users_backup.sql
    
    -> Restore table 
           
           mysql -u root -p mydb < users_backup.sql
           
    
    -> only structure no data 
      
      mysqldump -u root -p --no-data mydb users > users_schema.sql
      
    
    -> only data no structure
       
       mysqldump -u root -p --no-create-info mydb users > users_data.sql
    
    -> backup multiple table 
        
        mysqldump -u root -p mydb users orders products > backup.sql                                         
        

"""