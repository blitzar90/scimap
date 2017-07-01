import sys
sys.path.append('/root/scimap/')
from main import logger
import SocketServer
import SimpleHTTPServer

logger=logger('./server_log.txt')
logger.log('Starting server')
handler=SimpleHTTPServer.SimpleHTTPRequestHandler
http_Server=SocketServer.TCPServer(('',80),handler)
http_Server.serve_forever()
