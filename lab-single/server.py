import socket, sys, re, os

from threading import Thread


sys.path.append("../lib")       # for params
import params

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )



progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''       # Symbolic name meaning all available interfaces

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(1)              # allow only one outstanding request
# s is a factory for connected sockets


threadCount = 0

def listener_thread(s,conn,addr, threadCount):
    id = threadCount
    data = conn.recv(1024).decode()
    if not data:
        print("Conn empty")
    # data = s.recv(1024).decode()
    # print(data)
    # file_name = data[1]
    # if not os.path.isfile(file_name):
    #     fd = os.open(file_name, os.O_CREAT | os.O_WRONLY)

    #     while True:
    #         data = conn.recv(1024).decode().split(':')
    #         if not data:
    #             break
    #         len = data[0]
    #         payload = data[1]
    #         os.write(fd, payload)

    #     os.close(fd)
    
    print("Disconnecting: " + addr[0])
    conn.close()

    

listenPort = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', listenPort))
s.listen(10) 



while(True):
    print("Here")
    conn, addr = s.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    threadCount + 1
    x = Thread(target=listener_thread, args=(s,conn,addr,threadCount))
    x.start()

