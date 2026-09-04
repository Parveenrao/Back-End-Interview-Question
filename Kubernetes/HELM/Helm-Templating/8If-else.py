""" 

=> If-Else In Python 


    -> Used when you want Helm to conditionally generate YAML


    -> example 


      {{ if eq .Values.environment "production" }}
        replicas: 5
        {{ else }}
        replicas: 1
         {{ end }}

         
=> Mulitple 

{{ if eq .Values.environment "production" }}
replicas: 5

{{ else if eq .Values.environment "staging" }}
replicas: 3

{{ else }}
replicas: 1

{{ end }}


=> Comparison function 

eq    equal
ne    not equal
lt    less than
le    less than or equal
gt    greater than
ge    greater than or equal


{{ if gt .Values.replicaCount 3 }}
highAvailability: true
{{ else }}
highAvailability: false
{{ end }}


=> and or not 

{{ if and .Values.service.enabled .Values.monitoring.enabled }} -> both must be true 


{{ if or .Values.dev.enabled .Values.test.enabled }} => at least one must be true 


{{ if not .Values.production }} -> Runs when .Values.production is false/empty


=> helm if treat these value as false 

false
0
""
nil
[]
{}


"""