#TrafficHAT KS Demo
from time import sleep
t = 0.2
import anyio.GPIO as GPIO

RED = 4
YEL = 23
GRN = 24
BUZZ = 5
BUTT = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
#GPIO.setup(YEL, GPIO.OUT)
#GPIO.setup(GRN, GPIO.OUT)
#GPIO.setup(BUZZ,GPIO.OUT)
#GPIO.setup(BUTT,GPIO.IN)

try:
	while True:
		GPIO.output(RED, True)
		sleep(t)
		#GPIO.output(YEL, True)
		#sleep(t)
		#GPIO.output(GRN, True)
		#sleep(2)
		GPIO.output(RED, False)
		sleep(t)
		#GPIO.output(YEL, False)
		#sleep(t)
		#GPIO.output(GRN, False)
		#sleep(2)
		#GPIO.output(BUZZ, True)
		#sleep(t)
		#GPIO.output(BUZZ, False)
	
finally:
	GPIO.cleanup()
