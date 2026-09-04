""" 

=> Pause Container 

   -> A pause container is a tiny infrastrucuture container that kubernetes creates before any 
      application container 

   -> IT creates and owns the shared linux namespace for the Pod.

   -> Think of foundation of Pod.

 =>              Worker Node

                  containerd

                     │

               Pause Container

             (Owns namespaces)

                     │

      ┌──────────────┴──────────────┐

   nginx Container          Sidecar Container

      Join Namespace         Join Namespace     




"""