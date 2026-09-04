""" 

=> Values

   -> Contains the default configuration values used by our Helm templates


=> Problem values solve 

  spec:
  replicas: {{ .Values.replicaCount }}

  template:
    spec:
      containers:
        - name: backend
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"


          instead of harcodig these values in template , Helm lets us parameterize them 

   -> then put configuration in values 


   replicaCount: 3

    image:
  repository: mycompany/backend
  tag: v1       


=> Value precendence


   -> Helm can come from several places , and higher priority source override lower 
      priority ones.


"""