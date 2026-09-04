""" 

=> ClusterRole And ClusterBindingRole


    -> A Role works only inside one namespace


    -> even if the user has permission in development , they cannot access production



=> Why do we need clusterRole

    -> Kubernetes resources are cluster-wide

    -> Nodes are not inside any namespace 

    -> so a normal role cannot grant permission to read nodes 


=> What is cluster Role 

   -> A cluster Role define permission at the cluster Level


   -> Example 

       Prometheus need to monitor

         1. Pods 
         2. Nodes 
         3. Services 
         4. Deployment

    across every namespace 

    Normla ROle can not work here 

    Promethus needs a cluster Role


=> apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole

metadata:
  name: node-reader

rules:
- apiGroups: [""]
  resources:
  - nodes

  verbs:
  - get
  - list
  - watch


=> Cluster Role alone does nothing , it require clusterbindingROle


ServiceAccount
        │
        ▼
ClusterRoleBinding
        │
        ▼
ClusterRole
        │
        ▼
Read Nodes
Read Namespaces
Read PVs



"""