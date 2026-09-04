""" 


2. Parameter Component In StorageClasses 

   -> The parameter section is a key-value map that tells the storage provisioner how to create
       the storage

       We specify 

         1. 16 GB Ram 
         2. 1 TB SSD 
         3. Intel i7

         4. Black color

    -> SImilary , when kubernetes ask the storage backend to create a volume , it sends these parameter

    -> Parameters depends on Provisioner ,

    -> different Provisioner support different parametere

3. ReclaimPolicy 

   -> What happens to underlying storage after a PVC is deleted

   -> When a PVC is deleted , what should happen to the actual storage volume

   -> Should it 

      1. keep it 
      2. Delete it 
      3. Recycle it 


    The behaviour is controlled by reclaim policy  

    -> Two possible values


        1. Delete 

           reclaimpolicy : Delete

           when the pvc is deleted , kubernetes deletes the pv and ask the storage provider 
           to delete the actual disk


           -> why use delete 

              1. Best for temporarily or easily recreated data 

                 -> cache 
                 -> CI/CD pipeline
                 -> Development enviornments
                 -> Scratch storage

        2. Retain

          -> Delete the pvc, keep the pv and underlying storage


          -> Example , we have mysql database

              Database -> 500GB

              deleting the pvc should not delete the db file

          -> when to use Retain 

              1. Mysql 
              2. Postgressql 
              3. Monogdb
              4. Elasticsearch              



"""