"""" 

=> OAuth2.0 

    -> Is an authorization framework that allows an application to access user's resources on
       another service without asking for the user's password.

    -> Instead of sharing credentials , the application receives an access token with limited 
       permission and a limited lifetime



=> Main Component

   1. Resouce owner = The user (you)

   2. Client = The application requesting access 

   3. Authorization server = Verifies the user and issues token (Google)

   4. Resources server = hosts the protected resources


=> FLow OF OAuth 

   -> Suppose we bulding a job portal and we want to sign using Google

   -> Instead of storing password , we let google authenticate user 



   Step 1. user click login

       -> user visit jobportal.com

       -> click login with google

       -> browser send request 

          GET/login/google


   Step 2. Backend Redirects user to Google

      -> FastAPI creates a url like

                      https://accounts.google.com/o/oauth2/v2/auth?
                      client_id=abc123
                      &redirect_uri=https://jobportal.com/auth/callback
                      &response_type=code
                      &scope=email profile
                      &state=xyz123       


        -> clientId 

           Google gave your application this ID

           Goolge nows this request come from jobportal


        -> redirect_uri

            After login google should return here 

        -> response_type = code

            Do not give me an access token yet 

            Give me a temporary authorization code 

        -> scope 

           permission

           scope = emailprofile

    Step 3  Google show login screen

    Step 4 Consent Screen

       Google ask

         Joporal wants

           Email 
           Profile

        Allow


    Step 5 Google create AUthorization code

       Google generate abcedsf

       this is not an access token

       it is only -> Authorization code 

       Usually valid for only a few minutes and can only be used once 

    Step 6 . Google redirects back

       Browser redirects to jobportal


    Step 7. Backend validate states

        backend checks 

        Received state = Stored state

        If -> yes , continue 

        else : reject request


    Step 8. Backend exchange code for Access Token

       -> now server to server communication happens

       -> browser is no longer involved 


          POST http://oauth2.googleapis.com/token

          Body

             client_id
             client_secret
             code 
             redirect_uri
             grant_type = auhtorization_code


        -> google verify

            client_id
            client_server
            authorization code
            redirect_uri
            code not expired 
            code not already used 

         if everything is valid 

         Google returns

             {
              "access_token":"eyJ....",
              "expires_in":3600,
              "refresh_token":"1//abc...",
              "id_token":"eyJhbGci...",
              "token_type":"Bearer"
            }

    Step 9 Backend store token

       Usually access token


   Step 10 Backend request user info

        GET https://www.googleapis.com/oauth2/v3/userinfo

        header   Authorization: Bearer ACCESS_TOKEN

        Google return

           {
             "email":"john@gmail.com",
             "name":"John",
             "picture":"..."
           }   


    Step 11 Create local user 

        backend check

        does this exist    

        if no:

          create user 

        if yes: 

           fetch user 

   Step 12.  Create your own session

      -> Now google finish its job

      -> app creates its own authentication

          your own jwt access token + referesh token , or

          a server side session                                                                                   

"""