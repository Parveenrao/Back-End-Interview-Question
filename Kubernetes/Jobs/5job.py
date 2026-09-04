""" 


=> Indexed Job In kubernetes 

    -> completion : 10
    -> Parallelism : 3


    -> if multiple pods are running, how does each pod know which piece of work belongs to it

        Thats the one reason , kubernetes support Indexed jobs


    -> completionMode : Indexed

         Now kubernetes assign each completion as index


    -> how pod get the index

        For an indexed job, kubernetes make the completion index available to the Pod, thrugh the
        env variable

    -> combine with it parallelism

        completions : 10
        parallelism : 3 
        completionMode : Indexed 

        Kubernetes needs 

        10 indexes total 
        0 1 2 3 4 5 6 7 8 9

        but upto  3 pods running simulataneously 


                   Indexed Job

completions = 10
parallelism = 3

             ↓

      ┌──────┼──────┐
      ▼      ▼      ▼
    index0  index1  index2
      │      │      │
      ▼      ▼      ▼
      ✅      ✅      ✅

      ┌──────┼──────┐
      ▼      ▼      ▼
    index3  index4  index5
      │      │      │
      ▼      ▼      ▼
      ✅      ✅      ✅

            ...

          index9
            │
            ▼
           ✅

     All indexes complete
            ↓
        Job Complete             

        
=> what if index fails

     -> imagine 7 index fails

     -> k8s does not need successfull indexes to redo their work just because 7 failed

     -> it can retry the failed index


        index 7 -> Pod -> fail -> retry index 7 -> new attempt -> success

"""