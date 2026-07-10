""" 

=> Control Place vs. Data Plane 



=> What is Plane 

   -> A plane is simply layer of responsibility

   -> AWS divide lambda into two major layers



                AWS Lambda

        ┌─────────────────────────┐
        │      Control Plane      │
        └─────────────────────────┘
                    │
                    ▼
        ┌─────────────────────────┐
        │       Data Plane        │
        └─────────────────────────┘


     Control Plane = Manger(takes order , manages staff)

     Data Plane = Kitchen(acutally cocks the food)


=> Control Plane 

   -> Control Plane manages lambda resources 


       1. Create a function 
       2. Delete a function 
       3. Update code 
       4. Update configuration 
       5. Publish version 
       6. Manage aliases 
       7. Attach IAM Roles 
       8. Configure triggers 
       9. Store env variables


    control plane is managment not execution


    -> Example 

        suppose you execute 

          aws lambda create-function

          request goes to 


          developer -> AWS lambda API -> Control plane -> function created 

          No code execute , only metadata is created 

    -> ANother example 

        change memory 

        128Mb -> 1024 Mb

        aws updates configuration 

        again , no function executes 


        this is control plane work



=> Data Plane 

   -> Responsible for actually running lambda function

   -> Responsibilites

       1. Receive invocation 
       2. allocate execution env 
       3. start firecracker microvm

       4. load runtime 

       5. execute handler 

       6. Return response 

       7. Scale execution 

       8. Retry failed execution



=> Why Separate them 

 
    1. Better scalability

        1 million invocations -> data plane


        10 developers -> update configurations -> control plane


       function is not blocked  by managment operations

    2. Better security 

        -> Developer may have permission 

            1. Create function 
            2. delete function 
            3. update function 


        different iam permission protect each plane         


"""