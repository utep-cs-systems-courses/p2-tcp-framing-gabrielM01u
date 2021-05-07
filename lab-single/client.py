#!/usr/bin/env python3

import socket, sys, re, os, time
sys.path.append("../lib")       # for params
import params
switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:8000"),
    (('-d', '--delay'), 'delay', "0"),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )


#progname = "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage  = paramMap["server"], paramMap["usage"]

if usage:
    params.usage()

try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

s = None
for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        print("creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto))
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        print(" error: %s" % msg)
        s = None
        continue
    try:
        print(" attempting to connect to %s" % repr(sa))
        s.connect(sa)
    except socket.error as msg:
        print(" error: %s" % msg)
        s.close()
        s = None
        continue
    break

if s is None:
    print('could not open socket')
    sys.exit(1)

delay = float(paramMap['delay']) # delay before reading (default = 0s)
if delay != 0:
    print(f"sleeping for {delay}s")
    time.sleep(delay)
    print("done sleeping")




listenPort = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', listenPort))
s.listen(1)

fd = os.open("test.txt", os.O_RDONLY|os.O_CREAT)
assert fd >= 0
conn, addr = s.accept()
fileRequest = conn.send(('YO').encode())

response = s.recv(1024).decode()
response = response.split(':')

if response[1] == 'NO':
    while True:
        content = os.read(fd,1000)
        if len(content) == 0:
            break
        payload = bytes(len(content)+':')+content
        s.send(payload)
    print("Finished sending!")
elif response[1] == 'YES':
    print("File already exists in server.")

else:
    print(response)

s.close()





