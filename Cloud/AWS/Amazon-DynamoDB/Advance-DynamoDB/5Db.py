""" 
=> Global Table 

    -> DynamoDB Global Table allow you to replicate a table automatically across multiple 
       AWS region .

       This let application read and write to the nearest region with low latency while 
       providing disaster recovery and high availability


=> Why do we need global Tables

   1. Imagine we have table worldwide

   2. without Global Tables


        Users in India
           |

        AWS mumbai region
           |
           
        Users in US
           |
        
        still connect to mumbai

     -> problem 

        1. High latency for Us users 
        2. if mumbai goes down , application unavailable 
        3. No regional failover


    3. With Global Tables

        Global Table

      +----------------------+
      |                      |
      |                      |
+-----------+          +-----------+
| Mumbai    |◄────────►| Virginia  |
| ap-south1 |          | us-east-1 |
+-----------+          +-----------+
       ▲                     ▲
       │                     │
 India Users            US Users      


    -> each region has its own DynamoDB table 

    -> Changes replicate automatically


=> Internal Architecture 

        Application

        Write Request
              │
              ▼
     DynamoDB Region A
              │
      Commit Locally
              │
              ▼
   DynamoDB Streams Record
              │
              ▼
       Replication Service
      │             │
      ▼             ▼
     Region B        Region C
      │             │
    Apply Update  Apply Update


    -> Every write is committed  locally first 

    -> Replication happens async afterwards


=> Components 

    1. Local Table 

       -> Every region has its own dynamoDB table 

       -> Mumbai table , virgina table 

    2. dynamoDB streams 

        -> every writes generates a stream event


        -> stream event is consumed by the replication system


    3. Replication Service

        -> AWS manage a replication service that reads changes from the stream and sends them 
           to other region

           we never manage this yourself

          Streams 

             |

          Replication worker 

          |               |

          Tokoyo          London


    4. Confict  Resolver 

       -> Sometime two region update the same item simultaneously 

       -> mumbai balance = 500 at the same time , virigina = 700 

           which one wins


       -> conflict resolution 

           1. Dynamodb use last write wins

           2. every write contain a timestamp


=> What is One region fails 

    1. Suppose mumbai fails

       mumbai 

       virgina 

       tokoyo

       user can contiue writing to virginan or tokyo

       when mumbai return, dynamodb synchronizes it with latest change from other region


=> When should you use Global Tables?

     -> Global applications with users in multiple continents
     -> Low-latency read and write requirements
     -> Disaster recovery across AWS Regions
     -> High availability with automatic regional failover    


=> flow 

 Client
   │
   ▼
Nearest AWS Region
   │
   ▼
Partition Leader
   │
   ▼
Write-Ahead Log (WAL)
   │
   ▼
MemTable
   │
   ▼
Acknowledgment sent to client
   │
   ▼
DynamoDB Streams
   │
   ▼
AWS Replication Service
   │
   ├────────► Replica Region 1
   ├────────► Replica Region 2
   └────────► Replica Region N
                │
                ▼
      Apply write to local partition



"""