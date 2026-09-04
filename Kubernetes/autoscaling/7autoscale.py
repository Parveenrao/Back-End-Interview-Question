""" 

=> VPA Update Modes 

    -> VPA can recommend resources, apply them only when POd start or actively resize Pod 

    -> Behaviour is controlled by updateMode


    1. off -> Recommendation only 

       VPA watches resources usuage and calculates recommendations , but does not 
        modify pods 

        Pod:
        CPU request    = 200m
        Memory request = 256Mi

        VPA observes usage...

        Recommendation:
        CPU    = 600m
        Memory = 512Mi

        Pod remains:
        CPU    = 200m
        Memory = 256Mi

        this is useful when you're introducing VPA and want to see what it recommends before allowing automatic

        updatePolicy:
          updateMode: "Off"

          Off = Observe + Recommend, don't apply.

    2. Initial -> Apply when pods starts 

        VPA calculates recommendations and applies them when new Pods are created

        Current Pod
          CPU    = 200m
          Memory = 256Mi

          VPA recommends
          CPU    = 600m
          Memory = 512Mi      

          The existing Pod continues unchanged.

          Later, when a new Pod is created:

            New Pod
               ↓
          Admission Controller
               ↓
          VPA recommendation
               ↓
         CPU    = 600m
          Memory = 512Mi


          inital = Apply recommendation  only at pod creation

    3. Recreate  -> Replace Pod when needed 

       Vpa can actively updat existing pods      



"""