""" 

=> Init Containers

    -> Imagine 

        Application  -> Connect to mysql -> Start 

    -> but when pod start 

        Application starts 

        Mysql is still starting


    -> AN init container is a special type of containers that runs before the main application
       containers

    -> It perfrom setup task and must finish successfully before kubernetes start the regular 
       containers



    -> Create Pod -> Init Container 1 -> Completed -> Init Container 2 -> Completed -> Application Container -> Running

    Main containers never start until all init containers succeed


=> Common Use 

   1. Wait for database

     Init Containers -> Check Mysql -> Database Ready -> Yes -> Application starts


   2. Download configuration

     Git repo -> Init container -> download config files -> shared volumes -> application reads config 

   3. Databse Migration 

   4. Generate certificate 

   5. Change File permission


=> Can init containers run in parallel

   -> No 


   Init 1 -> Init 2 -> Init 3




"""