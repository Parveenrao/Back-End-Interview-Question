""" 


=> Quote function In Helm 

    -> quote is an helm template function that wraps a value in double quotes

    appName: backend

    metadata:
      name: {{ .Values.appName | quote }}

      
    metadata:
       name: "backend"

"""