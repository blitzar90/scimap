import SocketServer
import SimpleHTTPServer

handler=SimpleHTTPServer.SimpleHTTPRequestHandler
http_Server=SocketServer.TCPServer(('',8000),handler)
http_Server.serve_forever()