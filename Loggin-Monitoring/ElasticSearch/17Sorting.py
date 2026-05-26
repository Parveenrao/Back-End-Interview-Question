"""  
=> Sorting 
    
    -> Sorting orders your result  based on field
        
        price , date, rating , keword

-----------------------------------------------------------------------------------------

1. Basic Sorting first 
     
     {
          "sort" : [
              {"price" : "asc" / "desc"}
          ]
     }        
     
  -> You cannot sort on text fields
  
       "sort": [{ "name.keyword": "asc" }]


2. Multi sorting field 

                       
                       
                       
             {
        "sort": [
     { "rating": "desc" },
     { "price": "asc" }
   ]
     }  
     
3. Missing value first 

    {
  "sort": [
    {
      "price": {
        "order": "asc",
        "missing": "_first"
      }
    }
  ]
}

4. Yoy can make fake missing vlaue 


  {
  "sort": [
    {
      "price": {
        "order": "asc",
        "missing": 0
      }
    }
  ]
}     
             
"""