import time
from servo_device import ServoDevice

# create the servo Device
SERVO_PIN = 17
servo = ServoDevice(SERVO_PIN)

angles = [0, 45, 90, 135, 180, 135, 90, 45]
print('Looping with Servo angles (Ctrl-C to quit)...')
try:
    while True:
        servo.set_angle(0)
        time.sleep(3)
        servo.set_angle(45)
        time.sleep(3)
        servo.set_angle(90)
        time.sleep(3)
except KeyboardInterrupt:
  servo.stop()