""" 
=> Flush 
   
   -> Flush writes in memory data to disk  and reset the translog 

=> Why flush needed 
    
    -> Transaction log increases 
    -> Recovery become slow 
    -> Disk usage increase 

=> Lifecycle 


1. Index request
   ↓
2. In-memory buffer
   ↓
3. Translog (safety) ✅
   ↓
4. Refresh (searchable) 👀
   ↓
5. Flush (permanent + cleanup) 💾
   ↓
6. Merge (optimization) 🔧


=> When flush happen 
 
 1.Translog size threshold 
      "index.translog.flush_threshold_size": "512mb"
      
      if too bug -> flush 

=> Full Flow


WRITE PATH:

Index →
  Translog (safety)
  Buffer

Refresh →
  Segment created (searchable)

Flush →
  Segment committed + Translog cleared

Merge →
  Segments optimized             

"""