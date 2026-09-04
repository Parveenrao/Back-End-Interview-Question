""" 

=> EmptyDir 

    -> emptyDir is a temporary volume that kubernetes creates when a Pod is assigned to a node

       1. It starts as empty (hence the name)
       2. All conatiner inside the same pod can read / write to it
       3. The data survive when container restart 
       4. The data is deleted when pod is deleted


  Pod Created
      │
      ▼
Kubernetes creates emptyDir
      │
      ▼
Containers read/write data
      │
Container crashes?
      │
      ▼
Container restarts
      │
      ▼
Data still exists
      │
Pod deleted?
      │
      ▼
emptyDir deleted forever  


=> Why was emptyDir introduced

   1. Imagine a Pod has two container

      Pod -> App container / Logger container

      The app creates log file 

      Logger read those logs and send them to elasticsearch

   2. without shared volume

       App container 

        App/logs/app.logs

       Logger container 

         App/los/app.log

       These are different filesystem , so the logger cannot se app's log


    3. with emptydir

             emptyDir
             /shared-logs
             ┌───────────┐
             │ app.log   │
             └───────────┘
             ▲         ▲
             │         │
     App Container   Logger Container      

     
=> What is Pod deleted

    pod deleted -> emptydir deleted -> all data lost 

    a new pods gets a brand new empty , emptydir 


=> Emptydir can be stored in memory

   -> by default , emptydir use the node's disk


=> Common use case 

    1. Sharing files  between containers 

    2. Temporary cache 


    3. Scratch space

       -> application that need temporary working files during processing can use emptydir 

          instead of writing into conainter filesystem


"""