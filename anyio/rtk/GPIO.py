# anyio/arduino/GPIO.py  21/04/2014  D.J.Whale
#
# An ardunio (serial) based GPIO link

# CONFIGURATION ========================================================
   
DEBUG = False
USE_EMBEDDED_PYSERIAL = True

MIN_PIN = 2
MAX_PIN = 22

IN      = 0
OUT     = 1
BCM     = 0
BOARD   = 1
HIGH    = 1
LOW     = 0


# OS INTERFACE =========================================================

from .. import protocol
from .. import adaptors
import anyio.rtk.portscan as portscan

if USE_EMBEDDED_PYSERIAL:
  from os import sys, path
  thisdir = path.dirname(path.abspath(__file__))
  sys.path.append(thisdir)

import serial

  
# STATIC REDIRECTORS ===================================================

# Find out if there is a pre-cached port name.
# If not, try and find a port by using the portscanner

name = portscan.getName()
if name != None:
  if DEBUG:
    print("Using port:" + name)
  PORT = name
else:
  name = portscan.find()
  if name == None:
    raise ValueError("No port selected, giving in")
  PORT = name
  print("Your anyio board has been detected")
  print("Now running your program...")

BAUD = 230400


s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

s.close()
s.port = PORT
s.open()

    
instance = protocol.GPIOClient(adaptors.SerialAdaptor(s), DEBUG)
    
def setmode(mode):
  instance.setmode(mode)
  
def setup(channel, mode):
  instance.setup(channel, mode)
  
def input(channel):
  return instance.input(channel)
  
def output(channel, value):
  instance.output(channel, value)
  
def cleanup():
  instance.cleanup()
  
# END
