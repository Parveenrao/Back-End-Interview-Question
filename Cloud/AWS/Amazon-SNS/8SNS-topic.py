""" 

=> Topic Encryption 

    -> when we publish a message to an sns topic , that message is stored temp inside aws before 
       it is delivered to subscriber

       how does aws protect that messsage from unauthorized access

         answer is topic encryption


=> What is Topic Encryption 

    -> SNS encrypt message while they are stored inside aws using AWS KMS

    -> without encryption 

        publisher -> sns topic -> subscriber

        message exist in plain text inside sns while being processed

    -> with encryptio n

      publisher -> sns topic -> encrypt -> encrypted message -> decrypt(internally) -> subscriber


=> Encrypted at Rest

    -> sns encryption is Encryption at Rest

       protect store data 

       sns encrypt -> message body , stored message body

=> Encrypted at transit

   -> protect moving data over the network

     publisher -> HTTPS(TLS) -> SNS

     aws use HTTP/TLS for communication

     so sns provide both 

      1. tls while moving 
      2. ksm while stored


"""