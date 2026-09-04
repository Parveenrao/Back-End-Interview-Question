""" 

=> Chain Of Responsibilty 

    -> It is a Behavioral design pattern in which a request is passed through a chain of 
       handlers. 

       Each handler decide 

       1. Handle the request 
       2. Pass it to next handler in the chain 

    -> Example 

       Compnay Leave approval System 

       1. Team lead approves leaves upto 2 days 
       2. Manager approves leaves up to 5 days 
       3. Director approves longer leaves 

       When an Employee submits a leave request 

       Employee -> Team lead -> Manager -> Director 

    -> Structure 

       Request -> Handler A -> Handler B -> Handler  C

     -> Advantage 

       1. Reduce tight coupling between sender and reciever 
       2. Easy to add or remove handler 

     -> Disadvantage 

       1. Request may go unhandled if no handler can process it 
       2. Can be harder to debug             


"""