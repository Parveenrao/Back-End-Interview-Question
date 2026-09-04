""" 
=> SSTable

    -> An SStable (Sorted String Table) is immutable , sorted file stored on disk

        Sorted -> keys are stored in sorted order 

        Immutable -> Once written , never modified

    -> Think of it snapshot of memtable


=> Why it is called  "Sorted String Table"

    -> Keys are stored in sorted order 

=> Why are SStable are Immutable

    -> Imagine SStable contains

       User 1 -> ALice 

       User 2 -> Bob 

       User 3 -> charlie


       Now suppose we edit User 2 

       User 2 -> Bobby


       can we edit SStable -> No


       Instead 

       Old SStable 

       User 1 -> alice 

       User 2 -> Bob 

       User 3 -> Charlie

          + 

          Memtable 

       user 2 -> booby

       Later compaction creates a new SStable

       User 1 -> ALice 

       user 2 -> Bobby

       User 3 -> Charlie   

   



"""