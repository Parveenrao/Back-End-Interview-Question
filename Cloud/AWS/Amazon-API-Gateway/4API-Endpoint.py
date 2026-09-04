""" 

=> API Endpoint 

   -> Determine where your API is exposed and how client request enter AWS network

      1. Edge optimized
      2. Regional 
      3. Private


                     Internet Users
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
 Edge-Optimized      Regional         Private
        │                │                │
   CloudFront        API Gateway      VPC Endpoint
        │                │                │
        └────────────────┼────────────────┘
                         │
                   Backend Services

                   

=> 1 Edge-Optimized Endpoint

    -> Designed for client distributed around the world

    -> AWS automatically place a Cloudfront distribution in front of our api


    User(India)

          |

  Nearest CloudFront Edge

         |

   AWS Global network 

         |
  Regional API Gateway 
         |
    Lambda EC2 / ECS 

   -> Instead of the request travelling across the public internet all the way to the API's Region
      It enter AWS's global backbone network as early as possible

    -> Advantage 

       1. Lower latency for global user 
       2. Built in cloudfront 

       3. DDOs protection through AWS edge infra

       4. No cloudfront configuration required


=> Step 2 Regional Endpoint

    -> Designed for client in same aws region as the API

    -> No managed cloudfront distribution is placed front automatically 


       User -> internet -> regional api gateway -> backend

    -> Advantage

       1. lower latency for nearby users 

       2. Simple routing 

       3. work well with our cloudfront distribution


=> Private Endpoint

   -> Accessbile only from inside an Amazon VPC

   -> API is not reachable from public endpoint

   -> Advantage 

      1. Highest netowork isloation 
      2. internet inaccessible

      3. Traffic stays within aws network 

      4. well suited for sensitive workload
      


"""