""" 
=> Behavioral Pattern 
    -> How do object communicate each other without becoming tightly coupled
    
    1. Decoupling 
       -> Objects should not directly depend on each other 
    
    2. Responsibility Distributions 
       
       -> Dont dump everything in one class 
    
    3. Flexible Behavoir     
        
        -> Behavoir should be changeable without rewriting the whole code
    
------------------------------------------------------------------------------------------------------

=> Types Of Behavior Pattern 
    
    1. Communication Pattern (Event Based Thinking)
        -> Focus on who listen and react
       
       1. Observe 
       2. Mediator 
       3. Chain of responsibility
    
    -> Something happens , multiple component reacts           
    
    2. Responsibility Delegation 
        -> Focus on who handle the request 
       
       1. Chain of responsibility 
       2. Command
    
    3. Behavior Switching
        -> Change behavior dynamically 
        
       1. Strategy 
       2. State
     
     -> Same object , different behavior
    
    4. Algorithm Control 
        -> Control Flow of execution 
        
       1. Template 
       2. Iterator                   
"""