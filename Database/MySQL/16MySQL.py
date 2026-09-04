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


=> MySQL doesn't use a global unique index across partitions, 
   every PRIMARY KEY or UNIQUE KEY must include the columns used for partitioning. 
   This allows MySQL to enforce uniqueness using the local index of the relevant
   partition."     

   CREATE TABLE employees (
    id INT,
    department_id INT,
    name VARCHAR(100),
    PRIMARY KEY (id, department_id)
     )
    PARTITION BY HASH(department_id)
    PARTITIONS 4;



    department_id decides which partition stores the row.
    (id, department_id) is the primary key.
    department_id itself can repeat. 
    The combination (id, department_id) cannot repeat.

    "MySQL requires the partition key in every unique key because indexes are 
    local to partitions, and MySQL needs to enforce uniqueness without searching all partitions."
"""