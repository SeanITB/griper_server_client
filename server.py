import socket
import time

HOST = "0.0.0.0" # The remote host
PORT = 12345 # The same port as used by the server
print ("Starting Program")

keepGoing = True


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT)) # Bind to the port
s.listen(5) # Now wait for client connection.
c, addr = s.accept() # Establish connection with client. https://docs.python.org/3/library/socket.html#socket-objects

try:
     actual_state = [0, 42]
     output = bytes(actual_state)  # Example data
     c.send(output)  # Send raw bytes
     actual_state =  list(output)
     print("Send =",actual_state)
     time.sleep(0.2)  # Wait 1 second

     # Receive
     actual_state = list(c.recv(32))
     print("Received Raw =", actual_state)

     while keepGoing:
         # Ensure we have at least two elements before modifying
         if len(actual_state) > 31:
            if(actual_state[0] == 0):
                print("STOP!")
            elif(actual_state[0] == 1):
                actual_state[1] += 1  # Increment the width of the graph
                print("Incremented the width of the graph:", actual_state[1])
            elif(actual_state[0] == 2):
                actual_state[1] -= 1  # Decrement the width of the graph
                print("Decremented the width of the graph:", actual_state[1])
            else:
                print("para")
                keepGoing = False
        # Convert decimal array back to bytes
         output = bytes(actual_state)
         c.send(output)  # Send modified data back
         print("Sent Updated =", list(output))

         # Receive
         actual_state = list(c.recv(32))
         print("Received Raw =", actual_state)
         time.sleep(0.2)
except socket.error as socketerror:
    print("S'ha trobat un error:")
    print(socketerror)
    c.close()
    s.close()
c.close()
s.close()
print ("Program finish")
