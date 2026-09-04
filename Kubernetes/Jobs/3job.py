""" 

=> Backofflimit 

    -> backofflimit tells kubernetes how many failure a job can tolerate before k8s
       mark the jobs as failed

       means the job can fail / retry , but once its failure count reaches the configured 
       limit , k8s stop retrying and the job become failed




"""