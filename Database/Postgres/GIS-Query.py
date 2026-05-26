""" 
=> PostGIS 
    
    -> Postgress + Location intelligence
    
    -> It lets you store thing like 
       
       latitude , longitude , point 
    
    -> and query like 
        
        item with in 5km radius 
        neaerst radius 
        is this point inside radius

--------------------------------------------------------------------------------------------------

=> Inside postgress 
    
    CREATE EXTENSION postgis;
    
    # create table 
    
    CREATE TABLE places (
        id Serial PRIMARY KEY ,
        name TEXT ,
        location GEOGRAPHY(POINT , 4326)
    )           
    
    -> Geography = real earth distance (meters , km)
    -> 4326  = standard lat/lon system
    
    # insert data 
    
    INSERT INTO places (name, location)
    VALUES (
    'Cafe',
     ST_MakePoint(77.1025, 28.7041)::geography
    );

      
      
      # find places with in 5km 
      
      select * from places  where ST_DWithin(location ,    ST_MakePoint(77.1025, 28.7041)::geography,
       5000);
       
       
       # Index that will make very fast 
       
       CREATE INDEX idx_places_location
       ON places
       USING GIST (location); 
       
       
"""