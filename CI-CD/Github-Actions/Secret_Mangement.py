"""  
=> Secret Management In Github Actions 

      -> Its how you safely store thing like 
          1.API keys 
          2. DB password
          3. JWt secret 
          4. Docker credentials
     
     -> ${{ secrets.DB_PASSWORD }} ✅  configure this


--------------------------------------------------------------------------------------------------

=> Types of secret 
   
   1. Repository secret 
       -> For one repo
       -> most common
   
   2. Enviroment secret 
        -> used for staging and production
        -> dafer for deployment
   
   3. Organization scret 
          -> Shared across multiple repos


-----------------------------------------------------------------------------------------------------

=> Add secret 
    
    Repo --> Setting --> Secret and Varibles -> Actions --> New repo secret 
    
    add -> Db password , api_key , docker password


-----------------------------------------------------------------------------------------------------------
=> Example Docker login 

 -name : Login to docker 
  uses : docker/login-action@v3
  with:
    username : ${{secrets.DOCKER_USERNAME}}
    password : ${{secrets.DOCKER_PASSWORD}}    
                                 
"""