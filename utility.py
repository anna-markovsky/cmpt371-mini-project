import socket
import random
import time
import struct

class UtilityClass:
    serverName = 'localhost'
    serverPort = 12000
    @staticmethod
    def make_pkt(seqNum, ackNum, checksum, data):
        #here data is already encoded
        header_format = "!IIH" 
        payload = data.encode('utf-8')
        payload_len = len(payload)
        header_bytes = struct.pack(header_format, seqNum, ackNum, payload_len)
        packet = header_bytes + payload
        #pkt = Packet(seqNum, ackNum, checksum, data)
        #return f"{seq_num}|{checksum}|{data}".encode('utf-8')
        return packet

    def rdt_send(self, seqNum, ackNum, data):
        # 1. You must calculate or define the checksum first
        checksum = self.calculate_checksum(data) 
        packet = self.make_pkt(seqNum, ackNum, checksum, data)
        self.udt_send(packet)
        return packet
    def udt_send(self, packet):
        print("performing udt send")
        if random.random() < 0.10:
            print("Packet was lost. This happens 10% of the time.")
            return 
        else:
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            udp_socket.sendto(packet, (self.serverName, self.serverPort))
  
        

    #calculates the checksum of the data in packet
    def calculate_checksum(self, data):
        # Placeholder for your actual checksum logic
        return len(data) 
    #checks if the checksum value in header matches the checksum of the data
    def is_corrupt(self, packet):
        expected_checksum = packet.checksum
        actual_checksum = self.calculate_checksum(packet.data)
        return (expected_checksum != actual_checksum)
    def is_ack(self, expectedAck, packet):
        return expectedAck == packet.ackNum
    def start_countdown(seconds):
        while seconds > 0:
            # divmod splits the total seconds into minutes and remaining seconds
            #mins, secs = divmod(seconds, 60)
            time.sleep(1)
            seconds -= 1
            
        print("Timeout")