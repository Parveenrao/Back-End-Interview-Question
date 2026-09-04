""" 


=> with 

    -> with is a Helm control structure mainly used to change the current context (.)

       temporarily 


    -> example 

    database:
      host: localhost
      port: 5432
      username: admin   

    -> without with 

    data:
      host: {{ .Values.database.host }}
      port: {{ .Values.database.port }}
      username: {{ .Values.database.username }}  

    -> with 

             data:
             {{- with .Values.database }}
             host: {{ .host }}
             port: {{ .port }}
             username: {{ .username }}
             {{- end }}  


"""