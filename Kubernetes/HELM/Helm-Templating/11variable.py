""" 

=> Variable In Helm 

    -> Helm lets you control your own variable inside template

    -> A helm variable start with $


    {{- $name := "backend" }}


=> creating a variable 


{{- $appName := .Values.app.name }}


values.yaml

app:
  name: payment-service

=> we can use it 
{{- $appName := .Values.app.name }}

metadata:
  name: {{ $appName }}
  labels:
    app: {{ $appName }}  




"""