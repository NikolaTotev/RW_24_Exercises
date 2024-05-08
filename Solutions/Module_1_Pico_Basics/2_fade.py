from machine import Pin, PWM
import utime

# Define which pin number controls the LED
led_pin_number: int = 16

pwm_controller = PWM(Pin(led_pin_number))

# Define the frequency of the PWM waveform
pwm_controller.freq(1000)

pwm_controller.duty_u16(5000)
utime.sleep_ms(2000)

pwm_controller.duty_u16(5000)
utime.sleep_ms(2000)

pwm_controller.duty_u16(5000)
utime.sleep_ms(2000)

pwm_controller.duty_u16(5000)
utime.sleep_ms(2000)

while True:
    for duty in range(65025):
        pwm_controller.duty_u16(duty)
        utime.sleep_us(1)
    
    for duty in range(65025, 0, -1):
        pwm_controller.duty_u16(duty)
        utime.sleep_us(1)

        