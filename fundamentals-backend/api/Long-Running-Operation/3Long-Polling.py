""" 

=> Long-Polling 

    -> Is a communication technique where 

       1. client send a request 
       2. Server does not respond immediately if there is no new data 

       3. Instead the server keep connection open 

       4. As soon as the data become available (or timeout occur) , server sends the response 

       5. Client immediately sends another request 

    It is called long polling because The hTTP request stays open for a long time

=> Normal Polling 

   -> Client ask every 5 seconds 

   -> too many unnecessary request 

   -> Wastes bandwidth

   -> Delays depend on polling interval


=> Long Polling 

    Client --> Any new message 

    (server waits .....)

    (server waits .....)

    (server waits .....)

    New message arrives 

    Server --> Here is the message 

    Client -> Any new message 




"""