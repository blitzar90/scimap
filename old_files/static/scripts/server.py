#!/usr/bin/env python

import db
import main as m
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir,sep

logger=m.logger('../../server_log.txt')

class myHandler(BaseHTTPRequestHandler):
    
    """
    handler for the GET requests;
    """
    
    def do_GET(self):
        
        if self.path=="/":
            self.path="../views/index.html"
        
        try:

            if self.path.endswith(".html"):
                logger.log('Sending html %s ...' % self.path)
                self.sendHTML(self.path)


        except IOError:
            logger.log('File Not Found: %s' % self.path, logType='error')
            self.send_error(404,'File Not Found: %s' % self.path)

    #def do_POST(self):


    def sendHTML(self,url):
        
        try:
            f = open(curdir + sep + url) 
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
            logger.log("Html '%s' has been sent." % url)
        except Exception as e:
            logger.log("Sending of html '%s' failed due to %s." % (url, str(e)))

    #def sendAnswer(self,url):
    #        self.send_response(200)
    #        self.send_header('Content-type','text/json')
    #        self.end_headers()
    #        self.wfile.write('{ '+url+': 3}')
    #        logger.log('Answer has benn sent.')

def main():
    try:
        port=80
        logger.log('Starting server...')
        server = HTTPServer(('0.0.0.0', 80), myHandler)
        print('Server is listening on port: %s' % port)
        server.serve_forever()
    except:
        logger.log('Shutting down server...')
        server.socket.close()

if __name__ == '__main__':
    main()