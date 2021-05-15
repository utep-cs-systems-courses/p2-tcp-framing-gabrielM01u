#!/usr/bin/env python3

import socket, sys, re, os, time



listenPort = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


filename = sys.argv[1]

fd = os.open(filename, os.O_RDONLY|os.O_CREAT)
assert fd >= 0

s.connect(('127.0.0.1',50001))
msg = str(len(filename))+':'+filename
fileRequest = s.send(msg.encode())

response = s.recv(1024).decode()
response = response.split(':')

if response[1] == 'NO':
    while True:
        content = os.read(fd,1000)
        if len(content) == 0:
            break
        length = bytes(len(content))
        payload = length+":".encode()+content
        s.send(payload)
    print("Finished sending!")
    pkg = "DONE"
    msg = str(4)+':'+pkg
    s.send(msg.encode())
elif response[1] == 'YES':
    print("File already exists in server.")

else:
    print(response)

s.close()





