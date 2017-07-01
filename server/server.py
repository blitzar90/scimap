import SocketServer
import SimpleHTTPServer

handler=SimpleHTTPServer.SimpleHTTPRequestHandler
http_Server=SocketServer.TCPServer(('',80),handler)
http_Server.serve_forever()