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

#def test_ranger():
 #   d = rr.get_distance()
  #  while d > 10:
   #     print(d)
    #    time.sleep(1)
     #   d = rr.get_distance()
    #print"PASS"


pwmPin = 18
dc = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 320)
rr = RRB2()

var = 'n'
speed1 = 0
speed2 = 0
direction1 = 1
direction2 = 1
d = rr.get_distance()

distance = rr.get_distance()

while var != 'q':
    var = getch()
    print(d)
    if var == 'b':
	speed1 = 0.5
	direction2 = 1
	#speed2 = 0.5
	#direction2 = 1
	#print(d)
    if var == 'f':
	speed2 = 0.5
	#direction1 = 0
	#speed2 = 0.5
	direction2 = 0
	#print(d)
    if var == 's':
	#speed1 = 0.1
	speed2 = 0.1
	direction1 = 1
	direction2 = 1
    if var == 'l':
	speed1 = 0.5
	#direction1 = 1
	#speed2 = 1
	direction1 = 1
	#print(d)
    if var == 'r':
	speed1 = 0.5
	#direction1 = 0
	#speed2 = 1
	direction1 = 0
        #print(d)
	#print("Left: ", distL, " cm Right: ", distR, " cm")
#print distance
    #test_ranger()
    d = rr.get_distance()
    rr.set_motors(speed1, direction1, speed2, direction2)
	#distL = distanceL()
	#distR = distanceR()
	#print "Left: ", distL, " cm Right: ", distR, " cm"
#print ("loop, please CTRL C to cancel")
#while 1:
	#test_ranger()
    time.sleep(0.1)

#while True:
#            distL = distanceL()
#	    distR = distanceR()
#            print "Left: ", distL, " cm"
#	    print "Right: ", distR, " cm" 
#            time.sleep(1)
pwm.stop()
GPIO.cleanup()


