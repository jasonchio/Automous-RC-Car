import RPi.GPIO as io
import time

io.setmode(io.BCM)
io.setwarnings(False)

trigL= 23
echoL= 24
trigR= 27
echoR= 22

io.setup(trigL,io.OUT)
io.setup(echoL,io.IN)
io.setup(trigR,io.OUT)
io.setup(echoR,io.IN)

def distanceL():

#io.setup(trigL, False)
#time.sleep(1)
    io.output(trigL, True)
    time.sleep(.0001)
    io.output(trigL, False)

    while io.input(echoL) == 0:
        startL = time.time()

    while io.input(echoL) == 1:
        endL = time.time()

    durationL = endL - startL
    distanceL = durationL *17150
    distanceL = round(distanceL, 2)

    return distanceL



def distanceR():
#io.setup(trigR, False)
#time.sleep(1)
    io.output(trigR, True)
    time.sleep(.00001)
    io.output(trigR, False)

#while io.input(echoL) == 0:
 #   startL = time.time()

#while io.input(echoL) == 1:
#    endL = timetime()

    while io.input(echoR) == 0:
        startR = time.time()

    while io.input(echoR) == 1:
        endR = time.time()

#durationL = endL - startL
#distanceL = durationL *17150
#distanceL = round(distanceL, 2)

    durationR = endR - startR
    distanceR = durationR *17150
    distanceR = round(distanceR, 2)
#print "Left Distance: ", distanceL, " cm"
#print "Right Distance: ", distanceR, " cm"
    return distanceR

if __name__ == '__main__':
    try:
        while True:
            distL = distanceL()
	    distR = distanceR()
            print "Left: ", distL, " cm"
	    print "Right: ", distR, " cm" 
            time.sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by User")

	io.cleanup()
