""" 

=> LSI (Local Secondary Index)

    -> LSI allow you to query the same partition key but with a different sort key

    -> i want another way to sort items that belong to the same user 


    -> Imagine this table 

          Suppose we have a Posts table.

          Primary Key

          Partition Key :       UserId
          Sort Key      :       PostId


           UserId	PostId	    Likes	          CreatedAt
              U1	P101	     20	                 Jan 1
              U1	P102	     150	             Jan 5
              U1	P103	     50	                 Jan 10
              U2	P201	     300	             Jan 2
              U2	P202	     10	                 Jan 8

    -> How this stored 

       1. Inside partition U1

           p101
           p101
           p103

        becuase the sort key is PostId

        so when we query 

           UserId = U1

           we get  p101 , p102, p103

    -> Problem 

         1. Suppose your application ask

             Show all post of U1 sorted by likes

             No , becuase table is sorted by PostId 

    To sort like this , DynamoDB  would need to read every item and sort them , which it does 

    not do efficiently



=> Solution , LSI

   -> Create an LSI

      Partition Key : UserId 

      Sort Key      : Likes


      partition key is still userid , and sort is chaged 

      this is exactly what an lsi is


=> Key rule to remember

           LSI = Same Partition Key + Different Sort Key      


"""