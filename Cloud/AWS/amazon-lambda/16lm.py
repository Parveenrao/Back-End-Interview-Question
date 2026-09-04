""" 

=> AWS Lambda Initialization Phase

   -> The initialization phase (INIT phase) is the period between creating the execution env and 
      calling lambda_handler() function

      
   -> INIT phase = everything lambda does to prepare function before your handler starts executing

   -> This happen only during a cold start


=> Why is the INIT Phase Needed

    -> Before code runs , lambda needs to prepare the env

       1. Power on
       2. Load operating system 

       3. Open python 

       4. Load your project 

       5. Run your project


"""