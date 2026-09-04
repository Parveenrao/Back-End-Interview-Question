""" 


=> Pod Sandbox

    -> A pod sandbox is the environment created by the conatainer runtimm that provide

       the shared infrastrucutre for all containers in a Pod

    -> Before kubernetes start application containers , it starts pod sandbox


=> Why do we need Pod sandbox 


   -> Imagine u have to pod with two containers


   -> These containers need to share 

      1. Network 

      2. IPC namesapce 

      3. Volumes 

      4. Other linux namespace


      5. If kubernetes simply started two independent containers , they would each have

         1. Different Ip address
         2. Different network namespace 
         3. Different localhost 

     6. SO kuberenetes first create shared env



         Shared env is called Pod Sandbox    


"""