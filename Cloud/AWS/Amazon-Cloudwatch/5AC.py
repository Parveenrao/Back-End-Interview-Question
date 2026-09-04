""" 

=> 4. CloudWatch Dashboard

       -> Dashboard provide a visual monitoring system

         CPU =    45%
         Memory = 60%

         Request = 500

         Errors = 3

         Latency = 300ms

         A devops engineer can monitor the whole system from one dashboard   


=> 5. CloudWatch Log Insight

     -> Imagine millions of logs

     -> Finding one error manually is impossible

     -> Cloudwatch logs insights lets you query logs

=> 6. CloudWatch Events / EventBridge

      -> CloudWatch can react to AWS event 

         EC2 Started -> CLoudwatch -> Lambda

=> 7. Composite Alarm

      -> Instead of one alarm

      -> we can combine multiple alarm

         CPU > 80%

         AND 

         Memory > 90%


         Reduce false alert 

=> 8. Contibutor Insights

     -> Suppose API Recieve


       User A = 100 request 

       User B = 300 request 

       User C = 500 request 

    Contributor insights identifies the top contibutors

=> 9. Anomaly Detection 

       -> Instead of fixed threshold 

          CPU > 80%


       CLoudwatch learns normal behaviour

=> CloudWatch Workflow


   Application -> Cloudwatch agent -> Metrics + Logs -> Cloudwatch -> Alarm -> SNS -> Email -> Auto scaling or lambda



         


"""