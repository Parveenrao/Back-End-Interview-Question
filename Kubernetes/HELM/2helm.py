""" 

=> Helm Chart

    
    -> A helm chart is a package containing everything Helm needs to generate and deploy
       the kubernetes resources for an application


=> Basic Chart structure 


backend/
├── Chart.yaml
├── values.yaml
├── charts/
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── hpa.yaml
│   ├── serviceaccount.yaml
│   ├── _helpers.tpl
│   └── tests/
└── .helmignore


=> Chart.yaml 

   -> Indentity of the chart

   -> it contains metadata about the package


apiVersion: v2
name: backend
description: Helm chart for backend API
type: application

version: 1.0.0             -> version of our chart
appVersion: "2.5.0"        -> version of our application


=> values.yaml 

   -> configuration 

   -> This contain default values that template can use 

replicaCount: 3

image:
  repository: mycompany/backend
  tag: "v2.5.0"

service:
  type: ClusterIP
  port: 8080


=> templates 

    -> This container kubernetes yaml with helm template expression

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



Chart = Kubernetes templates + configuration + metadata packaged as one reusable application deployment.          

"""