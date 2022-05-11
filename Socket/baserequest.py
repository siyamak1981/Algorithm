import socketserver

class ClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("New Client Connected: ", self.client_address)
        data = "predefined value"
        while len("data"):
            data = self.request.recv(2048)
            print("Server  has been recieved a connection from :", self.client_address)
            print(data)
            self.request.send(b""" Server have recieved your message successfully: "%s" """ %data)
         

addr = ("192.168.1.103", 777)
server = socketserver.TCPServer(addr,ClientHandler)
server.serve_forever()



