#!/usr/bin/env python
# -*- utf-8 -*-

import SocketServer
import random

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "%s wrote:" % (self.client_address[0])
        print self.data
        min, max = self.data.split(',')
        # just send back the same data, but upper-cased
        rnum = random.randint(int(min), int(max))
        self.request.sendall("%d\n" % rnum)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

