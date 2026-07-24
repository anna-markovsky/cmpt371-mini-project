#Client
import socket
#import rdt
import sys
import time
from utility import UtilityClass

#Open UDP socket

class ClientClass:

    serverName = 'localhost'
    serverPort = 12000

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #clientSocket.setblocking(0)
    seconds = 10
    seqNum = 0
    ackNum = 0
    utility = UtilityClass()

    #clientSocket.connect((serverName, serverPort))
    while True:

#Send CONNECT
        d = input("Input data: ")
        # calculate the amount of bytes in data 
        byte_count = len(d.encode('utf-8'))
        ackNum += (seqNum + byte_count)
        print("seq num=", seqNum)
        print("ackNum ", ackNum)
        data = utility.rdt_send(seqNum, ackNum, d)



#Receive ACCEPT
        clientSocket.settimeout(10.0)

        try:
            # divmod splits the total seconds into minutes and remaining seconds
            #mins, secs = divmod(seconds, 60)
           

            ack, receiver_address = clientSocket.recvfrom(1024)
            print(ack.decode())
        except TimeoutError:


        #if timeout happens, resend packet
            print("Timeout")
            utility.udt_send(data)


#Begin sending packets



#Wait for ACKs



#Retransmit if timeout



#Close connection