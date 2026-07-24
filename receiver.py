#Client
import socket
#import rdt
import sys
import time
from utility import UtilityClass

class ServerClass:
    def rdt_recv(self,packet,expected):
        if (UtilityClass.is_corrupt):
            return 
        if(not UtilityClass.is_ack(expected, packet)):
            self.buffer.append(packet)
            return
    serverName = 'localhost'
    serverPort = 12000
    buffer = []

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((serverName, serverPort))
    s.listen(1)

    conn, addr = s.accept()

    while True:
        packet, sender_address = s.recvfrom(1024)
        #if packet wasnt lost we receive packet
        rdt_recv(packet)

        #send ack to sender
        s.sendto(packet.ackNum, sender_address)