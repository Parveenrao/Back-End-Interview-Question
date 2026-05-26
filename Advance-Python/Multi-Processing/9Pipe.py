"""" 

=> Pipe 
   
    -> A pipe is an IPC mechanism used for communication betweeen processes
    
    -> One process write data 
    
    -> Another process read data
    
    -> Pipe give me communication channel between two processes
    
    -> Used for mainly
       
         1. Parent-child relationship 
         
         2. Sending message / data
         
         3.Producer - consumer data


"""

from multiprocessing import Process, Pipe


def sender(conn):
    conn.send("Hello from sender")
    conn.close()


def receiver(conn):
    message = conn.recv()
    print("Received:", message)
    conn.close()


if __name__ == "__main__":

    parent_conn, child_conn = Pipe()

    p1 = Process(target=sender, args=(child_conn,))
    p2 = Process(target=receiver, args=(parent_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
# Two way communication

from multiprocessing import Process, Pipe


def child(conn):

    conn.send("Child says hello")

    msg = conn.recv()

    print(msg)

    conn.close()


if __name__ == "__main__":

    parent_conn, child_conn = Pipe()

    p = Process(target=child, args=(child_conn,))
    p.start()

    print(parent_conn.recv())

    parent_conn.send("Parent says hi")

    p.join()    