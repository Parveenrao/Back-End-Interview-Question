""" 


=> HELM 

    -> Helm is a package manager and release manager for kubernetes applications


=> WHy do we need helm 

     1. Suppose we are deploying backend application to kubernetes 


         deployment.yaml
         servive.yaml 
         configmap.ymal 
         secret.yaml 
         ingress.yaml
         hpa.yaml
         serviceaccount.yaml 

     2. Now imagine company has 

         frontent 
         backend 
         authentication 
         payment 
         notifications 
         analytics 

       And each application has configuration for 

          -> dev 
          -> staging 
          -> production



=> Helm Provide 

    1. Reusable kubernetes templates 
    2. configuration values 
    3. Application packging 
    4. Release lifecycle management

    
    -> instead of writing 

        replicas : 3 

    -> we write 

       replicas : {{.Values.replicacount}}

       then configure it separately 

       replicacount : 3

      Template = structure 
      Values = Configuration


=> What is Helm Chart

   -> A chart is a package containing the files Helm needs to deploy an application to 
      kubernetes


      myapp/
       │
       ├── Chart.yaml
       ├── values.yaml
       ├── templates/
       │   ├── deployment.yaml
       │   ├── service.yaml
       │   ├── ingress.yaml
       │   └── _helpers.tpl
       │
       └── charts/


    -> Chart 

       Package describing a kubernetes application 

    -> Chart.yaml 

       contains information about the chart 

                   apiVersion: v2
                   name: myapp
                   description: Helm chart for my application
                   version: 1.0.0
                   appVersion: "2.3.0"      

    -> values.yaml

       contains default configuration 
         replicaCount: 3

             image:
               repository: mycompany/backend
               tag: "2.3.0"

        service:
           type: ClusterIP
           port: 8080        

    -> template/deployment.yaml might contain

                     apiVersion: apps/v1
                     kind: Deployment

                     metadata:
                          name: {{ .Release.Name }}

                     spec:
                       replicas: {{ .Values.replicaCount }}

                      template:
                     spec:
                         containers:
                              - name: backend
                                image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"  

            -> Helm combines the template with the values to generate normal Kubernetes YAML.

=> Helm FLow 


             Helm Chart
                 │
        ┌────────┴────────┐
        │                 │
   templates/         values.yaml
        │                 │
        └────────┬────────┘
                 ↓
          Helm rendering
                 ↓
      Kubernetes manifests
                 ↓
          Kubernetes API
                 ↓
              Cluster


 => Chart vs. Release 

    1. Char is a reusable package 

    2. A Release is an installed instance of that chart 


=> Environment specific configuration 

    values.yaml
    values-dev.yaml
    values-staging.yaml
    values-prod.yaml                 
        



"""