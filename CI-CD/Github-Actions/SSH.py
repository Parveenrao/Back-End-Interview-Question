""" 
=> SSH (Secure Shell) 
    
    -> A secure way to connect with remote server and run commands 
    
    -> In Githuh action 
        
        Connect to your server → run deployment commands

---------------------------------------------------------------------------------------

- name: Deploy to server
  uses: appleboy/ssh-action@v1
  with:
    host: ${{ secrets.SERVER_IP }}
    username: ${{ secrets.SERVER_USER }}
    key: ${{ secrets.SSH_KEY }}
    script: |
      docker pull myapp:latest
      docker restart myapp        
        


-> Takes your server details
-> Uses SSH key
-> Connects to your server
-> Runs commands you provide
"""