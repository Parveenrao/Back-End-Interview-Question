""" 

=> Secret Updation And Rotation 

   -> Updating a secret means changing its value (for example , new database password)

   -> Rotating means periodically replacing a secret to imporve security

=> Why Rotate secrets 

   1. SUppose database password has been used for two years 

       -> Password leaked 
       -> Employee left the company 
       -> Api key comprised 
       -> Certificate expired 

       -> Security policy require regular change 


=> Creating a secret 

kubectl create secret generic db-secret \
--from-literal=username=admin \
--from-literal=password=admin123


=> Verify 

kubectl create secret generic db-secret \
--from-literal=username=admin \
--from-literal=password=admin123

=> Update it 

kubectl create secret generic db-secret \
--from-literal=username=admin \
--from-literal=password=NewPassword \
--dry-run=client -o yaml | kubectl apply -f -



"""