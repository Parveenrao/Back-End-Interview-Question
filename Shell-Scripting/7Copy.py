""" 
=> Copy in SHell 
    
    
    -> Sytax 
       
       cp file.txt file.txt
       
       create a copy of file.txt as file2.txt
       
       if file2.txt exist , gets overwritten
    
    -> Copy into directory 
        
        cp file1.txt /home/user/docs/
    
    -> Copy directories
        
        cp -r myfolder backup/
    
    -> safe copying 
              
              cp -i file1.txt file2.txt
              
              ask before overwrite
    
    -> see what happening 
         
         cp -v file1.txt file2.txt
    
    -> cp -a project/ backup/
    
       
       copy entire project  dir into backup
        
        -a  = archive  , copy clone
        
         preseve timestamp  , links all
    
    -> Copy multi files 
      
      cp file1.txt file2.txt file3.txt folder/                               


"""