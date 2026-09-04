""" 

=> Cross-Account SNS Topic

   -> cross account SNS allows AWS Account A to securely communicate with AWS Account B using the same 
      sns topic

    -> instead of creating separate topic in every AWS account , one account owns the topic 
       while other accounts can publish it , subscribe to it or both

=> WHy do we need Cross-Account SNS

   Imagine an e-commerce company

   AWS organization

    Account A -> Order Service 

    Account B -> Payment service 

    Account C -> Shipping Service 

    Account D -> Analytics 

    Account E -> Notifications

    Order service created one sns topic -> Order Event Topic

    when order is updated

    each service receives the event



"""