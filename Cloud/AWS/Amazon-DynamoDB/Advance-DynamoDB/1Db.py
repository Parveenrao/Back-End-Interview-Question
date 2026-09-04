""" 

=> Conditional Writes 

    -> Amazon DynamoDb lets you perform a write only if a specified condition is true.
      this prevent race condition , accidental overwrites and incosistent data when 
      client access the same item concurrently 


     -> Types Of Conditional Writes

        DynamoDB supports conditions with

         1. PutItem 
         2. UpdateItem 
         3. DeleteItem 
         4. TransactionWriteItems

     -> Syntax

           table.update_item(
              Key={
                "UserId":"123"
             },

            UpdateExpression="SET Balance = Balance - :amt",

            ConditionExpression="Balance >= :amt",

            ExpressionAttributeValues={
              ":amt":500
            }
          )

=> Internal Flow 

               Client
                 │
                 ▼
           DynamoDB Router
                 │
                 ▼
           Leader Replica
                 │
                 ▼
            Locate Item
                 │
                 ▼
          Read Current Version
                 │
                 ▼
          Evaluate Condition
                 │
                 ├──────────────┐
                 │True          │False
                 ▼              ▼
               Write WAL      Return Error
                 │
                 ▼
           Update MemTable
                │
                ▼
            Replicate
                │
                ▼
             Success

        conditional check happens before , the write is committed


=> Supported Condition Functions 

    1. attribute_exist()

         attribute_exist(UserId)

         update only if item exist 

   2. attribute_not_exist()


           attribute_not_exist(UserId)

           insert only if new item

   3. attribute_type()

        attribute_type(Age , N)

        ensure type is number

   4. contains()

        contains(Tags , "AWS")

        for list and sets 

   5. begins_with()

        begins_with(Name , 'par)

        useful for strings

   6. size 

      size(name) < 20 

      limit string / list(size)

=> What happen when condition fails

    -> No data is modified 

    -> client receives = Conditioncheckfailedexpression

    -> no wal entry is written becuase the operation is rejected before the write phase

=> Is is atomic

   -> yes , the condition evaluation and write happen as one atomic operation on the target item

    
      Read  operation + write -> One Atomic operation


=> Performance Cost

   1. Even if the condition fails 

      -> DynamoDb still needs to read the current item to evalute the condition

      -> write is not performed if the condition if false 

   2. Implications 

      -> A failed condition write consume read capacity (or read resource in on-demand mode)
         because the item must be read 

      -> It does not consume write capacity for the rejected write itself


=> Advantage 

    1. Prevent Duplicate User

    2. Inventory stock management 

    3. Optimistic locking



"""