"""    
=> CI/Cd
    -> Continuous Integration + Continuous Delivery / Deployment
  
------------------------------------------------------------------------------------------------
  
=> CI 
    -> Developers frequently merge codes -> automatically builds = test runs

=> CD (Continuous Delivery)
    -> Code always be in deployable state

=> CD (Continuous Deployment)
     -> Every successful change is automatically deployed in production
     
=> CI/CD is a process that automates building , test , deploying code to ensure faster , reliable and frequent release 

---------------------------------------------------------------------------------------------------------------------------

=> FLow 
   
   1. Source stage 
      
      Git push trigger pipeline
   
   2. Build Stage 
       
       compile code , install dependencies 
   
   3. Test Stage 
       -> Unit test
       -> Integration test
   
   4. Package stage 
       
       -> Create artifact (Docker)
   
   5. Deploy stage 
       
       -> Deploy to staging - production
       
   6. Monitor stage 
      
      -> logs , alerts , rollback                     
             
       
"""