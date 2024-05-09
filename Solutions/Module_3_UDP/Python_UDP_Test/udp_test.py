import time
import socket

for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    message = b'test'
    addr = ("192.168.4.1", 2390)

    while True:        
        client_socket.sendto(message, addr)
        print("Sending...")
        time.sleep(0.1)