"""

=> OIDC

   -> Open ID is an authentication protocol built on top of OAuth 2.0

      OAuth 2.0 -> "Can this app access your data" (Authorization)

      OIDC -> who are you (Authentication)


   -> Why OIDC created

       OAuth2.0 only tells an application

         This user allowed you to access their resources

         It does not prove who the user is

        -> Example 

             1. user click on login with google

             2. but how app knows 

                 UserID
                 Email
                 Name
                 Profile Picture 

             3. Oauth does not define this

             4. OIDC adds that missing identity layer 

=> OIDC

   -> Authentication 

   -> Access Token + ID token 

   -> Identity User 

   -> Identity Provider 

   -> OIDC introduce one more concept  IDENTITY Layer 


=> Token in OIDC

    -> Three token can exist 

        1. Authorization Code 

        2. Access token 

        3. ID token


=> What is ID token 

   -> An id token is a jwt token containing information about the authenticated user 

                {
  "iss": "https://accounts.google.com",
  "sub": "123456789",
  "aud": "spotify-client-id",
  "exp": 1755000000,
  "iat": 1754996400,
  "email": "parveen@gmail.com",
  "email_verified": true,
  "name": "Parveen Kumar",
  "picture": "https://..."
}


-> This is identity information 


-> Not API permission



=> OIDC flow 

User

↓

Client

↓

Google Authorization Endpoint

↓

Login

↓

Authorization Code

↓

Client Backend

↓

Token Endpoint

↓

Returns

Access Token

ID Token

Refresh Token




-> In Oauth


The real issue

The issue with OAuth is not:

"The backend doesn't receive a token."

It does.

The issue is:

"OAuth never defines that the token is proof of the user's identity."

An Access Token proves:

"Someone has permission to access a resource."

It does not standardize:

"This is definitely Alice, authenticated by Google."

OIDC adds exactly that missing guarantee by introducing the ID Token.

"""