""" 

=> EBS Encryption 

    -> EBS encryption protect the data stored on an EBS volume by encrypting it using 
       strong encryption algorithm

    -> even if some gain access to physical storage, they cannot read the data without
       the encryption key

    -> AWS use AWS key Management Service (AWS KMS) to manage the encryption keys


=> Why do we need encryption 

   -> Imagine your EBS volume contains

      Employee records 
      Customer data
      Bank details 
      Passwords 
      Medical records

   -> Without encryption 

      Data -> Plain text 


   -> With encryption 

      Data -> Encrypt -> Random unreadable text 


      only someone with the correct encryption key can decrypt and read it 


=> How Encryption Works 

   Application -> EC2 instance -> Encrypted EBS volumes -> AWS KMS key

   -> when application writes data 

      1. Data is sent to EBS volume 
      2. EBS automatically encrypt it 
      3. The encrypted data is stored 
      4. When the application reads it back , EBS automatically decrypts it 


=> Can we Encrypt an existing unencrypted EBS volume

    -> We cannot enable encryption directly on an existing unecrypted volume


    Unencrypted -> Create snapshot -> Copy snapshot with encryption enabled -> Create new encrypted volume -> Attack to EC2


"""