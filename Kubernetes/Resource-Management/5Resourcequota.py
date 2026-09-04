""" 


=> ResourceQuota
 
    -> Lets you control the total amount of resource a namespace can consume

    -> Limitrange = rules for individual container/pods

    -> resourcequots = Rules for enitre namespace

    -> Suppose cluster has three namespace

       cluster -> Team -A / Team -b / Team C

       we do not want team-a consume all the cluster resource resources, we can give it quota

apiVersion: v1
kind: ResourceQuota
metadata:
  name: team-a-quota
  namespace: team-a

spec:
  hard:
    requests.cpu: "4"
    requests.memory: "8Gi"
    limits.cpu: "8"
    limits.memory: "16Gi"

    -> These numbers are combined across workload in the namespace


=> How k8s calculated it 

    hard:
  requests.cpu: "4"
  requests.memory: "8Gi"

  Pod a -> cpu = 1
  memory = 2Gi

  Pod b -> cpu = 2
  memory = 3Gi

  so both pod can admitted

  pod c = 2
  memory 1gi

  request to create the pod is rejected because it would exceed the namespace quota


=> Resource quota can also limit object counts

apiVersion: v1
kind: ResourceQuota
metadata:
  name: object-quota
  namespace: production

spec:
  hard:
    pods: "20"
    services: "10"
    secrets: "20"
    configmaps: "20"
    persistentvolumeclaims: "5"



    now production namespace have 

    pods = 20 
    services = 10 
    secrets = 10
    pvc = 5
    configmaps = 20


=> limitrange and resourcequota can work together 

                 production
                     │
          ┌──────────┴──────────┐
          │                     │
     LimitRange            ResourceQuota
          │                     │
          ↓                     ↓
  Individual container     Whole namespace

  max CPU = 2             total request = 10 CPU
  max RAM = 2Gi           total limit   = 20 CPU
                           max Pods      = 50


So LimitRange and ResourceQuota complement each other: one keeps individual 
workloads reasonable, while the other prevents the namespace as a whole from 
exceeding its budget.                           


"""