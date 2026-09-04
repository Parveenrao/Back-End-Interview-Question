""" 

=> Server Side Events 

   -> SSE is an HTTP based technology that allows the server to continuously push updates 
      to the client over a single , long lived HTTP connection



=> SSE 


   Imagine a stock market website 



   browser -> GET/events 

   Server -> Price = 100 , Price = 101 , Price = 99 , Price = 103 

           Connection stays open


    The browser open one connection and the server send update whenever something change


=> SSE is just HTTP

    HTTP Request -> Long lived response -> Server continuosuly writes data


=> Event Format

    -> Each message follows a simple text format 

        data : hello 

        blank line indicates end of event

        another event : Price updated


    -> Named events 

        Instead of default "message" event we can assign a custom event name

        event : Payment 
        Data  : order paid

    -> Event ID 

        each event can have an id 

         id : 101
         data : price updated

    -> Retry 

       Server can suggest how long the client should wait before 

         retry : 5000

         retry after 5 seconds             


"""