import socket
import network
import struct
import time
import _thread
import machine
import utime
import time

# Define which pin number controls the LED
fading_led_number: int = 16
blinking_led_number: int = 17

def fade_led():
    pwm_controller = machine.PWM(machine.Pin(fading_led_number))
    # Define the frequency of the PWM waveform
    pwm_controller.freq(1000)
    
    while True:
        print("Something")
        for duty in range(65025):
            pwm_controller.duty_u16(duty)
            utime.sleep_us(1)
        
        for duty in range(65025, 0, -1):
            pwm_controller.duty_u16(duty)
            utime.sleep_us(1)

# Start thread on first core
_thread.start_new_thread(fade_led,())

blinking_led: machine.Pin = machine.Pin(blinking_led_number, machine.Pin.OUT)

while True:
    print("Something else")
    blinking_led.toggle()
    utime.sleep_ms(500)
    

