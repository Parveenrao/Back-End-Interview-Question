"""
 
=> NodePort

    -> A Node port Service expose your application outside the kubernetes cluster by opening 
       the same port on every worker node 


    -> Any request coming to that port is forwarded to one of the Pods behind the Services.

    -> kubernetes automatically allocates a port in the default range 30000-32767


=> how Node port work

   Pod listen on 80 

   Service listen on 80 

   Nodeport is 30080



   Browser -> 192.168.1.10 : 30000 -> Nodeport service -> ClusterIP -> Pod:80


=> YAML Example 

 
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort

  selector:
    app: nginx

  ports:
  - port: 80
    targetPort: 80
    nodePort: 30080

=> When should NodePort be used?
    -> Mainly for development, testing, on-premises clusters, 
       or simple environments. In production, LoadBalancer or Ingress 
       is generally preferred for exposing applications externally.    

 
 
"""