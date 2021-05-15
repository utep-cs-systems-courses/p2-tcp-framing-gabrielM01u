#!/usr/bin/env python3

import socket, sys, re, os

from threading import Thread, Lock


# sys.path.append("../lib")       # for params
# import params

# switchesVarDefaults = (
#     (('-l', '--listenPort') ,'listenPort', 50001),
#     (('-?', '--usage'), "usage", False), # boolean (set if present)
#     )


lock = Lock()
listenPort = 50001
listenAddr = ''
# progname = "echoserver"
# paramMap = params.parseParams(switchesVarDefaults)

# listenPort = paramMap['listenPort']
# listenAddr = ''       # Symbolic name meaning all available interfaces

# if paramMap['usage']:
#     params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(1)              # allow only one outstanding request
# s is a factory for connected sockets


threadCount = 0

def listener_thread(s,conn,addr, threadCount):
    id = threadCount
    data = conn.recv(1024).decode()
    while not data:   
        print("...")
        data = conn.recv(1024).decode()

    print(data)
    
    data = data.split(':')
   
    file_name = data[1]
    if not os.path.isfile('../lib/'+file_name):
        response = 'NO'
        response = str(2)+':'+response
        conn.send(response.encode())
    
        fd = os.open('../lib/'+file_name, os.O_CREAT | os.O_WRONLY)

        while True:
            data = conn.recv(1024).decode().split(':')
            length = data[0]
            payload = data[1]
            if length == len(payload):
                lock.acquire()
                os.write(fd, payload)
                lock.release()
            elif payload == "DONE":
                break
            else:
                pass
        os.close(fd)
    else:
        response = 'YES'
        conn.send((str(3)+':'+response).encode())
    
    print("Disconnecting: " + addr[0])
    conn.close()

    

# listenPort = 8000

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('', listenPort))
# s.listen(10) 



while(True):
    print("Here")
    conn, addr = s.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    threadCount + 1
    x = Thread(target=listener_thread, args=(s,conn,addr,threadCount))
    x.start()
s.close()

