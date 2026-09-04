""" 

=> AWS Lambda Code Storage

   -> Code storage is the internal lambda component responsible for storing , versionig and 
      distributing your function code to execution environments

    code storage is where AWS securely store lambda deployment package or container iamge 
     before it is executed


=> Why does Lambda Need code storage

   1. when we deploy a lambda function  , code does not run immediately

   2. Instead AWS  first store it safely


   Developer -> Upload ZIP -> Lambda code storag -> Later -> Execution env -> Run code

   3. The execution env fetches the code from storage when needed


=> What can be stored 

1. ZIP Package

    -> function.zip
         |-> app.py
         |-> requirements.py
         |-> utils.py
         |-> libraries/

    maximum compressed upload size (via direct upload) is limited , and the unzipped deployment
    package also has size limit


-> Container Image 

  -> Instead of zip

  Docker Image -> Amazon ECR -> Lambda

  containers image are stored in AWS ECR and lmabda pulls the image when creating an
  executing environment

=> Development flow 

  Developer -> Upload code -> Lambda control plane -> validate code -> Stored in code storage -> Ready for invocation


=> Control Plane manage the upload and storage 

=> Data plane later retrives the code for execution


=> Internal Architecture

              Lambda

      ┌─────────────────────────┐
      │     Control Plane       │
      └──────────┬──────────────┘
                 │
        Upload Function Code
                 │
                 ▼
      ┌─────────────────────────┐
      │      Code Storage       │
      └──────────┬──────────────┘
                 │
      Invocation Occurs
                 │
                 ▼
      ┌─────────────────────────┐
      │      Data Plane         │
      └──────────┬──────────────┘
                 │
                 ▼
      Execution Environment


=> Code Versioning 

   -> every published version has its own immutable code


   Version 1 -> code A

   Version 2 -> Code B


   -> AWS keep them separate

       Code storage 
          |-> Version 1
          |-> Version 2
          |-> Version 3
          |-> Latest (Latest)


=> Security

    -> Lambda code storage is 

        1. Encrypted by AWS 
        2. Accessble only through authorized lambda operation 
        3. version controlled for published version

        4. Not directly accessible from within our function code


=> When is the code downloaded?

   -> During a cold start, when a new execution environment is created. 
      Warm execution environments reuse the code already loaded.        

"""