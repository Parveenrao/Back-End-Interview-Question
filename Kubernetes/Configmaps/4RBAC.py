""" 

=> RBAC

    -> Role Based Access Control is a kubernetes authorization mechanism

    -> It answer question , i know who are you , what are you allowed to do


    -> Can this pod read secrets 

    -> Can this developer create pods 

    -> Can jenkins deploye application 

    -> Can prometheus list nodes



=> FOur Main RBAC Objects

   1. Role 

      -> Role define permission within single namespace 

      -> A Role does not grant permission by itself 


apiVersion: rbac.authorization.k8s.io/v1
kind: Role

metadata:
  namespace: default
  name: pod-reader

rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]

-> Common verbs 

   1. get -> Read one object 

   2. list -> List object 

   3 watch -> Watch change 

   4. Create -> create object 

   5. update -> update object 

   6. patch -> partial object 

   7. delete -> delete object 

   8. deletecollection -> delete many 

=> Role alon does nothing   




"""