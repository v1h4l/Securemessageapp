import socket
import sys
from select import *
from time import ctime,time

host_name= socket.gethostname()
#HOST = socket.gethostbyname(host_name)
HOST = '127.0.0.1'
SOCKET_LIST=[]
RECV_BUFFER= 4096
PORT = 5555



def server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind((HOST, PORT))
    SOCKET_LIST.append(server_sock)
    
    
    print("starting time is: ", ctime())
    print("server chat is innitilizing in port :" + str(PORT))
    while 1: 
        now, hey, error = select(SOCKET_LIST, [], [])
        for sock in lettore:
            if sock == server_sock:
                conn, address, =server_sock.accept()
                SOCKET_LIST.append(conn)
                
                print("1l client (%s, %s) si e comence" % address)
                transmission(server_sock, conn, "[%s, %s] >> entrato $ my chat room\n")
            else:
                try:
                    data = sock_recv(RECV_BUFFER)
                    if data:
                        transmission(server_sock, sock, "\r" + str(sock.getpeername()) +"> "+ data)
                        
                    else:
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)
                        
                        transmission(server_sock, sock, "its client (%s, %S)e' uscito....\n" % address)
                except:
                    transmission(server_sock, sock, "its client (%s, %S)e' uscito....\n" % address)
                    continue
                
    server_sock.close()
    
def transmission(server_socket, sock, message):
    for socket in SOCKET_LIST:
        if socket != server_socket and socket!= sock:
            try:
                socket.send(message)
            except:
                socket.close()
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
                    
if __name__ == '__main__' :
    sys.exit(server())
                    
            
