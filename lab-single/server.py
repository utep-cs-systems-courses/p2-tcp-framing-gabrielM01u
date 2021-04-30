import socket, sys, re, os
from framing import frame
from threading import Thread



threadCount = 0

def listener_thread(s,conn,addr, threadCount):
    id = threadCount
    rport = addr[1]
    ack = 0
    while True:
        data = conn.recv(2048)
        if tcp_logic(data) == 1:
            ack = 1
            s.send(packet.synack_packet(rport,ack))
            ack = 0
        elif tcp_logic(data) == 2:
            s.send(packet.)
        if not data:
            break
    print("Disconnecting: " + addr[0])
    conn.close()

def tcp_logic(data):

    if data and len(data) == 14:
        if data[:13] == b'\x01':
            print('SYN recvd')
            return 1
        elif data[:13] == b'\x02':
            print('ACK recvd')
            return 2
    

listenPort = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', listenPort))
s.listen(1) 

packet = frame(listenPort, s)

while(True):
    conn, addr = s.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    threadCount + 1
    x = Thread(target=listener_thread, args=(s,conn,addr,threadCount))
    x.start()

