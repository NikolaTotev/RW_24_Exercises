import socket
import network
import struct
import time
import _thread
import machine
import utime
import time
import servo_utils as utils

ssid = "MiniBotAP"
password="Boti24"
servo_pin = 16
servo = machine.PWM(machine.Pin(servo_pin))
servo.freq(50)

data_lock = _thread.allocate_lock()

udp_data = 0


def angle_to_duty(target_angle):
    print(f"target{target_angle}")
    return int(6553/180 * target_angle + 1638)

def easeInOutQuadratic(x: float):
  return  (2 * pow(x, 2)) if (x < 0.5) else ((-2 * pow(x, 2)) + (4 * x) - 1)


def easeToPosition (servo: machine.PWM, current, target, speed=3):    
    print(f"Current {current}, Target {target}")
    if current < target:
        diff = target - current
        for x in range (0, 1000, 6):
            servo.duty_u16(current + int(easeInOutQuadratic(x/1000)*diff))
            utime.sleep_ms(speed)
    
    if current > target:
        diff = current - target
        for x in range (0, 1000, 6):
            servo.duty_u16(current - int(easeInOutQuadratic(x/1000)*diff))
            utime.sleep_ms(speed)

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
        global udp_data
        data_lock.acquire()
        udp_data = data        
        data_lock.release()


def movement_loop():
    
    current_position = 0

    # We have to set the initial position of the servo
    servo.duty_u16(utils.angle_to_duty(current_position))

    while True:
        global udp_data        
        data_lock.acquire()
        local_data = int(udp_data)
        data_lock.release()
        
        if local_data != current_position:
            print(f"Moving to new position: {local_data}")
            new_position = utils.angle_to_duty(local_data)
            utils.easeToPosition(servo, utils.angle_to_duty(current_position), new_position)
            current_position= local_data

        utime.sleep_ms(100)

            
# Start the movement loop on core 1
_thread.start_new_thread(movement_loop,())


# Start the UDP loop on this core
udp_server(ssid, password)

