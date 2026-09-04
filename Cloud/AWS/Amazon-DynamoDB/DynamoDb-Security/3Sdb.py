""" 

=> Encryption At Rest In DynamoDB

   -> Means that all data stored on DynamoDb disk is encrypted automatically before being 
      written to storage. When data is read back, dynamo decrypt it backs


   -> Why Encryption at rest 

       -> Imagine in DynamoDB storage server is stolen or someone gains access to the
          physical disk

          so, thats why if someone accesses the storage media directly , they cannot read the
          contents

=> High Level Flow


                Client
                   │
                   ▼
            PutItem Request
                   │
                   ▼
        DynamoDB Front-End Router
                   │
                   ▼
          Validate Request
                   │
                   ▼
      Request Data Encryption Key
                   │
                   ▼
         AWS KMS (Key Management Service)
                   │
          Returns Data Key
                   │
                   ▼
      Encrypt Item Before Storage
                   │
                   ▼
          SSD / Storage Layer


=> Read flow


             GetItem Request
                   │
                   ▼
           Read Encrypted Data
                   │
                   ▼
        Request Decryption Key
                   │
                   ▼
              AWS KMS
                   │
                   ▼
         Decrypt in Memory
                   │
                   ▼
          Return Plain Data


=> What get Encrypted 

    1. Table data
    2. Partition keys 
    3. Sort keys 
    4. LSI
    5. GSI
    6. Streams 
    7. Backups 
    8. PITR data
    9. Exported data snapshot managed by dynamodb

=> Encryption Process

    1. Before disk write 

      Application data -> Generate data encryption key  -> encrypt item -> Store ciphertext

=> Where are the keys stored 

   -> DynamoDB does not store your master encryption key with our data

   -> Encrypted key and master key are separated

   
=> Role Of AWS KMS

   -> AWS use the KMS to manage encryption keys


   DynamoDB -> Request Encryption key -> AWS KMS -> Customer Master key (CMK/KMS key) -> Generate data encryption key



"""