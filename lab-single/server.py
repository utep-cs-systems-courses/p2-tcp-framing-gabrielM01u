import socket, sys, re, os
from threading import Thread


threadCount = 0

def worker_thread(conn, threadCount):
    while True:
        data = conn.recv(2048)
        print(data.decode('utf-8'))
        if not data:
            break
    print("Disconnecting: " + addr[0])
    conn.close()

listenPort = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', listenPort))
s.listen(1) 

while(True):
    conn, addr = s.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    threadCount + 1
    x = Thread(target=worker_thread, args=(conn, threadCount))
    x.start()

