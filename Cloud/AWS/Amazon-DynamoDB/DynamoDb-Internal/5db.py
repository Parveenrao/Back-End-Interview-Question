""" 

=> Consistency In DynamoDB 

    -> Consistency is one of the most important topic , it explains why replicated database 
       sometime return  stale data 

=> What is Consistency 

   -> If i write a new data , will every future read immediately see that new value 


   -> why this is problem 

       1. Data is not stored in only one place 

       2. It is copied to multiple replica

       3. Let see what happen during a write 

         ->  suppose current value is 

         ->  name = Rahul

         ->  application updates it 

         ->  write reach to leader node 

         -> but replication take a tiny amount fof time

         -> small delay is called replication lag 

         -> it is usually millisecond , but is exist 

=> DynamoDB Provides Two Read Models

   1. Eventually Consistent Read (Default)

      Write -> Leader -> Replica Updating -> Read Happens here -> May old data

      after some millisecond , replica become consistent

      hence the name Eventually consistent

   2. Strong Consistent Read 

       -> here DynamoDB ensure you read the latest committed value


         Write -> Leader Updated -> Read -> Latest Value

         Result is always latest -> No stale data is returned


=> When Eventual consistent is fine

  1. Social media feed
  2. Product reviews 
  3. News feeds 
  4. Like counts 
  5. View counts 
  6. Analytics Dashboard



=> Python Example 


   response = table.get_item(
   
                key = {
                
                "UserId" : "U101"})

    response = table.get_item(
    
                key = {
                
                "UserId" : "U101"}, 
                
                
                ConsistentRead = True) 

        -> ConsistentRead = True , parameter tells DynamoDB to return  latest committed value                   




"""