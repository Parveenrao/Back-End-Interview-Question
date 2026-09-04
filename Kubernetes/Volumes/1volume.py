""" 


=> Volumes 

    -> In kubernetes volumes are a ways to provide persistent or shared storage to containers
       running inside a Pod.

    -> Why volumes needed 

        1. By default , files created inside containers are stored in container's writeable layer 
           when the container crashes or is recreated the data is lost 


        2. volume solve this problem by

            1. Persistent data beyond container restart 
            2. Sharing data between containers in the same pod
            3. Providing access to external storage ssytem      




"""