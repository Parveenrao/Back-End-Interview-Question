""" 
=> TLS (Transport Layer Security)


----------------------------------------------------------------------------------------------------------server {
server  {
    
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /etc/ssl/certs/example.crt;
    ssl_certificate_key /etc/ssl/private/example.key;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;

    ssl_ciphers HIGH:!aNULL:!MD5;

    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:10m;
    ssl_session_tickets off;

    ssl_stapling on;
    ssl_stapling_verify on;

    resolver 8.8.8.8 8.8.4.4 valid=300s;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    location / {
        proxy_pass http://backend;
    }
}

1. listen 443 sll http2 
    
    -> 443 = HTTPS port
    -> SLl = enable secure protocol (TLS)
    -> http2 = faster (multiplexing)

2. Server name 
   -> Domain name for your server 

3. .crt -> public key
    .key -> Private key

4. ssl_protocols TLSv1.2 TLSv1.3 
    -> Modern tls protocols

5. ssl_prefer_server_ciphers on;
    
    -> server decide which cipher use , not client 
    -> Prevent weak cipher selection

6. ssl_ciphers HIGH:!aNULL:!MD5;
    
    -> allow only strong encryption 
    -> block 
       1. aNULL = no authenication
       2. MD5 = broken hashing

7.ssl_stapling on
   -> speeds up certification verification                          
    

















"""