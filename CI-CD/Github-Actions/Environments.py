""" 
=> Enviroments
     
     -> Controlled stage of deployments
          
          dev -> staging -> production
          
          each enviroment has its own secrets , protection rules , approval gates 

-------------------------------------------------------------------------------------------------------
=> Why environments exists 
     
     1. Without Environment 
        
        push code -> deploy to production immediately (dangerous)
        
    
    2. With environments 
        
        Push -> test -> staging -> approval -> production 

-----------------------------------------------------------------------------------------------------

1. Create Enviroment   
     
     Repo -> Setting -> Environments -> Set New Environment
     
     Create 
       
       1. Staging 
       2. prouduction

-----------------------------------------------------------------------------------------------------

=> Use in Github actions 
    
jobs:
  deploy:
     runs-on: Ubuntu-latest
     
     environment : production 
     
     steps: 
        
        -name : deploy app
         run : eacho "Deploying"

-> This job is tied to environment

-----------------------------------------------------------------------------------------------------------

=> Protection Rule 

jobs:
  test:
    runs-on : ubuntu-latest
    
  deploy-staging:
    runs-on: unbuntu-latest
    needs : test  
    environment : staging
  
  deploy-production:
    runs-on : unbuntu-latest
    needs : deploy-staging
    environment : production 


                                      
"""