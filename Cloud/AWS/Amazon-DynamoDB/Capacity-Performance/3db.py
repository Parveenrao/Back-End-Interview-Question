""" 

=> Brust Capacity

   -> Brust Capacity is a mechanism in DynamoDB that lets a table or partition temporarily use 

      unused throughput from the recent past to handle short traffic spike wihtout 

      immediate throttling

   -> Example 

      1. Suppose table is provisioned mode with

          1000 RCUs

          actual usuage for 5 minutes : 300 RCUs/sec

        -> Each second 

           Provisioned = 1000
           used        = 300

           unused      = 700

        -> because  we are not using all provisioned capacity. DynamoDB accumulates brust credit 

           (upto limit)

        -> Now imagine a spike

           Normal : 300 RCU/sec

           Suddenly 1500 RCU/sec

           for a short period , DynamoDB serve more than provisioned 1,000 RCUs by using
           stored brust credit 

        ->     Normal Traffic
                 |
                 v
           +----------------------+
          | Partition Capacity    |
          | 1000 RCU              |
           +----------------------+
                 |
            Only 300 RCU used
                  |
         Unused throughput tracked
                  |
         Burst reserve available
                   |
          Sudden traffic spike
                   |
            Uses reserve first
                   |
           If reserve finishes
                   |

             Throttling begins              


=> Important Characteristics

     1. Brust Capacity is temporary 
     2. Is it not additional permanent throughput 
     3. It depends on previous unused capacity 
     4. It is managed  per partition , not as one global  pool for enitre table 

     5. It help absorb short - lived spike , not sustained high traffic


=>  Does Burst Capacity increase your provisioned RCUs or WCUs?

     -> No. It only allows temporary use of previously unused throughput. 
        Your configured provisioned capacity does not change.  

=>  Does On-Demand mode use Burst Capacity?

    -> Yes, DynamoDB can absorb short traffic spikes in On-Demand mode as well. 
       However, the concept is less visible to users because AWS manages capacity 
       automatically. You still should not rely on burst behavior for sustained traffic 
       increases.           
"""