""" 

=> Label Selector

     -> Label Selector is a way to find or select kubernetes object based on their 
         labels

     -> think of like a filter 

     -> Example , if Pods , have these labels 

        PodA 

        app = frontend 

        PodB

        app = frontend 

        PodC
        app = backend 

        Pod D

        app = mysql

    a label selector

       app = frontend

       select Pod A , PodB


       it ignore 

       Pod C
       Pod D

=> Label vs Selector 

    -> labels are attached to objects 


    -> selectors search those labels

=> ==============================================================================


=> Create three pods 


apiVersion: v1
kind: Pod

metadata:
  name: nginx2

  labels:
    app: nginx



apiVersion: v1
kind: Pod

metadata:
  name: nginx2

  labels:
    app: nginx



apiVersion: v1
kind: Pod

metadata:
  name: redis

  labels:
    app: redis




kubectl get pods -l app=nginx


=> Types of label selector 

   1. Equality-based selector (= , == , !=)

        kubectl get pods -l app=frontend


        kubectl get pods -l app=frontend , env=production

   2. Set based Selector 

       in 

       notin

       exist 

       does not exist 


       kubectl get pods -l 'app in (frondend , backend)

       kubectl get pods -l 'app notin (frontend)'     



"""