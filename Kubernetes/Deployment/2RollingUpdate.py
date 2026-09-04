""" 


=> Rolling Update 

    -> A rolling update is a deployment starategy where kuberenetes gradually replaces old Pods 
       with new Pods without causing downtime


    -> Instead of stopping all old pods first , kubernetes does this 

       Old pods(v1)

       Pod1
       Pod2
       Pod3
       Pod4
       Pod5

    -> Kubernetes does 

       Delete 1 old Pod
       Create 1 new pod 

       Delete another old pod
       Create another new pod

       Delete another old pod
       Create another new pod


=> Who Performs Rolling Updates

   -> The Deployment Controller

      Deployemnt   -> Deployment Controller -> Creates new Replicaset -> Gradually scale 


=> Commands 

   
    1. Create deployment Yaml file 

    2. kubectl apply -f deployment.yaml

    3. check pods 

    4. now change 

        iamge: nginx:1.26

    5. Apply again

       kubectl apply -f deployment.yaml

    6. watch rollout live

       kubectl get pods -w

    7. check rollout status

        kubectl rollout status deployment nginx-deployment

    8. Rollout history 

         kubectl rollout history deployment nginx-deployment

    9. Rollback 

        -> if one version 2 has some bug 

               kubectl rollout undo deployment nginx-deployment


=> Rolling Update Strategy 

     -> Be default , Deployments use the RollingUpdate strategy ,

        strategy:
           type : RollingUpdate
           rollingupdate:

           maxsurge: 25%
           maxUnavailable : 25%

      -> maxsurge = maximum no. of pods that can be created above the desired replicas during update 


      -> maxunavailable 

           Maximum no of pods that can be available during update      


"""