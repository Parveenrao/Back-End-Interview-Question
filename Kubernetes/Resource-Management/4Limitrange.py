""" 

=> LimitRange 

    -> A Limit range lets you define resource rules for container / pods inside a namespace 


    -> Resource Request/limit = Developer configure one workload 

    -> LimitRange = cluster policy workload across a namespace 


=> Problem LimitRange Solves 

    -> Suppose we have a namespace = production

    -> Developer A creates

           resources:
               requests:
                cpu: "100m"
                memory: "128Mi"

    -> Developer B creates 

       resources:
           requests:
              cpu: "8"
              memory: "16Gi"    

    -> Developer C completely forgots


    -> without policies workloads can have inconsistent resource configuration




                      
                      
apiVersion: v1
kind: LimitRange
metadata:
  name: container-limits
  namespace: production

spec:
  limits:
    - type: Container

      defaultRequest:
        cpu: "250m"
        memory: "256Mi"

      default:
        cpu: "1"
        memory: "512Mi"


=> Enfore minimum resource

apiVersion: v1
kind: LimitRange
metadata:
  name: resource-policy
spec:
  limits:
    - type: Container

      min:
        cpu: "200m"
        memory: "128Mi"

=> Enforce maximum

max:
  cpu: "2"
  memory: "2Gi"


=> Full example 


apiVersion: v1
kind: LimitRange
metadata:
  name: app-limits
  namespace: production

spec:
  limits:
    - type: Container

      min:
        cpu: "100m"
        memory: "128Mi"

      max:
        cpu: "2"
        memory: "2Gi"

      defaultRequest:
        cpu: "250m"
        memory: "256Mi"

      default:
        cpu: "1"
        memory: "1Gi"



"""