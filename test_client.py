__author__ = 'nathan'


import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

message_stream = ['up', 'up', 'down', 'left', 'right', 'invalid']

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
while True:
    for message in message_stream:
        time.sleep(0.5)
        sock.sendto(message, (UDP_IP, UDP_PORT))