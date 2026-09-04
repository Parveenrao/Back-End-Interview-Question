""" 

=> Range in helm 

    -> Range is basically a loop

    -> we use it when .Values contains a list or map and you want Helm to generate YAML
       repeadetly 


    1. Loop over a list 

        -> suppose values.yaml

        ports:

           -80
           -443
           -8080


        -> template

            ports:
                  {{- range .Values.ports }}
                  - containerPort: {{ . }}
                  {{- end }}       


                  . Here means current item


    2. Loop over list of object 

         containers:
         - name: nginx
           image: nginx:1.27
            port: 80

         - name: redis
         image: redis:7
          
           port: 6379  


    containers:
{{- range .Values.containers }}
  - name: {{ .name }}
    image: {{ .image }}
    ports:
      - containerPort: {{ .port }}
{{- end }}

=> Loop over map 


environment:
  APP_ENV: production
  LOG_LEVEL: info
  DEBUG: "false"



  env:
{{- range $key, $value := .Values.environment }}
  - name: {{ $key }}
    value: {{ $value | quote }}
{{- end }}


this generate like this

env:
  - name: APP_ENV
    value: "production"
  - name: DEBUG
    value: "false"
  - name: LOG_LEVEL
    value: "info"



"""