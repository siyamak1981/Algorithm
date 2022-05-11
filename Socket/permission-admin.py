import socketserver
import http.server

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/admin/":
            self.wfile.write(b"Permission Denied")
            b = bytes(self.headers)
            self.wfile.write(b)
        else:
            http.server.SimpleHTTPRequestHandler.do_GET(self)

addr = ("", 777)
httpServer = socketserver.TCPServer(addr, RequestHandler)
httpServer.serve_forever()