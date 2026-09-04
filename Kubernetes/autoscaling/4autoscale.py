""" 

=> Policies 

   -> policies define how fast HPA is allowed to change the number of replicas

   policies:
  - type: Pods
    value: 4
    periodSeconds: 60

  - type: Percent
    value: 50
    periodSeconds: 60

-> Pod 

   This sets an absolute number of pods that may be added or removed during specified
   period

   scaleUp:
  policies:
    - type: Pods
      value: 4
      periodSeconds: 60

      HPA can add at most 4 pods over 60 second period


-> type - Percent 

    This limit scaling relative to the current number of replicas

    scaleUp:
  policies:
    - type: Percent
      value: 50
      periodSeconds: 60

      Meaning HPA can increase the replica count by at most 50% over 60 second period

      current = 10 

      desired  = 30 

      50% of 10 = 5

      10 -> 15 , 5


-> periodsecond


    periodsecond:60

    define the time period over which kubernetes enforce that scaling limit

    type: Pods
    value: 4
    periodSeconds: 60

    not more than 4 pods can be added over a 60 second period



=> what if we have both policies

scaleUp:
  policies:
    - type: Pods
      value: 4
      periodSeconds: 60

    - type: Percent
      value: 50
      periodSeconds: 60

Current = 10 pods
Desired = 30 pods

pod polic allows 

  10 -> 14

percent policy allows 

10 -> 15 = 5

so which one HPA use 

Thats where selectPolicy comes in

selectPolicy : max

with max, it choose the policy that permit the largest replica change 


selectpolicy : Min 

this it choose the policy allowing the smallest change 
"""