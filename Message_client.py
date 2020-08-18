import socket

def Main():



    host = "0.0.0.0"
    # modify this port for your own port
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
    
if __name__ =='__main__':
    Main()
