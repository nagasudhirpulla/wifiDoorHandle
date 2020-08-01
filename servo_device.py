import RPi.GPIO as GPIO

class ServoDevice(object):
    """Internet 'servo object' that can control GPIO on a Raspberry Pi."""
    servoPort = None

    def __init__(self, pinNumber=26):
        """Initialize the 'thing'."""
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pinNumber, GPIO.OUT)
        self.servoPort = GPIO.PWM(pinNumber, 50)
        self.servoPort.start(2.5)  # Initialization with 5% duty cycle

    def set_angle(self, ang):
        """Set the servo angle to the provided angle in degrees (0 to 180 degrees).
        """
        if ang < 0:
            ang = 0
        elif ang > 180:
            ang = 180
        dutyCycle = 5 + (ang*5/180)
        self.servoPort.ChangeDutyCycle(dutyCycle)
    
    def stop(self):
        self.servoPort.stop()
        GPIO.cleanup()