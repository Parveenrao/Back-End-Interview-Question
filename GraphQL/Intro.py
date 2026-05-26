""" 
=> GraphQL 
    
    -> It is a query language created by Meta 
    
    -> GraphQL let client control the data shape
    
    -> Core idea 
        
        1. Client can ask exactly what it needs, nothing more , nothing less
    
-------------------------------------------------------------------------------------------------------

=> Rest Vs GraphQL 

   1. RestApi 
       
       -> Server decide response structure
       
              GET /user/1
              
              {
                "id": 1,
                "name": "Parveen",
                  "email": "abc@gmail.com",
               "address": "..."
           }
        -> We need only name  , but got extra data , more bandwidth    
       
   2. Graphql 
       
       -> Client decide response structure  


----------------------------------------------------------------------------------------------

=> Strucutre of Graphql 
    
    -> Graphql has 3 parts  
    
       1. Schema (Heart of GrraphQl)
           
           Define Type + Operation 
       
       
        type User {
         id: ID!
         name: String!
         age: Int
         }

        type Query {
         getUser(id: ID!): User
       }

        type Mutation {
         createUser(name: String!, age: Int): User
        }  
       
       2. Query Structure 
          
          -> Client decide what field it want
       
       3. Mutation 
          
          -> For create ,write , delete
       
       4. Resolver 
           
           -> Fetch data       
"""