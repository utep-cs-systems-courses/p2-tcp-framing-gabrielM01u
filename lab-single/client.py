import socket, sys, re, os


listenPort = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', listenPort))
s.listen(1)

# fd = os.open("/test.txt", os.O_RDONLY|os.O_CREAT)
# assert fd >= 0

