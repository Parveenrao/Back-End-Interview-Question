""" 

=> Amazon S3

   -> Amazon S3 is AWS object storage device

   -> It store file of any type and size in a highly durable , scalable and secure way


   -> We can store 

     1. Images 
     2. videos 
     3. PDFs
     4. Logs 
     5. Machine Learning datasets 
     6. backups 
     7. Static webiste 
     8. Software package 
     9. Database backup


    -> Real world example 

      Suppose we are building Instagram

      User uploads 

        1. Photos 
        2. Videos 
        3. Profile pictures
        4. Stories 

     where will these file store -> not on the EC2 instance 

     Instead User -> upload image -> Amazon s3

     database only store , user_id , profile_pic url


=> S3 Stands for 

    -> Simple storage device

    -> S3 is object storage 

    -> There are three major storage types 


       1. Block storage  -> EBS -> Store blocks 

       2. File storage  -> EFS  -> Files/Folders 

       3. Object storage -> S3  -> Objects


=> What is an object

   -> Object consist of 

      1. Data 
      2. Metadata 
      3. Unique key


      Photo.jpg

      Data:
       Actual image

      Metadata:
        Created Date
        Size
        Content-Type

      Key:
       /images/photo.jpg
  
      Unlike a traditional filesystem, S3 doesn't use real folders. 
      Everything is identified by a unique object key.

      
=> S3 Structure 

    AWS Account

       │

     Bucket

       │

     Objects



     Bucket:
      company-data

     Objects:

        employee.csv

        images/logo.png

        videos/demo.mp4

        logs/app.log

=> Bucket 

    A bucker is a container


    Bucket:
      my-images

    Contains

      cat.jpg

      dog.jpg

      lion.png

=> Bucket Naming Rules 

    1. Must be globally unique , parveen-images 

    2. if someone else already owns it

        parveen-images

    You cannot create it

=> Bucker is Regional 

   -> When creating is bucket, you choose an AWS region

       Bucket:
         company-backup

       Region:
          ap-south-1 (Mumbai)

       The bucket itself resides in that region, though AWS replicates data across 
       multiple Availability Zones within the region for durability.   

       
=> Object key 

    -> Every object has a unique key

=> Folder in S3

   -> folder dont actually exist


=> URl of an object

   -> Object can be accessed using URLs

=> Maximum object size 

    -> 5 Tb

    -> Single upload 5GB


    -> Larger than 5GB uses Multipart upload , where the file is split into parts that are 
       uploaded in parallel and then assembled by S3


=> Unlimited objects 

    -> You can store millions or billions of object in one bucket

=> S3 durability 

   -> AWS adverties 11 nines(99.99999999) durability


   -> if we store 10 million object , on average you might be expect to lose about one
      object every 10,000 years due to storage failures

"""