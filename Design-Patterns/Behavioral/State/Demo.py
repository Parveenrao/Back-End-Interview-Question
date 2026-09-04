""" 

=> State Design Pattern 

  -> State Design Pattern is a Behavioral Design Pattern that allows an object to change its 
     behaviour when its internal state changes.

  -> Instead of writing many if-else or switch statement to check the current state , 
     the State pattern encapsulate the behaviour of each state into its own class


   -> Why we need it 


       In Real world , object's behaviour depends on its current state

       1. A traffic light behave differently when it is Red, Yellow or Green 
  
       2. An ATM behave differently when card is inserted
        
       3. A media player behave differently when it is Playing , Paused or Stopped 

       4. An order behave differently when it is Created , Paid , shipped , Delivered 

"""


class MediaPlayer:
    def __init__(self):
        self.state = "Stopped"

    def play(self):
        if self.state == "Stopped":
            print("Playing music")  
            self.state = "Playing"

        elif self.state == "Playing":
            print("ALready playing")

        elif self.state == "Paused":
            print("Resuming music") 
            self.state = "Playing"   


             

             