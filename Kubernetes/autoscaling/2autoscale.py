""" 



=> HPA Algorithm

=======================================================================================

1. HPA Workload

              ┌──────────────────────┐
              │    HPA Controller    │
              └──────────┬───────────┘
                         │
                         ▼
                  Get Pod metrics
                         │
                         ▼
                Calculate utilisation
                         │
                         ▼
              Calculate desired Pods
                         │
                         ▼
             Should we actually scale?
                   │            │
                  YES           NO
                   │            │
                   ▼            ▼
            Update replicas    Wait
                   │
                   └──────┐
                          ▼
                     Repeat


                     

=> Thrashing And Flapping


     -> flaaping / thrashing means the HPA keeps scaling up and down repeadetly in a 
        short period


        minReplicas: 2
        maxReplicas: 10

        metrics:
           - resource:
              name: cpu
              target:
                 type: Utilization
                 averageUtilization: 50

     -> Target CPU = 50%

Time       CPU        HPA
---------------------------
10:00      48%        3 pods
10:01      55%        4 pods ↑
10:02      47%        3 pods ↓
10:03      58%        4 pods ↑
10:04      45%        3 pods ↓
10:05      56%        4 pods ↑         


That repeated:

3 → 4 → 3 → 4 → 3 → 4

is called flapping or thrashing.



=> Tolerance In HPA 

   -> Tolerance is a small buffer around the target metric where HPA does not scale

   -> Its main purpose is to prevent thrashind , 

   -> Suppose

       Target CPU = 50%
       Tolerance =  10%

       A 10% tolerance around a 50% target means

       Lower boundary = 50% * 0.9 = 45%

       Upper boundary = 50% * 1.1 = 55%


                No scaling
            ┌──────────────┐
────────────┼──────────────┼────────────
           45%            55%
     Scale Down          Scale Up



     CPU = 52%  → No scaling
     CPU = 48%  → No scaling
     CPU = 54%  → No scaling

     CPU = 60%  → Scale up
     CPU = 40%  → Scale down


     -> Why tolerance , imagine the target is 50%

         49% -> scale down 

         51% -> scale up 

         48% -> scale down

         52% -> scale up

         without tolerance


     -> Tolerance = dead zone around the target where HPA intentionally avoids 
        scaling to reduce unnecessary oscillation.    

=> Stabliziation window In  HPA 

   -> Do not immediatley scale based on a temporary metirc change.  Look at the 

      recommendations from the recent past before deciding

      behavior:
         scaleDown:
           stabilizationWindowSeconds: 300


   -> With a 5-minute scale-down stabilization window

         HPA considers the recommendations generated during the previous 
         5 minutes and chooses the highest recommendation for scale-down.        
"""