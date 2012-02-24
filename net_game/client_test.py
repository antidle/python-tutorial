import socket, time

HOST = 'localhost'    # The remote host
PORT = 50000              # The same port as used by the server
VERSION = '  0'
TOTAL = 2
ID_SIZE=1

# Echo client program
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(VERSION)
my_id = int(s.recv(ID_SIZE))
print 'my_id', my_id

while 1:
    time.sleep(1)
    s.sendall('a')
    data = str(s.recv(TOTAL))
    print data
s.close()
