""" 

=> Default means 

    -> Use this fallback value when the provided value is empty


    spec:
  replicas: {{ .Values.replicaCount | default 1 }}


=> Problem with default with boolean values 

 
    featureEnable : false



    -> Tempale 

       enables : {{.Values.featureEnabled | deafult true}}

       we might expect enableed : false


       but helm default consider false an an empty value , so it use fallback value


=> Zero has the same problem 

   retrycount : 0

   Template

   retries : {{.Values.retrycount | default 3}}


   heml consider 0 into empty value




"""