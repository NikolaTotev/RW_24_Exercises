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



