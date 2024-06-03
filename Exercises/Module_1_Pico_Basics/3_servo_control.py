from machine import Pin, PWM
import utime


# Small utility function for easier control
def angle_to_duty(target_angle):
    print(f"target{target_angle}")
    return int(6553/180 * target_angle + 1638)

# Here we use the output of the easing function to drive the servo. 
# Some additional transofrmations are needed for it to be useable for a servo input.
def easeToPosition (servo: PWM, current, target, speed=4):    
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

# The magic where easing is calculated
def easeInOutQuadratic(x: float):
  return  (2 * pow(x, 2)) if (x < 0.5) else ((-2 * pow(x, 2)) + (4 * x) - 1)


# Define which pin number controls the LED
servo_pin: int = 16

servo = PWM(Pin(servo_pin))

# Servos work with a PWM frequency of 40-200Hz, however 50Hz is recommended in general
servo.freq(50)

# Rotate servo to 180 degrees
duty_cycle_from_angle = angle_to_duty(180)
servo.duty_u16(duty_cycle_from_angle)
utime.sleep_ms(500)


# Rotate servo to 90 degrees
duty_cycle_from_angle = angle_to_duty(90)
servo.duty_u16(duty_cycle_from_angle)
utime.sleep_ms(500)


# Rotate servo to 0 degrees
duty_cycle_from_angle = angle_to_duty(0)
servo.duty_u16(duty_cycle_from_angle)
utime.sleep_ms(1000)


# To make the servo move smoother a technique called "easing" can be used. For our example we are using easeInOutQuadratic
current_duty_cycle = angle_to_duty(0) 
target_duty_cycle = angle_to_duty(180)
easeToPosition(servo, current_duty_cycle, target_duty_cycle)

current_duty_cycle = angle_to_duty(180) 
target_duty_cycle = angle_to_duty(0)
easeToPosition(servo, current_duty_cycle, target_duty_cycle)


# And now the servo move smoother!
while True:
    current_duty_cycle = angle_to_duty(0) 
    target_duty_cycle = angle_to_duty(180)
    easeToPosition(servo, current_duty_cycle, target_duty_cycle)
    utime.sleep_ms(1000)

    current_duty_cycle = angle_to_duty(180) 
    target_duty_cycle = angle_to_duty(0)
    easeToPosition(servo, current_duty_cycle, target_duty_cycle)
    utime.sleep_ms(1000)


