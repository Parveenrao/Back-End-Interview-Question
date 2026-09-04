""" 

=> Volumes Type 


   1. General Purpose SSD(gp3) , Most popular

      -> Best for most application 

      -> Web server 

      -> Application server 

      -> Small to medium database 

      -> Boot volumes

      -> Features 

        1. SSD-based 
        2. Low latency 
        3. Good balance of price and performance

        4. Can independently configure

           -> storage 
           -> IOPS 
           -> Throughput

         Default choice for most EC2 instance 

    2. Provisioned IOPS SSD(io2)

        -> Most critical - application requiring extremely high performance

        -> Orcale database 
        -> MySql
        -> PostgresSql 
        -> Sql server 
        -> SAP HANA

      -> Features

         1. Highest IOPS
         2. Very low latency 
         3. Designed for heavy database load
         4. More expensive than gp3 

    3. Throughput Optimized HDD(st1)

       -> Large files that are read and written sequentially

          1. Hadoop
          2. Video processing 
          3. ETL jobs      

       -> Features based 

          1. HDD based 
          2. High throughput 
          3. Lower cost than SSD
          4. Not suitable for database

    4. Cold HDD(sc1)

       -> Best for infrequently accessed data 

          1. Backup 
          2. Archived logs 
          3. Old reports 
          4. Historical data 


        -> Features 

          1. HDD based 
          2. Lowest performance 
          3. Suitable when data is rarely accessed 

    5. Mangnetic (Standard)

       -> Old generation EBS volume 

       -> Lowest performanc 

       -> Mostly kept for backward compatibility 

       -> Rarely used for new application                         



"""