""" 

=> What is S3 bucket 

    -> S3 is a logical container that store objects (files)


    AWS Account
    │
    ├── Bucket 1
    │      ├── image1.jpg
    │      ├── video.mp4
    │      └── data.csv
    │
    ├── Bucket 2
    │      ├── logs/
    │      └── backup.zip
    │
    └── Bucket 3

    -> Every object must belong to exactly one bucket


=> Bucket Setting 

   1. General configuration 

       -> Contains basic bucket information

           bucket Name 
           Region 
           Creation date
           Object ownership

           The region cannot be changed after bucket creation. To move data to another region , create 
           a new bucket and copy the object


   2. Versioning

      -> Store multiple version of the same object 

      -> Without versioning

          report.pdf -> upload again -> old file replaced 

       -> With versioning

          report.pdf -> veriosn1 , version2 , version3

          recover deleted files 
          roll back to previous version
          protect against accidental overwrites

          Enable versioning for important data 

    3. Default Encryption 

        -> Automatically encrypt every uploaded data

    4. Object lock 

       -> Prevents deletion or modification of objects for a specified time 
     
       -> Governance mode 
           Administrator with special permission can remove the lock 

       -> Compliance mode 

           Nobody can delete the object until retention period expire    
    
    5. Lifecycle Rules 

        -> Automatically move or delete object based on age 

    6. Event Notifications 

        -> Trigger action when bucket events occur 

        -> object created , object deleted , object restored 

    7. Transfer Acceleration 

       -> Uses AWS's global edge network to speed  up uploads from distant location 

    8. Server Access Logging 

       -> Records every request made to the bucket 

       -> who accessed , when , which object  , Response code 

    9. Request Metrics

       -> Number of request 

       -> Erros 

       -> Latency 

       -> Data transferred 

   10. Inventory 

      -> Generate reports listing all object 

      -> object name 

      -> Size 

      -> Encryption 

      -> Storage class 

   11. Replication 

      -> Automatically copies object to another bucket 

      -> Types 

        1. Same Region Replication (SSR)

           Mumbai bucket -> Another mumbai bucket 

        2. Cross region  bucket 

           Mumbai  -> Singapore 


   12. Static website hosting 

       -> Allow s3 host static website 

   13. Bucket policy 

     -> Define bucket level permission using JSON

   14. CORS (Cross-origin Resource Sharing)

     -> allow web application from differnet domains to access bucker resouces 

   15. Block Public access 

      -> Keep Public access enabled unless you intentionally need public access 

   16. Access point 

      -> Provide separate endpoints and permissions for different application accessing the same bucket                                                                
               


"""