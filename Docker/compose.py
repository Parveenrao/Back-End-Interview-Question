"""   


version: "3.9"

services:

  app:                        -> Define service name , become container 
    build: .                   -> build image from docker file , current directory              
    container_name: python_app
    restart: always             -> if container crash , restart always docker
    depends_on:                   -> start redis and postgress first until they do health check
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      DATABASE_URL: postgresql://myuser:mypassword@postgres:5432/mydb
      REDIS_URL: redis://redis:6379
    ports:
      - "8000:8000"

  postgres:
    image: postgres:15
    container_name: postgres_db
    restart: always
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U myuser"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7
    container_name: redis_cache
    restart: always
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5

volumes:
  postgres_data:
  redis_data:

"""