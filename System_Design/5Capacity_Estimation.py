""" 

=> Complete Capacity Estimation Example

   
   -> Assumptions 

      1. DAU = 5 Million
      2. Request/user/day = 40

      3. Photo upload/day = 2 million 

      4. Average photo size = 3 MB 

      5. Peak factor  = 5


    step 1. Total Reques 

            5 million * 40 => 200M/day


    step 2 Average RPS 

        200 M / 86400 => 2315

    step 3 Peak RPS 

       2315 * 5 => 11575


    step 4 Read and write ratio 

       Assume 90% Read , Write = 10% 

       Read = 10,417 RPS 

       Write = 1, 158 RPS


    step 5 storage 

        2 Million * 3 => 6TB/day


    step 6 Server

      -> suppose one server handle

        1200 RPS

        11,575 / 1200 => 10 servers 

        deploy 10-12 servers                        



"""