""" 

=> Behviour In HPA

  -> behaviour in kubernetes controls how HPA scales up and scales down

  -> HPA decide how many replicas it wants from metrics , behaviour puts rules 
     around how quickly that change is allowed to happen


behavior:
  scaleUp:
    stabilizationWindowSeconds: 0
    policies:
      - type: Pods
        value: 4
        periodSeconds: 60

  scaleDown:
    stabilizationWindowSeconds: 300
    policies:
      - type: Percent
        value: 20
        periodSeconds: 60


-> Scaleup 

   -> controls what happen when HPA wants more pods
   scaleUp:
  policies:
    - type: Pods
      value: 4
      periodSeconds: 60

      This means HPA can increase by at most 4 pods over a 60 second period

-> scaledown 

    -> Control what happen when HPA wants fewer pods


"""