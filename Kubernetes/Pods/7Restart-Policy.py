""" 

=> Restart Policy 

    -> Restart Policy tells the kubelet whether to restart containers in a Pod 

       after they stop

    -> There are only three values

        1. Always (default)
        2. OnFailure
        3. Never 


=> 1. Always 

    -> Restart the container no matter how it exist 

    -> even program exit succesfully , keep restarting because policy is Always



=> 2. On Failure 

    -> Restart only if the process exist with a non zero exit code 


=> 3. Never 

     -> Never restart the container



=>            Exit

               │

       restartPolicy

               │

   ┌───────────┼────────────┐

Always     OnFailure      Never

Restart    Restart only   Never

Always     on Exit≠0      Restart     




"""