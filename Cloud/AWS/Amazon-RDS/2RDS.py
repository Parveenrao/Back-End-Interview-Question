""" 

=> RDS Component 

   1. DB Instance

       -> The DB instance is the actual database server 

       -> IT contains 

           1. CPU 
           2. Memory 
           3. Storage 
           4. Database software 

        -> example
                          db.t3.micro

                          2 vCPU

                          1 GB RAM

                          20 GB Storage

                           MySQL   

   2. DB Engine 

      -> This is the database software

      -> Example , Mysql , PostgresSql 

      -> When creating RDS , AWS aks 

           Which engine do you want

   3. Storage 

       -> Database file stored on EBS volumes

   4. Instance Class

       -> RDS instances have different CPU and RAM


   5. RDS Endpoint

       -> Unlike running a database on a fixed IP , RDS provide a stable DNS endpoint

       -> Your application connect to this endpoint 


=> High Availability (Multi A-Z)

    -> With Multi AZ

      Primary Database -> Synchronous Replication -> Standy Database 


      if the primary db fails -> AWS automatically -> Standby become primary



=> Read Replicas 

    -> Read replicas improve read performance , not availability 

    -> Reads go to replica

    -> write go to primary

=> Automatic backup 

    -> AWS automatically backs up database

    -> Retention (1 to 35 days)

        we can restore to any point within the retention window (depending on engine)

=> Manual Snapshot 

   -> never expire until deleted

   -> use them before 

       1. Upgrading 
       2. Migrating 
       3. Large changes 

=> Point-In-Time Recovery

   9:00 AM -> DB OK

   10:30 Someone delete tables 

   11:00 AM -> oops 

   we can restore the db to 10:29 AM


=> Security 

   -> RDS use multiple layer security

   -> Security groups

       Control who can connect

    -> IAM 
       IAM controls who can

       1. Create database 
       2. Delete database 
       3. Modify database 

    -> Encrypt 

       AWS encrypt 

       1. Storage 
       2. Snapshots 
       3. Replicas

     using AWS Key Management Service(KMS)

     -> SSL 

        Application can usee SSL/TLS to encrypt data in transit 

=> Monitoring 

    -> AWS provide monitoring through Amazon CLoudwatch

=> Scaling 

   -> Vertical Scaling 

       Increase instance size , More CPU , More Ram

=> Storage Scaling 

   -> Increase storage 

      20GB -> 100GB

=> Maintenance Window 

   AWS perform 

   1. Minor version upgrade 
   2. Patches 
   3. Security updates

=> Parameters Groups 

   -> Instead of editing database configuration file directly , RDS use parameter group 


      max_connection 

      innodb_buffer_pool_size 

      query_cache_size

=> Options Group 

   -> Enable engine specific features


=> Transaction 

    -> RDS support fully ACID txn when using engine like Mysql and PostgreSQL

=> Pricing 

   -> pay for 

      1. Instance hour 
      2. Storage 
      3. IOPS 
      4. Backups beyond the free allocation 
      5. Data transfer 


=> Real World Architecture 


                    Users
                      │
                      ▼
                Load Balancer
                      │
                      ▼
                  EC2 Instances
                      │
                      ▼
             Amazon RDS (Primary)
                 /           \
                ▼             ▼
         Read Replica    Read Replica

=> Request FLow 

   Login -> RDS Primary (Read / write)

   Place order  APp -> RDS Primary (Write)

   Browse Products App -> Read Replica (Read)

   Reports / Analytics App -> Read Replica (Read)


"""