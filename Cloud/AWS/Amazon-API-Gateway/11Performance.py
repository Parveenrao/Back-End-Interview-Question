""" 

=> Performance In Amazon API-Gateway

   -> API Gateway itself does not have cold start 

   -> cold start usually refers to aws lambda

   -> how to reduce cold starts

      1. keep deployment package small 
      2. intialize expensive resources outside the handler 

      3. Use provisioned concurrency for latency - sensitive  APIs

      4. choose lightweight runtime when appropriate


=> Connection Reuse 

  -> Every new network connection has overhead

  -> without resue 

      req 1 -> open connection / close  req 2 -> open/close connection 

      every request tcp/tls setup

  -> with connection reuse 

      request 1 request 2 request 3 -> close

      same connection is reused


=> Compression
   -> Large response take longer to transfer

   -> api gateway can compress eligible response before sending them to client 

=> caching


=> Regional Endpoint

   -> choosing right endpoint type affect latency


=> Payload limit 

   -> large payload increase 

      1. upload time 
      2. download time 
      3. parsing time 
      4. memory usuage


=> Streaming

  -> traditional request - response

     backend -> generate entire response -> send response

     client wait until everything is ready

    -> streaming 

       backend -> chunk 1 chunk 2 chunk 3 -> client 


"""