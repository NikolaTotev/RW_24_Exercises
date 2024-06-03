import machine
import utime

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
