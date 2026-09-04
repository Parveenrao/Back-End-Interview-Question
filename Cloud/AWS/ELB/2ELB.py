""" 

=> How ELB works 

   

      -> user opens , www.amazon.com

      -> DNS returns elb dns name 

      -> Request reach elb 

      -> Elb check  , which server is healthy 

      -> traffic sent to healthy EC2


=> Component Of ELB


   1. Listener

      -> Wiat for incoming request 

      -> Listener contain , protocol , port , rules 

   2. Rules 

      -> Tell ELB where to send request 

      1. /image -> image server 

      2. /api -> api server 

      3. /admin -> Admin server


   3. Target Group 

      -> A target group is a collection of backend targets 

      -> can be 

        1. EC2 
        2. ECS
        3. EKS 
        4. Lambda 
        5. Ip addresses

   4. Targets

       -> Actual servers 

       EC2 , Lambda , Containers 


=> Health Check 


   1. Suppose 

      EC2-1

      EC2-2

      EC2-3

      EC2-2 crash


      elb check every second , stop sending traffic

=> Cross Zone Load balancing   

    -> all request distributed


=> SSL Termination 

   HTTPS traffic 

   CLient -> Encrypted -> ELB -> Decrypt -> EC2


   -> EC2 does less  encryption work 
   -> Centralized certificate management 
   -> Simpler application configuration

   Certificate come from AWS Certificate Manager

=> Sticky Session 

    -> Sometime user session must stay on one server 

    user -> ec2 -> next request -> ec2 -> next request -> ec2

    elb use cookies

=> IDle timeout 

  -> Suppose user stop sending data 

  -> elb waits. eg = 60 second , no activity , connection closed 

=> Connection Draining (Deregistration delay)

   1. Suppose ec2 removing 

   2. without draining , disconnected 

   3. with draining , finish exisiting request , Remove server 


=> Security Groups 

   Elb has its own security groups 

   Internet -> elb 443 allowed -> ec2 only elb security group allowed


   -> best practice is to allow your ec2 instance to accept traffic only from elb 
      security group


"""