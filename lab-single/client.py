import socket, sys, re, os


listenPort = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', listenPort))
s.listen(1)

fd = os.open("../../test.txt", os.O_RDONLY|os.O_CREAT)
assert fd >= 0

fileRequest = s.send(('8:test.txt').encode())

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





