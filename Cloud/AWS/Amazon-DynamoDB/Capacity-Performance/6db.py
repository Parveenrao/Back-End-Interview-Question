""" 

=> AutoScaling In Provisioned Mode
   
   -> Auto Scaling in Provisioned mode automatically increase or decrease the provisioned RCUs
      and WCUs based on actual usuage , helping maintain performance while reducing cost 

   -> Unlike , On-Demand mode , where DynamoDB manage capacity completely, Provisioned mode 
      still requires you define minimum and maximum capacity. Auto scaling adjust the capacity 
      with those limit

=> Why do we need auto scaling 

    1. Suppose table is configured with 

       Provisioned RCUs = 100 

       Provisioned WCUs = 100

    without auto scaling 

      100 RCUs

    At 2pm  

      Need = 300 RCUs
      Have = 100 RCUs

      Result throttling


=> with auto scaling

      1. We configure

          Minimum RCUs = 100

          Maximum RCUs = 1000

          target utilization = 70%

        Auto scaling notice that utilization is consistently above the target 

        It increase capacity 


=> Internal Architecture 

                 Client Requests
                        |
                        v
                 DynamoDB Table
                        |
            Measures consumed RCUs/WCUs
                        |
                        v
               CloudWatch Metrics
                        |
                        v
         Application Auto Scaling
                        |
         Compare with Target Utilization
                        |
        +---------------+---------------+
        |                               |
Utilization too high            Utilization too low
        |                               |
Increase RCUs/WCUs             Decrease RCUs/WCUs
        |                               |
        +---------------+---------------+
                        |
                        v
          Updated Provisioned Capacity


"""