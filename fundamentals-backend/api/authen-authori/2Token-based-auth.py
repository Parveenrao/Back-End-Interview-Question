""" 

=> WHy do we need Tokens 

   1. lets compare with Session

         Browser 

           |

         Cookies : session_id = abc123
            |

         server 

            |

          look in redis

             |

          abc , user20

      The server store session data

=> Token authentication

    -> The server store nthng about the user's login session

    -> instead , after login it give the client a token
 
    
       Browser -> 34rwemn3k4jkn2jkn2j4

    -> client store it 

    -> every request include that token


=> Flow 

    1. Login 

       username + password 


    2. server verifies credentials 

    3. Instead of creating a session 

        server creates a token


   4. Response


      {
      
        access_token : "eeke"
      }        

      
    5. client store it 

       ex -> in browser memory


   6. Next request 

       -> instead of cookies

          client send 

             Authorization : Bearer eudhfd


             no session ID 

             NO redis lookup

             no redis lookup

             no session table

    7. Server 

        Receives , Bearer TOken


        It verifes

          Is the signature valid

          Has it expired

          Was it issued by me               


          

                 Login
                    │
                    ▼
            +----------------+
            |   FastAPI      |
            +----------------+
                    │
          Verify username/password
                    │
                    ▼
              +------------+
              | PostgreSQL |
              +------------+
                    │
                    ▼
          Create Signed Token
                    │
                    ▼
      Client stores access token
                    │
──────── Future Requests ────────
                    │
Authorization: Bearer <token>
                    │
                    ▼
            +----------------+
            |   FastAPI      |
            +----------------+
                    │
          Verify token signature
                    │
                    ▼
            Extract user_id
                    │
                    ▼
              Handle request          
"""