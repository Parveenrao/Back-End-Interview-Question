""" 

=> VPA maxallowed and minallowed



   1. minallowed 

        -> Define the minimum resource VPA is allowed to recommend / apply


        resourcePolicy:
            containerPolicies:
              - containerName: "*"
                  minAllowed:
                   cpu: 200m
                   memory: 256Mi

   2. maxAllowed

        maxAllowed defines the maximum resources VPA can recommend/apply.  



=> Using both together 

resourcePolicy:
  containerPolicies:
    - containerName: "*"
      minAllowed:
        cpu: 200m
        memory: 256Mi
      maxAllowed:
        cpu: "2"
        memory: 4Gi



"""