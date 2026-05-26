""" 
=> addFields
     
     -> $addfield is used to add new fields and modify existing fields in document
     
     -> Take current document and add extra computed field
     
     -> Input 
                 
                 {
             "_id": 1,
             "name": "John",
             "marks": [80, 90, 70]
            } 
     
     -> db.students.aggregate([
         {$addfield : {totalmarks  : {$sum : $marks}}}])
                    
                    
                    {
                  "_id": 1,
                  "name": "John",
                  "marks": [80, 90, 70],
                  "totalMarks": 240}

----------------------------------------------------------------------------------------------------------

=> facet 
    
    -> lets you run multiple independent aggregation pipeline on same input dataset -> in one go
                
     Input Data
     ↓
 ┌───────────────┬───────────────┬───────────────┐
 │ Pipeline A    │ Pipeline B    │ Pipeline C    │
 │ (count)       │ (avg)         │ (top users)   │
 └───────────────┴───────────────┴───────────────┘
     ↓
 Single combined result 
 
 
      -> Basic Syntax
             
             {
     $facet: {
       pipeline1: [ <stages> ],
       pipeline2: [ <stages> ],
       pipeline3: [ <stages> ]
     }
    }          
    
    -> All pipeline run in parallel
       
     -> Recieve same input
     
     -> They are independent 
     
     -> Output is always array

-----------------------------------------------------------------------------------------------------

=> Bucket 
    
    -> Group documents into ranges based on field values
    
    -> Put values in pre-defined ranges 
    
       0  -  50 => Fail 
       50 -  75 => Average 
       75 -  100 => Good
                  
                  
                  db.products.aggregate([
                        {
                 $bucket: {
                    groupBy: "$price",
                      boundaries: [0, 100, 500, 1000],
                      default: "Other",
                     output: {
                    count: { $sum: 1 }
                     }
                    }
                    }
                  ] )                  
"""