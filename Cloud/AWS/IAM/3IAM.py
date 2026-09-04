""" 

=> IAM Group

   -> An IAM Group is an collection of IAM users 

   -> Instead of assigning permission to every user individually , you assign permission to 
      the group ,then every user in the group automatically inherit those permissions

=> How Permission Flows 

   
   Policies -> Groups -> Users 

=> Multiple Groups

    -> Can one user belong to multiple  , Yes 


      Parveen --> Backend Group --> Security Group

=> Can Groups Contains Groups 

   -> Aws does not support Nested Groups

=> Can a Group exist without users 

    -> Yes , Intern group


=> Can user exist without any group 

    Yes -> Parveen

    No group membership

    We can attach policies directly to the user if needed 
         



"""