#


import socket

def Main():
    # set host to your own specification
    host = "0.0.0.0"
    port = 5555
    
    sock = socket.socket()
    sock.connect((host, port))    

    message = input(">> ")
    while message != 'q':
        sock.sendto(message)
        data = sock.recv(1024)
        print("Received from server: " + str(data))
        message = input(">> ")
        
    sock.close()
    
if __name__ =='__main__':
    Main()
