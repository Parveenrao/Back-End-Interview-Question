""" 


=> API Keys 

    -> An API keys is a random secret string isssued by the server that identifies the client



=>            Generate API Key
                  │
                  ▼
        +-------------------+
        |      Server       |
        +-------------------+
                  │
                  │ Give API Key
                  ▼
        +-------------------+
        |      Client       |
        +-------------------+
                  │
      Every Request includes key
                  │
                  ▼
        +-------------------+
        |      Server       |
        +-------------------+
                  │
       Lookup API Key in Database
                  │
          Valid? ───────────────┐
             │                  │
            Yes                No
             │                  │
      Process Request      Return 401    




"""