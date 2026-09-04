""" 
=> Main Component Of EC2

    
  1. Amazon Machine Image(AMI)

     -> An AMI is a template used to launch an EC2 instance 

     -> like installing windows from an ISO file 

     -> It contains 

        1. Operating system(Ubuntu , Amazon Linux ,Windows)
        2. Required software 
        3. Libraries 
        4. Configuration 
        5. Application code 

        Example Ubuntu 24.04 AMI -> Launch EC2 -> Ubuntu Server starts

        Without an AMI , an EC2 instance cannot be created 


    2. Instance Type 

       -> An EC2 Instance Type define the hardware configuration of the virtual machine that AWS creates for you 

       -> When buying a laptop , we choose 

         1. CPU(intel i5 , i7)

         2. RAM(8GB , 16GB)

         3. GPU (RTX 4060)

         4. SSD(512GB)

       -> Similary In AWS , we choose an instance type 

          1. CPU
          2. RAM 
          3. Storage 
          4. Network speed
          5. GPU

       -> why do we need Instance type 

           Different application need differnt hardware 

           1. Banking app = High CPU , High RAM
           2. AI training = GPU

           3. Database = Large RAM

        -> Naming Convention

            1. t3.micro

                t-> family 
                3-> Generation 
                micro -> size

            2.m7i.large 

               m-> family 
               7-> Generation 
               i-> Processor variant 
               large -> Size 
                                          


"""