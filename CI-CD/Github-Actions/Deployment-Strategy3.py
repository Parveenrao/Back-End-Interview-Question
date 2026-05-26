"""   
=> Blue Green Deployment 
    
    -> Blue = current live version 
    -> Green = new version (just deployed it)
    
  -> Both environments are identical copies of your app (same DB , infra , configs locally)


-------------------------------------------------------------------------------------------------------

=> Working 
   
   1. Your app is running on Blue (Live)
   2. You deploye code to Green
   3. You teset Green
   4. When ready swtich traffic 
   
     Now Green live 
     Blue become backup     



"""