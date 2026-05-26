""" 
=> Fan-In 
   
   -> You don't pre-compute feeds, you build the feed when user request it 
   
   -> instead of pushing post to followers 
   
   -> you pull post from followed user at read time
   
   => Store post once , combine them when user need
 
 -------------------------------------------------------------------------------------------------------
 
 => User open feed 
    
    1. Get list of users they follow
    2. Fetch posts from those users 
    3. Merge + sort (by time / ranking)
    4. Return feed


=> Flow


User open app

Fetch following list 

Fetch posts from each user 

Merge + sort 

Return feed 
    
   

"""