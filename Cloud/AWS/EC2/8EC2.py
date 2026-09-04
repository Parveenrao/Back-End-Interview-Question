""" 
=> Key-Pair 

   -> A key pair is a security mechanism used to authenticate yourself when connecting to

      an EC2 instance 


   -> For Linux EC2 instance , AWS use public-key cryptography instead of password by default

      Public key -> The Lock installed on the server 

      Private key -> The only key need to unlock it 

                    Key Pair
               ┌───────────────┐
               │               │
           Public Key       Private Key (.pem)
          (Stored on EC2)   (Stored on your PC)   

          
=> Why do we need Key-pairs 

   -> Imagine AWS allowed everyone to log in with only username and password

   -> Problems 

      1. Password can be guessed 
      2. Password can be stolen 
      3. Brute-force attack are common


=> What inside in Key-Pair 

    1. Public Key

       -> Stored on EC2 instance 
       -> Safe to share 
       -> Used to verify your identity

    2. Private key 

      -> Downloaded when you create the key pair 
      -> Stored only on your computer 
      -> Never share it


=> How Authentication Works 

    Laptop -> Private Key(.pem) -> SSH connection -> EC2 instance -> Public key stored -> Yes -> login allowed 
                                                                                        -> No -> Login denied  


"""