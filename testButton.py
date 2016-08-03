# testButton.py  05/05/2014  D.J.Whale
#
# Test that the button works

import time
TIME = 0.1

# Raspberry Pi
#import RPI.GPIO as GPIO
#BUTTON = 4

# Arduino
import anyio.GPIO as GPIO
BUTTON = 21
LED = 4
def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(BUTTON, GPIO.IN,pull_up_down=GPIO.PUD_UP)
  GPIO.setup(LED, GPIO.OUT)
  
def loop():
  while True:
    time.sleep(TIME)
    b = GPIO.input(BUTTON)
    if not b:
      print(b)
      GPIO.output(LED,1)
    else:
      print(b)
      GPIO.output(LED,0)
try:
  setup()
  loop()
finally:
  GPIO.cleanup()

# END

