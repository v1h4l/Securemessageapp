#once reaceived connection initiates handshake ad the output send
import socket
# main function

def Main():
    # set host to your own specification
    host = "0.0.0.0"
    port = 5555
    #port number
    
    sock = socket.socket()
    sock.connect((host, port))    

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
