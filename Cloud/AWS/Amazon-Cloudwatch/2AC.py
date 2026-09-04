""" 

=> Main Component Of Cloudwatch 

CloudWatch

├── Metrics
├── Logs
├── Alarms
├── Dashboards
├── Events (EventBridge)
├── Log Insights
├── Agent
├── Composite Alarms
├── Contributor Insights
├── Anomaly Detection



  1. Cloudwatch metrics

     -> A metric is simply a numerical value measured over time 

     -> Example 

         CPU utilization    = 75% 

         Network In         = 300MB 

         Network Out        = 120 MB 

         Disk Read          = 20MB/s


         Request            = 500/sec

         erros              = 10

    Every AWS serive automatically send metrics 


    -> Example 

        EC2

        CPU = 40%

        Memory = ?

        Disk Read = 20MB/s

        
    -> Common EC2 metrics

       CPU Utilization 
       NetworkIn
       NetworkOut 
       DiskReadBytes 
       DiskWriteBytes
       StatusCheckfailed

       Memory isn;t listed , why , AWS does not collect usuage by default

       To collect -> Install the cloudwatch agent

    -> Metric Resolution 

        1. Metrics are collected at different intervals

        2. Standard Resolution = Every 1 minute 

        3. High Resolution = Every 1 second


        High Resolution metrics are useful for latency-sensitive workloads but can cost more

    -> Dimensions 

       1. Dimension are labels attached to metrics 


          CPU utilization 

          InstanceID i-23456
          Region= ap-south1
          Enviornment = production

          These help filter metrics

    -> Namespaces 

        Metric are grouped into namespace 

        AWS/EC2

        AWS/S3

        AWS/RDS

        AWS/Lambda

        Custom/MyApplication

    -> Custom Metrics

       You can publish your own metrics 

       Example , My application tracks 

       1. order processed 
       2. payment Failure 
       3. Users online 
       4. Response time 
       5. video frame processed 


      We can send them to cloudwatch

      Application -> orders = 150 -> Cloudwatch                      





"""