import socket
import sys
import _thread

def EchoServer(csocket, addr):
    while True:
        client_data = csocket.recv(2048)
        if client_data:
            csocket.send(client_data)
        else:
            csocket.close()
            return 

echoServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
echoServer.bind(("192.168.1.103", int(sys.argv[1])))
echoServer.listen(3)

while True:
    cSock, addr = echoServer.accept()
    _thread.start_new_thread(EchoServer, (cSock, addr))