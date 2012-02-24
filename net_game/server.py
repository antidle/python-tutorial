# Simple game server?
import socket
import logging
import sys

TOTAL = 2  # n of clients
DATA_SIZE = 1   # 1 byte protocol
HOST = '0.0.0.0'                 # Symbolic name meaning all available interfaces
PORT = 50000              # Arbitrary non-privileged port
VERSION = "  0"
DEBUG = True

if DEBUG:
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    
logging.info('server started')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)
logging.debug('socket initialized. waiting for conneciton')

# wait for connections 
conns = []

client_id = 0
while len(conns) < TOTAL:
    conn, addr = s.accept()
    logging.info('connection from %s' % str(addr))
    ver = conn.recv(3)
    if ver == VERSION:
        logging.info('id %d vertion ok' % client_id)
        conns.append(conn)
        client_id += 1
    else:
        logging.warning('version error : received %s', ver.encode('string-escape'))
        conn.close()

logging.info('all client ready : %d' % len(conns))

client_id =0
for conn in conns:
    conn.sendall(str(client_id))
    client_id = client_id + 1

# init all client
def broadcast(conns, data):
    logging.debug('broadcasting : [%s]', data.encode('string-escape'))
    for con in conns:
        conn.sendall(data)
    logging.debug('broadcasted : [%s]', data.encode('string-escape'))

# do broadcast in blocking mode
while 1:
    history = []
    turn = ""
    client_id = 0
    for conn in conns:
        logging.debug('reading from client %d' % client_id)
        data = conns[client_id].recv(1)
        if len(data) == 0:
            logging.error('connection closed?')
            sys.exit()
        turn += data
        logging.info('data received from %d: [%s]' %(client_id, data.encode('string-escape')))
        client_id += 1
    history.append(turn)
    broadcast(conns, turn)

