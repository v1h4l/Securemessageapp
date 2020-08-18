import socket

def Main():
    host = "127.0.0.1"
    #modiy this port for yout own port
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
#finish the script    
if __name__ =='__main__':
    Main()
