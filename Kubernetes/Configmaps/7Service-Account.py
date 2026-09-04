""" 

=> Service Account

   -> A service in kubernetes is an indentity that is assigned to application (pods) not
      to human users

=> How it works
    -> Create a ServiceAccount.
    -> Grant it permissions using Role or ClusterRole and RoleBinding or ClusterRoleBinding.
    -> Attach the ServiceAccount to a Pod.
    -> Kubernetes automatically provides the pod with a token representing that ServiceAccount.
    -> The application uses the token to authenticate with the Kubernetes API.   


=> Default ServiceAccount

     -> Every namespace automatically has a default ServiceAccount.

     -> If you don't specify one:

          spec:
            serviceAccountName: default

      -> Kubernetes automatically assigns the default ServiceAccount to the pod.

      -> However, in production, it's considered a best practice to create 
         dedicated ServiceAccounts with only the permissions each application needs 
         (the principle of least privilege).       



"""