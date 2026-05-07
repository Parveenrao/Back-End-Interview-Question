""" 
=> Cron Tab
   
   -> Is used to schedule a commmand or script to run automatically at specific time
   
   -> Run backup every night 
   
   -> Send log every hour 
   
   -> Restart a service every hour 
   
   -> Execute a shell script every hour


=> What is Cron 
    
    1. Cron
       
       -> Background service (deamon) that  keeps running 
       
       -> Crontab => file where we write scheduled jobs

------------------------------------------------------------------------------------------------------------

-> Open crontab 
    
    crontab -e

-> Basic cron Syntax
  
  * * * * * command
  
  5 starrs represent time field
  
┌──────── minute (0 - 59)
│ ┌────── hour (0 - 23)
│ │ ┌──── day of month (1 - 31)
│ │ │ ┌── month (1 - 12)
│ │ │ │ ┌ day of week (0 - 7)
│ │ │ │ │
* * * * * command           
          

-> Every minute cron job
   * * * * * echo "Hello" > file.txt  
   

-> Every day at 2 AM

 0 2 * * * /home/user/backup.sh
 
 
-> Every 5 minutes 
 
 */5 * * *  * script.sh
 
-> Every sunday at 6 PM 
   
   0 18  * * 0 script.sh

-> Important symbol 
   
   * -> Means evey
 
-> /n Interval 
    
    */10 -> Every 10 minutes

-> Multiple values , 
 
0 9, 18 * * *  -> 9 AM and 8 PM


-> Range - 

0 9-17 * * *  -> every hour from 9 to 5    


-> View existing crontab 
   
   crontab -l

-> Remove cron tab 
    
    crontab -r
    
    delete all cron jobs          
"""
