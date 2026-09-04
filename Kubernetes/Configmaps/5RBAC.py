""" 

=> RoleBinding 

   -> A Rolebinding connect A Role To A user , Group , or service account


=>           Pod
           │
           ▼
   Service Account
           │
           ▼
     RoleBinding
           │
           ▼
         Role
           │
           ▼
 Permissions:
 GET Pods
 LIST Pods
 WATCH Pods   




"""