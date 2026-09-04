""" 


=> Read Model 


     Replaying miilions of events for every request is too slow

     instead 

     event -> Projection -> Read db


     -> why projection 

       suppose one account has 50 millions events


       every api call would replay , 50 million event 

       impossible

       projection keep , 

       current balance 

       current order status

       current inventory



=> Idempotency

   -> Sometime event is delivered twice


      MoneyDeposited 

      MoneyDeposited

      Balance doubled

      each event get unique id



=> Event store requirements 


   1. An event store should provide 

      -> Append only write 

      -> Event ordering 

      -> Version control 

      -> fast sequential reads 

      -> event replay 

      -> Optimistic concurrency 

      ->  durability

      -> replication




"""