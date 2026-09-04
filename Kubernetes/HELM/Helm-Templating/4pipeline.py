""" 

=> Pipeline In Helm 


    -> A pipeline means taking the output of one value / function and passing it to the 
       next function

    -> the operator is |


    -> value -> function -> function -> final result


    -> In Helm 

        {{.Values.appName | lower | quote}}


=> Result on left side of | is passed as the last arguments to the function on the 
   right            



"""