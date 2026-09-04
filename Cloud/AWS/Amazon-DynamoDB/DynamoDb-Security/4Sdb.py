""" 

=> Encryption In Transit In DynamoDb

   -> Encryption In Transit means that all data travelling between our application and
      DynamoDB is encrypted while it is moving across the network


   -> Unlike Encryption at Rest, which protects stored data, Encryption in 
      Transit protects data from being intercepted while it is being sent or received.  

=> Why do we need it 

   1. Imagine application send this

                           {
                    "UserId": "101",
                    "Password": "mypassword123"
                   }

                   
   2. Without Encryption 

      Application -> Plain Text -> Internet -> Hackers sniffs traffic -> Reads password

   3. with encryption 

                Application
                     │
                TLS Encryption
                     │
                     ▼
                 Internet
                     │
                Hacker Sees
                     │
              A8D92KJHF8DK...    

=> High Level Architecture

            Client Application
                    │
          HTTPS Request (TLS)
                    │
                    ▼
            Internet / Network
                    │
                    ▼
          AWS Edge / Load Balancer
                    │
            TLS Decryption
                    │
                    ▼
         DynamoDB Front-End Service
                    │
                    ▼
           Process Request

"""