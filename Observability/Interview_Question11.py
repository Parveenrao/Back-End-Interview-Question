"""
=> Storage Ans TSDB
    
    -> How does Prometheus store data
    
        1. each data point in prometheus is stored as 
        
        <metric_name>{label1="value1", label2="value2"} value @ timestamp
        
        http_requests_total{method="GET", status="200"} 1027 @ 1714032000

----------------------------------------------------------------------------------------------

=> What is TSDB 
   
   -> Time series database specially designed to store and query time based data  that change over time
   
   -> Key concept 
      
      1. Time series
         
         unique combination of metric name + labels 
         
        http_requests_total{method="GET", status="200"}
                 
     2. High write throughput 
          
          TSDB are designed to handle , million of data point per second
          
          continous ingestion
     
     3. Compression 
         
         -> Store delta of of timestamp and values
         
         saves huge storage space

-----------------------------------------------------------------------------------------------------

=> Write Ahead log 
    
    1. Before writing data to the main database , the system first write it to a log file 
        
        that log = wal
    
    
    -> Why wal 
       
       memory if fast but volatile 
       
       data in memory -> lost 
       
       data in wal
       
       
       1. Data comes in (metrics scraped)
       2. Write data → WAL (on disk)
       3. Store data → Memory (fast access)
       4. Later → flush to permanent storage (blocks)    
       
    In Prometheus TSDB
     WAL is stored in: /data/wal
     Data is written in segments (files)
     It is continuously appended (fast writes)      
     
     
     
     Sequential writes → very fast
     Append-only → no overwrites
     Crash recovery → replay log
     Durability → prevents data loss           


---------------------------------------------------------------------------------------------------------

=> Data Retention 
    
    -> how long data is stored before it deleted 
    
     Data retention --> keep data for X time , and then remove it automatically
    
    
    -> In prometheus 
        
        Default retention = 15 days
        after 15 days = old metric are deleted 
        
        
        we can change it 
        --storage.tsdb.retention.time=30d
    
    -> Why data retention 
    
       1. storage control 
           
           if you dont delete old data 
            
            disk fill up -> system crash
       
       2. Performance
          
          lesss data = faster queries
          more data  = slower queries

------------------------------------------------------------------------------------------

=> Compaction 
    
    -> Process of merging small data blocks into larger ones and cleaning them up so storage stays efficient and queriesstay fast
    
    -> Working 
      
      1. Small blocks are created
          
          -> Prometheus write data into 2 hour block
      
      2. Background compaction start 
          
          -> A background process looks for block that can be merged
      
      3. Merge block 
          
          2h + 2h + 2h -> 6h 
          
          6h + 6h -> 12h 
          
          12h + 12h -> 24h
      
      4. Old blocks deleted
          
          -> after merging 
              
              new compacted block is kept 
              old smaller block are deleted 

----------------------------------------------------------------------------------------------

=> What happen if disk is full  
      
      1. Write start failing
         
         prometheus tries to write to 
          
          wal (write-ahead-log)
          
          new block
        
        disk is full
        
        new metric are not stored 
        
        start losing data 
      
      
      2. Wal cannot append
        
        -> Wal is append only
        -> no space => no wal
        
        
        prometheus may crash
        
        or wal is apending or drop some sample
      
      3. Scrapping continues
         
         -> Target still scrap 
         -> But data cannot be persisted 
      
      4. Compaction stop 
         
         -> compaction need space for new merge block
         -> No space = compaction fails
         
         leads to too many small blocks 
         
         worse performance
      
      5. Query performance degrade
         
         -> Fragmented blocks 
         
         -> incomplete write
      
      6. Possible Corruption  
          
          -> Partial write 
          -> Incomplete wal segment
          
          On restart 
            
            Recovery may fail 
            Data loss increase 
 
---------------------------------------------------------------------------------------------

=> How does Prometheus handle restart 
  
  1. Load Existing data block 
     
     -> Prometheus scan data block 
     -> Load all persisted block (on disk)
  
  2. Replay WAL 
      
      -> It reads wal 
      -> Replays all recent data that was
          
          written to wal
          but not yet flushed to blocks
   
   3. Rebuild Head Block
       
       -> Recent 2 hours of data is restored in memory 
       -> so queries for recent data will work
   
   4. Resume scrapping 
      
      -> Prometheus restarts scrapping target 
             
             
             
             Shutdown → Restart
                    ↓
           Load blocks from disk
                   ↓
               Replay WAL
                   ↓
          Rebuild memory (head block)
                   ↓
             Resume scraping      
 
-----------------------------------------------------------------------------------------------------------

=> Block storage   
    
    -> Storing time series data in fixed size chunk of time called "blocks" 
    
    
    -> What is block 
       
       Each block typically contains ~ 2 hour of data 
       stored as directory on disk
          
          block/
          ├── chunks/     → compressed time-series data
          ├── index       → helps find data quickly
          ├── meta.json   → metadata (time range, stats)      
    
    -> How blocks are created 
    
       1. Data is written to wal 
       2. Memory 
     
       3. After 2 hours 
         
          -> data is flushed to disk
          -> a new blocked is created 
          
          Time → →

          [10:00–12:00] → Block 1 
          [12:00–14:00] → Block 2
          [14:00–16:00] → Block 3        
    
    
    -> WHy blocks
        
        1. Faster queries 
            
            Prometheus scan only relevant blocks
             
             query last 1hour -> does not scan all data 
        
        2. Easier deletion
            
            Old blocks are simply deleted 
             
            No complex cleanup
        
        3. Eficient compaction 
           
           -> small block merged into bigger one                                                                                                             
"""