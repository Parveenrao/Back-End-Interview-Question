""" 

=> Instance Family 


   1. T Family (Burstable)

        t3.micro


        -> Small application

        -> Learning AWS

        -> Personal webiste 

        -> Small APIs

        -> Development 

        -> Free Tier 

        -> Characteristics

            1. Low cost 
            2. Burstable CPU 
            3. Small RAM

        -> Example 

            Wordpress Website 

              50 users/day 

              t3.micro


    2. M Family 

        m7i.large 

        -> Balance CPU and RAM

        -> Web applications 

        -> Backend APIs

        -> Enterprise apps 

        -> Medium workload

    3. C Family 

       -> High CPU

       -> Video encoding 

       -> Machine learning inference 

       -> Gaming servers 

       -> batch processing

    4. R Family 

       -> Memory Optimized 

       -> Large RAM

       -> MySql 

       -> Redis 

       -> Analytics 

       -> Postgres SQL

    5. P Family (GPU)

       -> AI Traning 

       -> Deep learning 

       -> LLMs 

       -> CUDA

       -> Pytorch 

       -> Tensorflow

    6. G Family 

       -> GPU for graphics and inference

          1. Image processing 

          2. Video streaming 

          3. ML inference 

          4. Virtual desktop

    7. I Family 

       -> Storage optimized 

       -> Fast SSD

       -> NOsql 
       -> Elasticsearch 

       -> Database

    8. D Family 

       -> Large HDD storage 

        1. Big data 
        2. Hadoop 
        3. Data warehouse                                              


  2. Processor Type 

      m7i 

      i = Intel

      i                  -> Intel Xeon

      a                  -> AMD EPYC

      g                  -> AWS gravition

   3. Instance Size 


     1. micro 
     2. small 
     3. medium 
     4. large 
     5. xlarge 
     6. 2xlarge 
     7. 4xlarge 
     8. 8xlarge 
     9. 16x large 
     10. 32x large

     Larger size provide more vCPUs , memory and networking capacity


   4. vCPU

       -> A virutal cpu is the compute resource assigned to your EC2 instance.

       -> It is based on the physical CPU core availabe on underlying AWS host 

   5. Network speed 

      -> Different instance type support different network speeds


      t3.micro -> upto 5gbps 

      c7g.16xlarger -> 25-50gbps


      high performance workloads often require higher network bandwidth                   
"""