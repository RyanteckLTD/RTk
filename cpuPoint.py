#!/usr/bin/python
# Import required libraries
import zeropoint as zp
import psutil
from time import sleep
zp.init()

#Reset ZP
zp.stepToZero()


while True:
	cpuPercent = psutil.cpu_percent()
	print(cpuPercent)
	cpuPercent = cpuPercent / 100
	zeroPointPercent = cpuPercent*600
	zp.stepTo(zeroPointPercent)
	sleep(0.2)
	
