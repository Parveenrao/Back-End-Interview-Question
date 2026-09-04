""" 

=> VPA Recommendations 

   -> When VPA observer container , it does not calculate just one cpu / memory number 

   -> It produce serveral values

   Recommendation:
  Container Recommendations:
    Container Name: backend

    Lower Bound:
      Cpu:     300m
      Memory:  400Mi

    Target:
      Cpu:     600m
      Memory:  700Mi

    Upper Bound:
      Cpu:     1
      Memory:  1Gi

    Uncapped Target:
      Cpu:     800m
      Memory:  900Mi

=> 1. Target 

     -> This is the main value 

     -> VPA is essentially saying  , Based on what i have observed this is an appropriate request 
        for this container

=> 2. Lower bound

    -> Minium resonable recommendation


    lowerBound = 300m
target     = 600m
upperBound = 1000m

              Target
                 ↓
300m ├──────────600m──────────┤ 1000m
 ↑                              ↑
Lower                         Upper
Bound                         Bound


If the container's resource request falls significantly below the lower bound, VPA has stronger reason to consider it under-provisioned.


=> Upperbound 

    -> Maximum resonable recommendations


    Lower Bound = 300m
   Target      = 600m
   Upper Bound = 1000m

=> uncappedTarget — Recommendation before your policy caps


       uncappedTarget = what VPA would recommend without minAllowed/maxAllowed constraints.


"""