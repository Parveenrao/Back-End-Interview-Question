""" 
=> Partitioning means splitting a large table into smaller physicall parts  , but still treat as one table

   -> WHy partitioning 
     
     1. Faster queries 
     2. Better performance 
     3. Easy data mangement
     4. Improve index efficiency
     
-------------------------------------------------------------------------------------------------------------------

=> Range Partition 
    
    -> Split based on range of values
        
        order by values
        
        
     CREATE Table orders (
         
         id int , 
         order_date DATE
         
     )        
     
     Partition by RANGE (YEAR(order_date)) (
         
         Partition p0 values less than (2022),
         Partition p1 values less than (2023),
         Partition p2 values less than (2024)
     )
     
     -> ADd partition later 
     
     ALTER TABLE orders
       ADD PARTITION (
       PARTITION p2025 VALUES LESS THAN (2026)
      );


=> List Partition 
     
     -> Parition based on specific values
     
     CREATE TABLE  users (
         
         id int ,
         country varchar(250)
         )
         
         PARTITION BY LIST COLUMNS(country) (
             
             PARTITION india values in ('India),
             PARTITION usa VALUES in ('usa'),
             PARTITION uk values in ('uk')
         )


=> Hash Partition 
     
     CREATE TABLE products (
         id int , 
         name varchar(100)
     )    
     
     PARTITION BY HASH(id)
     PARTITIONS 4; 


=> Key partition 
      
      -> Mysql internal hash 
      
      CREATE TABLE customers (
      id INT PRIMARY KEY,
      name VARCHAR(100)
      )
     
     PARTITION BY KEY(id)
     PARTITIONS 4;         
"""