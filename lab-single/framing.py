import socket

SYN_SEQ = b'\x00\x00\x00\x00'
SYNACK_SEQ = b'\x00\x00\x00\x01'
ACK_SEQ = b'\x00\x00\x00\x00'
HEADER_LENGTH = 13

class frame:

    seq = 0
    ack = 0

    def __init__(self,port,socket):
        self.port = port
        self.socket = socket

    def sendSYN(self, rport):
        global ack

        src_port = self.port.to_bytes(2, 'big') # append src port
        header = bytearray(src_port)
        dest_port = rport.to_bytes(2,'big') 
        header.append(dest_port)                # append dest port
        header.append(SYN_SEQ)                  # append seq # for SYN packet
        header.append(self.ack.to_bytes(4,'big'))
        header.append(HEADER_LENGTH.to_bytes(1,'big')) ##13 bytes total
        header.append(b'\x00\x00')
        self.socket.send(header)
        pass