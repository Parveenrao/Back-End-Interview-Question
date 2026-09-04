""" 


=> ConfigMap 

    -> A Configmap is a kubernetes object used to store non-sensitive data as key-value pair

    -> central configuration files four our application


       Application Code -> Reads Configuration -> ConfigMap


    
=> Config Map Architecture
 

                 Kubernetes API Server
                       │
         +----------------------------+
         |        ConfigMap           |
         |----------------------------|
         | DB_HOST=postgres           |
         | DB_PORT=5432               |
         | LOG_LEVEL=INFO             |
         +----------------------------+
                       │
           Mounted or Injected
                       │
               +---------------+
               |     Pod       |
               +---------------+
               | Application   |
               +---------------+


               
=> Configmap Stores 

    1. Environment variables 

    2. Configuration files 

    3. Command line arguments 

    4. Application properties 

    5. JSON

    6. YMAL 

    7. TEXT files 

    8. INI files

    9. Anything that is not secret


=> What shoud not go in Configmap

   1. Password 

   2. API keys 

   3. JWT secrets 

   4. Certificates 

   5. Db password



=> Create a config map 

    1. Method 1 (YAML)

apiVersion: v1
kind: ConfigMap

metadata:
  name: app-config

data:
  DB_HOST: postgres-service
  DB_PORT: "5432"
  LOG_LEVEL: INFO    

  
=> Create 

    kubectl apply -f configmap.yaml
  
    
=> check 

   kubectl get confimag

=> Describe 

kubectl describe configmap app-config


  2. Method2 directly

     kubectl create configmap app-config \
         --from-literal=DB_HOST=postgres \
         --from-literal=DB_PORT=5432

  3. Method 3 from file 

     kubectl create configmap app-config \
--from-env-file=config.properties


    4. Method 4 Entire directory 

      config/
    nginx.conf
    app.json
    settings.ini


    kubectl create configmap app-config \
--from-file=config/


=> Example 


apiVersion: v1
kind: Pod

metadata:
  name: demo

spec:
  containers:
  - name: app
    image: nginx

    env:
    - name: DATABASE_HOST
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: DB_HOST

    - name: DATABASE_PORT
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: DB_PORT



=> Size limit 

    1 MB

    -> Do not store 

    Large videos 
    Ml models 

    ZIp files 

    Large dataaset





"""