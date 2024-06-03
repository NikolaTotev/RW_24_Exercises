from machine import Pin
import utime

# Define which pin number controls the LED
led_pin_number: int = 16

# Initialize pico pin
led_pin: Pin = Pin(led_pin_number, Pin.OUT)

# Turn pin on
led_pin.value(1)

led_pin.value(0)

# This is how to sleep
utime.sleep_ms(500)

# Turn pin off
led_pin.value(0)

# Blink pin
while True:        
    led_pin.value(1)        
    utime.sleep_ms(500)        
    led_pin.value(0)
    utime.sleep_ms(500)        

        








