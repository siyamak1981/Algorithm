import socket
import socketserver
import http.server

addr = ("192.168.1.103", 777)
httpServer = socketserver.TCPServer(addr, http.server.SimpleHTTPRequestHandler)
httpServer.serve_forever()


