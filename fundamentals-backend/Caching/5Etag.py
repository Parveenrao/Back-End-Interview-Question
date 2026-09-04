""" 

=> Etag (Entity Tag)

    -> Is a unique indentifier for a specific version of a resources 


    -> instead of asking give me the whole response again 

       browser ask

          Has this response changes since the last time i saw it ??

          if the answer is no , server replies , 304 not modified 



-> How Etag is generated

   1. hash(most common)

      Hash the response body   SHA256(response)


=> Cache-control and etag used together      




"""