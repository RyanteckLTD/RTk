#TrafficHAT KS Demo
from time import sleep
t = 0.1
import anyio.GPIO as GPIO

gpios = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

GPIO.setmode(GPIO.BCM)
while True:
	for cGPIO in gpios:
		print("Testing GPIO", cGPIO);
		GPIO.setup(cGPIO,GPIO.OUT)
		raw_input("Press enter to continue")
		GPIO.output(cGPIO,1)
	sleep(1)
	for cGPIO in gpios:
		#sleep(t)
		raw_input("Press enter to continue")
		GPIO.output(cGPIO,0)
		#sleep(t)
	sleep(1)
