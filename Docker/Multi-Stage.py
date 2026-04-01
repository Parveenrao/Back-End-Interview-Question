""" Mutil stage image build 

# stage 1 Build dependencies 
   
   FROM python:3.11  as builder 
   
   WORKDIR /app
   
   copy requirements.txt .
   
   RUN pip install --user -r requirements.txt 
   
# stage 2 

  # Stage 2 → runtime
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local

COPY . .

ENV PATH=/root/.local/bin:$PATH

CMD ["python", "app.py"]   

"""