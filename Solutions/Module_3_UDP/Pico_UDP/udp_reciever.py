import socket
import network
import struct
import time
import _thread
import machine
import utime
import time


ssid = "MiniBot_AP_6"
password="MiniBot4224" #x1
#password="MiniBot8448" #x2
#password="MiniBot12672" #x3
#password="MiniBot16896" #x4
#password="MiniBot210120" #x5
#password="MiniBot252144" #x6

def inet_aton(addr:str):
    return bytes(map(int, addr.split(".")))

def udp_server(ssid, password):
    
    print("Starting AP")
    ap = network.WLAN(network.AP_IF)
    ap.config(ssid=ssid, password = password)    
    ap.active(True)

    while ap.active() is False:
        pass

    print("AP ready, setting socket options")
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 2390))
    udp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, struct.pack(">4sI", inet_aton('224.1.1.1'),0))
    print(ap.ifconfig())
   

    while True:
        data, addr = udp_socket.recvfrom(16)            
        print(f"Received: {data}")
        
udp_server(ssid, password)

