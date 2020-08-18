# server script



import optparse
import socket

def main():
    host = '127.0.0.1'
    port = 8090
    
    sock = socket.socket()
    sock.bind((host, port))
    
    sock.listen(1)
    c, addr = sock.accept()
    
    print("conection from; " + str(addr))
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print("from connected user: " + str(data))
        data = str(data).upper()
        print("sending: " + str(data))
        sock.send(data)
    
    sock.close()

if __name__ == '__main__':
    print("[+] Waiting for a connection.....")
    main()
