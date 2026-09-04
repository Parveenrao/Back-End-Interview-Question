""" 

=> Startup Node 

    -> A startup Node , has my application successfully finished starting


    -> it is especially usefull for application that need significant startup time 

       Ml service model loading , legacy application 

    -> while the startup probe is running . Kubernetes does not execute liveness or
       readiness probe


startupProbe:
  httpGet:
    path: /startup
    port: 8080
  periodSeconds: 5
  failureThreshold: 30

livenessProbe:
  httpGet:
    path: /health
    port: 8080
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5



  => Once the startup probe succeeds, Kubernetes stops running it and allows 
    liveness/readiness probes to take over.          

=> startupProbe:
  httpGet:
    path: /startup
    port: 8080
  periodSeconds: 5
  failureThreshold: 30

livenessProbe:
  httpGet:
    path: /health
    port: 8080
  periodSeconds: 10
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  periodSeconds: 5
  failureThreshold: 2    


"""