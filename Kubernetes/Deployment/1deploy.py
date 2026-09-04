""" 

=> Deployment 

     A deployment is a kubernetes object that  manages pod thorugh a replicaset 
     
     -> Instead of saying create one pod 

     -> we say , Always keep running  5 pods


=> Why Not Replicaset directly 

    -> Replica set cannot perform

        1. Rolling updates 
        2. Rollbacks 
        3. Version history 
        4. Deployment strategies

    -> Deployment add these features on top of Replicaset 


=> Deployment Yaml


   apiversion:  apps/v1          -> Deployment belongs to apigroup
 
   kind : Deployment             -> Create a deployment object 


   metadata:                     -> Deployment name , not pod name 

      name : nginx-deployment

   spec:
 
      replica : 3                 -> Desired number of pods

      selector:                   -> Deployment needs to know which Pods belong to me

         matchLables:


            app: nginx             -> look pods haing app : nginx
      
      template:                    -> Everything inside pod is a pod definition

          metadata:                -> Deployment copies this definition when pod creates

              lables:              -> templates.metadata.lables , every pod receive this label
                                          Pod1 = app:nginx , Pod2 = app:nignx , Pod3 = app:nginx
                 app : nginx             

         spec:                    -> template.spec = normal pod specification

            containers:

               -name: nginx

               image : nginx:latest                 

     
     
=> Creating Deployments 

    kubectl apply -f deployment.yaml

=> Check deployments

     kubectl get deployments


=> Check Replicaset 

    kubectl get rs 

=> Check pods 

    kubectl get pods 


=> Scaling  , want 10 pods 

   kubectl scale deployments nginx-deployment --replica = 10


=> Want 2 pods

   kubectl scale deployment nginx-deployment --replica = 2



=> Why Do we need deployment instead of Pods 

    1. Because deployment provide 

        -> Self-healing 

        -> Scaling 

        -> Rolling updates 

        -> Rollbacks 

        -> Declarative management

     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     """ 