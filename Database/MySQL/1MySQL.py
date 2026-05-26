""""  
=> String Data types in Mysql 
    
    1. CHAR (Fixed Length)

       -> ALways store exactly 10 characters , Faster than varchar 
    
    2. VARCHAR  
        
        -> Store variable length strings
        
        -> SLightly slower than CHAR (need length check)
        
        -> Varhcar is stored inside the row
    
    3 Text 
       
       -> Text is string data type that used to store large amount of text data     
       
       -> Text is outside the row (off-page)
       
       -> Table row keeps only pointer , Access text is slower 
       
       -> Types of Text 
           
           1. TINYTEXT = 255 bytes
           2. TEXT     = 65,353 bytes
           3. MEDIUMTEXT = 16MB
           4 LONG TEXT = 4GB 
      
      
      -> Only Prefix index and full text index allowed
      
      CREATE INDEX idx_comment ON comments(comment(50)); (index only first 50 char of commment , prefx index )
    
    4. BLOB 
       
       -> Binary Large Object
       -> Used to store binary data , not text
       
       
       TINYBLOB   → 255 bytes
       BLOB       → 64 KB
       MEDIUMBLOB → 16 MB
       LONGBLOB   → 4 GB
       
     -> Uses 
        1. Images 
        2. PDFS
        3. Videos 
        4. Encyrpted data
    
    
     -> Stored behaviour 
       
       1. Stored off page (outside row)
       2. Row store pointer 
       3. slower result 
       4. more disk I/O
    
    
     -> Why not store in BLOb 
      
      1. Database become huge 
      2. Backup become slow 
      3. Replication lag increase
      4. Performance degrade
    
    5. Enum 
        
        Enum is a string data type with a fixed set of alloweed rules
               
               
               CREATE TABLE orders (
                      id INT PRIMARY KEY AUTO_INCREMENT,
                       status ENUM('PENDING', 'SUCCESS', 'FAILED')
                       );                 
      
      
      -> Mysql store enum as integeer internally , not string 
             
             PENDING = 1
             SUCCESS = 2
             FAILED = 3
             
             memory efficient , comparison are fast 
      
      
      -> Enums are hard to modify
    
    6. SET 
        
        -> set is a string type that allows multiple values from predefined list
                
                CREATE TABLE permissions (
                id INT PRIMARY KEY AUTO_INCREMENT,
                access SET('READ', 'WRITE', 'EXECUTE')
                 );           
        
        -> you can store READ , WRITE  , READ , WRITE
        
        -> Working of set internally 
           
           READ  -> 1   (001)
           WRITE -> 2   (010)
           EXECUTE -> 4 (100)        
        
        -> WHy set exist
           
           To represent multiple boolean-like flag in one column
           
           access SET('READ','WRITE','EXECUTE')
        
        
        -> Voilate Normalization 
       
       -> SOlution 
          
          
          creat another table 
            
            CREATE TABLE user_permissions (
             user_id INT,
             permission VARCHAR(20)
             );                              

"""