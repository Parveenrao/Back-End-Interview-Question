""" 


=> ExternalName 

   -> An External Name Service does not route traffic to Pods at all

   -> Instead , it maps a kubernetes service name to an external DNS using a DNS
      CName record 


=> WHy do we need it 

    -> Suppose application runs in kubernetes , but database is hosted outside the cluster 

        Application Pods 
            |

        Mysql On AWS RDS    

     instead of hardcoding

        mysql.company.com

     everywhere in your application , you can create a kubernetes Service 

       mysql

      that points to

      mysql.company.com


      now application always connnect to


=> Architecture

    without ExternalName

     Pod  -> mysql.company.com

     application = "mysql.company.com"

     if the hostname changes

     mysql-changes.company.com

     we must update every application



=> Real world Use case 

   1. AWS RDS 

   2. External Redis 

   3. Legacy Database 


"""