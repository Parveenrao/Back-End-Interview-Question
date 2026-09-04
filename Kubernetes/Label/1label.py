""" 
=> Label 

    -> Lables is a key-value pair attached to kubernetes object 

    -> Like tags or stickers that help kubernetes identify resources 


    labels:
       app     : nginx 
       env     : production
       version : v1

       
    app -> key 

    niginx -> value


apiVersion: v1
kind: Pod

metadata:
  name: nginx-pod

  labels:
    app: nginx
    env: production

spec:
  containers:
  - name: nginx
    image: nginx   


this pod has two labels 

app and env 



=> WHy we need lables 

   -> Suppose cluster has 100 pods

   -> Some belong to frontend , backend , database and cache 

   -> how kubernetes know which pod belogs to frontend

"""

