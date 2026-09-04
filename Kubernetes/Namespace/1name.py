""" 

=> Namespace In Kubernetes 


   -> Namespace  is a way to logically divide a kubernetes cluster into multiple virutal cluster 

   -> Like in computer 

       Computer 
         |-> Movies 
         |-> Documents
         |-> Photos
         |-> Music 

    THe files all exist on the same computer , but they are organized into differenet folders 


    -> Similarily , in kubernetes 

      Cluster 
       |-> default
       |-> kube-system
       |-> dev
       |-> testing
       |-> production

    ALl resources run on same kubernetes cluster , but they are organized into different namespace

=> Why Do we need namespace

    -> Imagine company has three teams

        1. Development teams 
        2. Testing team 
        3. Production team

    -> without namespaces

        Cluster 

        Pod 1
        Pod 2
        Pod 3
        Pod 4
        Pod 5


=> Default namespace 


     kubectl get namespaces

     NAME              STATUS   AGE

        default           Active

        kube-system       Active

        kube-public       Active

        kube-node-lease   Active

        
=> 1. Default Namespace

     -> if we do not specify namespace , kubernetes

=> 2. kube-system

     contain kubernetes system component

=> 3. kube-public 

   A namespace read by all users 

=> 4. kubet-node-lease 

    store node heartbeat information


=>     


"""