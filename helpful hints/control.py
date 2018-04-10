import RPi.GPIO as GPIO
import time
from rrb2 import *
import tty
import sys
import termios
import time
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

var = 'n'
speed1 = 0
speed2 = 0
direction1 = 1
direction2 = 1

while var != 'q':
    var = getch()
    if var == 'f':
	speed1 = 0
	direction2 = 1
	speed2 = 0.9
	direction2 = 1
    if var == 'b':
	speed2 = 0.9
	direction1 = 0
	speed1 = 0
	direction2 = 0
    if var == 's':
	speed1 = 0.1
	speed2 = 0.1
	direction1 = 1
	direction2 = 1
    if var == 'l':
	speed1 = 0.5
	#direction1 = 1
	#speed2 = 1
	direction1 = 1
    if var == 'r':
	speed1 = 0.5
	#direction1 = 0
	#speed2 = 1
	direction1 = 0

    rr.set_motors(speed1, direction1, speed2, direction2)

#print ("loop, please CTRL C to cancel")
#while 1:
    time.sleep(0.1)


pwm.stop()
GPIO.cleanup()
