""" 


=> FastAPI Implementation

    -> How do you secure a FastAPI application from login API Access


                  User
                    │
             Login (HTTPS)
                    │
                    ▼
              FastAPI Backend
                    │
      Verify username/password
                    │
                    ▼
            PostgreSQL Database
                    │
         Password hashed (bcrypt/Argon2)
                    │
                    ▼
      Generate Access + Refresh Token
                    │
      ┌─────────────┴─────────────┐
      │                           │
Access Token                Refresh Token
(15 min)                    (7-30 days)
      │                           │
      ▼                           ▼
Protected APIs             Refresh Endpoint
      │                           │
JWT Verification        Redis DB (token id)
      │                           │
      ▼                           ▼
 RBAC Permission Check      New Access Token
      │
      ▼
 Business Logic

 

=> 1. Password Hashing 

   -> Never store password in plain text 


      from passlib.context import CryptContext

      pwd = CryptContext(schemes = ["bcrypt"])

      hashed = pwd.hash("admin")


=> 2. HTTPS

    -> Without HTTPS , anyone can read it

    -> with https  , encrypted (always read HTTPS)

=> 3. JWT Authentication

     -> User log in

         POST/login

=> 4. HTTP Bearer AUthentication

   -> FastAPI provider a helper

=> 5. JWT verification

=> 6. Current User Dependency

          -> instead of decoding 

=> 7. RBAC (Role-Based-Access Control)

=> Permission 

   -> Sometime roles are not enough


=> Refersh token

   -> when access token expire 

   -> backend verifies refersh token and issue a new token

=> Logout

   -> JWT is stateless , so we cannot delete them after issuing them

   -> A common solution is to store referesh token (or their unique id) in Redis

=> Rate limiting

    -> Prevent brute force attacks

=> Security headers 

=> Input validation

   -> Fastpi use pydantic models

=> SQL injection Prevenetion


=> CORS


=> Logging


=> Secret management
"""