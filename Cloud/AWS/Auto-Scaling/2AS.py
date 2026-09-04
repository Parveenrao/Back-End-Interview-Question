""" 

=> Component Of Auto Scaling 

   1. Launch Template 

      -> Think of it as a blueprint 

      -> When AWS creates a new EC2 instance , it needs to know 

         1. Which AMI
         2. Instance type 
         3. Security group 
         4. Key pair 
         5. IAM Role 
         6. User data
         7. EBS volume 
         8. Network setting

       -> ALl of this stored inside the launch template

    2. Auto-Scaling Groups

       -> This is the heart of Auto-scaling

       -> It manage a group of EC2 instance 


           Auto Scaling Group 

            Minimum  = 2
            Desired  = 4

            Maximum  = 10

    3. Scaling Policies 

       -> Scaling policy tells AWS when to add or remove instance 


       1. Manual Scaling 

          -> Manually change the desired capacity 

             Desired = 4

             Desired = 7

             AWS launch 3 more instance 

       2. Dynamic Scaling 

          -> Based on cloudwatch metrics 

             CPU > 70%

             Launch 2 instance 


             CPU < 30% 

             terminate 2 instance 

        3. Target Tracking Scaling 

           -> you specify a target metrics 


           maintain cpu = 50%


           AWS automatically adjust capacity to keep CPU utilization around that target.
           aws recommend target tracking for common metrics like average CPU utilization 
           or request count per target 


    4. Step  Scaling 

       -> Scale by different amounts depending on how large the metric  breach is 


          CPU > 60%

          +2 instance 


          CPU > 75% 

          +4 instance 

          CPU > 90%

          +8 instance

    5. Scheduled Scaling 

        -> Usefull when traffic is predictable 

        Every day 9 AM

        Launch 10 server 

        11 PM

        terminate extra server 

    6. Predictive Scaling 

       -> AWS analyzes historical traffic patterns and predict future demand

       -> Example

           Every friday evening

           Traffic usually spike

           AWS launches instance before traffic increase using forecasting 


=> Health Check

   -> Auto scaling continuously monitor instance 


      Desired = 4

      Running

      EC2-1
      EC2-2
      EC2-3
      EC2-4

      suppose EC2-2 crash

      auto scaling detect it

      terminate ec2-2 and launch ec2-5


      desired capacity stays at 4

      
=> Multi-AZ Auto Scaling

     -> Suppose our application runs in two Availability zones

        if AZ-1 fails

        auto scaling launches new instances 

=> Lifecycle of an Auto Scaling Instance 

    Launch Template -> Auto scaling launches EC2 -> Instance boots -> Health check -> Registered with ALB

    -> Recieve traffic -> Scale In -> Deregistered from ALB -> terminate


"""