""" 
=> Docker File 

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

--------------------------------------------------------------------------------------------------

=> Github Action File 

name : Docker CI/CD

on:
  push:
    branches : ["main"]

jobs:
  build-and-push:
    runs-on : ubuntu-latest
    
    steps:
     
     # 1 Get code
     
       -name : Checkout 
        uses : actions/checkout@v4
     
     # 2 Docker builder 
        
        -name : Setup Buildx
         uses : docker/setup-buildx-action@v3
     
     # Login to Docker Hub 
       
       -name : Login To DockerHub
        uses : docker/login-action@v3
        with:
           username : ${{secrets.DOCKER_USERNAME}}
           password : ${{secrets.DOCKER_PASSWORD}}     
     
      # 4. Build & push image
        - name: Build and Push
          run: |
           docker build -t ${{ secrets.DOCKER_USERNAME }}/myapp:latest .
           docker push ${{ secrets.DOCKER_USERNAME }}/myapp:latest   
       
        # 5. Optional: test container
           - name: Run container
                run: |
                  docker run -d -p 8000:8000 ${{ secrets.DOCKER_USERNAME }}/myapp:latest
                   sleep 5
                   curl -f http://localhost:8000 || exit 1   
                   

-------------------------------------------------------------------------------------------------

=> Workflow 
      
   1. Code pushed to GitHub
   2. Actions runner starts
   3. Logs into Docker Hub using secrets 🔐
   4. Builds Docker image
   5. Pushes image to Docker Hub
   6. Runs container → checks if app works

->  If anything fails → pipeline stops




























































"""