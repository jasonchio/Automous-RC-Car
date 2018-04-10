import RPi.GPIO as GPIO
import time
from rrb2 import *
import tty
import sys
import termios
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

pwmPin = 18
dc = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 320)
rr = RRB2()

pwm.start(dc)
rr.set_led1(1)

rr.set_motors(1, 1, 1, 1)

print ("loop, please CTRL C to cancel")
while 1:
	time.sleep(0.075)

pwm.stop()
GPIO.cleanup()
