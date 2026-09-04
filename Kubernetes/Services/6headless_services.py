""" 

=> Headless Services 

   A Headless service is a service without cluster IP

   Normally, kubernetes , service gives you

   One stable CLusterIp

   Load balancing across pods

   Headless service return the IP addresses of the individual Pods through DNS 

   
=> Why do we need Headless Service 

   1. Suppose we have 3 database pods

      mysql-0
      mysql-1
      mysql-2

    A normal clusterIp Service hides behind one IP

    The application does not know  which pod

    But sometime we need to connect to a specific pod

    Mysql 
    Postgres 
    Cassandra
    kakfa
    elasticsearch


=> Headless Service 

Application
      |
      |
DNS
      |
+-----+-----+------+
|     |     |      |
Pod1 Pod2 Pod3



=> example 

apiVersion: v1
kind: Service

metadata:
  name: nginx-headless

spec:
  clusterIP: None                      # here cluster IP means , do not allocate clusterIp
                                         just publish Pods Ip
  selector:
    app: nginx

  ports:
    - port: 80
      targetPort: 80
 



"""