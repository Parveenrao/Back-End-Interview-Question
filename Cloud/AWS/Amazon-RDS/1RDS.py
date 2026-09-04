""" 

=> Amazon RDS (Relational Database Service)

 
    -> Amazon RDS is a fully managed relational database service provided by AWS.

    -> Instead of Installing and maintaining database on your own server. AWS manage the infra ,
       while we focus on application 

    -> Without RDS = Buy A server ,  install  a database , configure backups , monitor health ,
       update software and handle failure 

    -> With RDS = AWS does all that . Simply connect database and connect our application


=> Why Was RDS Created 

   1. Imagine we build an e-commerce application 

      we need database to store

      1. Users 
      2. Orders 
      3. Products 
      4. Payments 

   2. Without RDS 

      1. Install Mysql 
      2. Configure storage 
      3. Configure networking 
      4. Create backups 
      5. Monitor CPU 
      6. Upgrade version 
      7. Replace failed hardware 
      8. Set up Replication 
      9. Configure security

    AWS created RDS so developers don't have to manage db servers


=> what Does RDS manage 

    -> AWS automatically manage 

        1. Server provisioning 
        2. Database installing 
        3. OS patching 
        4. Automatic backups 
        5. Monitoring
        6. Failover 
        7. Replication 
        8. Storage management 
        9. Hardware replacement 

    -> You only manage 

        1. Database schema 
        2. Tables 
        3. Queries 
        4. Users
        5. Data

=> Supported Database Engine 

   -> RDS support multiple relational database

      1. Mysql 
      2. Postgres 
      3. MariaDB 
      4. Oracle 
      5. Microsoft sql server 
      6. Amazon Aurora


=> RDS Architecture 


                  Client

                   │

         Backend Application

                   │

           Endpoint (DNS Name)

                   │

            Amazon RDS Instance

      ----------------------------
      CPU
      RAM
      Database Engine
      Storage (EBS)
      Operating System
      ----------------------------

                   │

              Stored Data



"""