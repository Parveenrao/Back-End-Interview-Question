""" 
=> Query Based Modelling
    
    -> Design table based on queries  , not based on data relationship
    
    -> Cassandra thinking 
        
        1. List queries first
        2. Desgin table  for each query
        3. Duplicate data if needed

------------------------------------------------------------------------------------------

1. List Queries 
   
   1. Get message of chat
   2. Get chat of user
   3. Get latest message 
   
   
   these define your schema


2. Create table per query 
   
   1. Get message of chat
   
       
       create table message_by_chat(
           chat_id uuid ,
           message_id  timeuuid,
           sender_id uuid 
           text TEXT 
           
           Primary Key(chat_id , message_id)
           
           with clusterig order by(message_id desc)
       )           
       
       
       -> problem is very large partition 
       
       -> Solution , break one large partition into buckers (smaller chunks)
       
                       CREATE TABLE messages_by_chat (
                        chat_id UUID,
                        bucket TEXT,              -- e.g. "2026-04"
                        message_id TIMEUUID,
                        sender_id UUID,
                        text TEXT,
                        PRIMARY KEY ((chat_id, bucket), message_id)
                        ) WITH CLUSTERING ORDER BY (message_id DESC);
                
                
                -> Instead of 
                         chat_id = 123 → 1 million messages ❌
                  
                  (chat_id=123, bucket=2026-01) → Jan messages
                  (chat_id=123, bucket=2026-02) → Feb messages
                 (chat_id=123, bucket=2026-03) → Mar messages    
    
    
    
    2. Get chat of users
                   
                   
                   CREATE TABLE chats_by_user (
                   user_id UUID,
                   last_updated TIMEUUID,
                   chat_id UUID,
                   other_user_id UUID,
                   last_message TEXT,
                   PRIMARY KEY (user_id, last_updated)
                    ) WITH CLUSTERING ORDER BY (last_updated DESC);   
    
    
    
    3. Get latest messgae
    
                        
                        CREATE TABLE chats_by_user (
                          user_id UUID,
                          last_updated TIMEUUID,
                          chat_id UUID,
                          last_message TEXT,
                          PRIMARY KEY (user_id, last_updated)
                           ) WITH CLUSTERING ORDER BY (last_updated DESC);                                     


"""