
import socket

def Main():
    host = "127.0.0.1"


import socket

def Main():
    host = "0.0.0.0"
    port = 5555
    
    sock = socket.socket()
    sock.connect((host, port))    
    # output after a successfull connection
    message = input(">> ")
    while message != 'q':
        sock.sendto(message)
        data = sock.recv(1024)
        print("Received from server: " + str(data))
        message = input(">> ")
        
    sock.close()
#finish the script    
if __name__ =='__main__':
    Main()
