""" 

=> Readiness Probe
  
    -> A readiness probe determine , is this container ready to receive traffic right now


    -> Readiness fail -> container is not restarted

         Pod become notReady and is removed from normal service traffic



    -> Imagine deployment with three probe 

        Pod 1, Pod 2 , Pod 3

        If Pod b readiness probe start failing

        the application in Pod B can still be running. Kubernetes simply stop treating 
         it as an eligible backend for normal service traffic     




"""