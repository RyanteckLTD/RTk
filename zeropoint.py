#!/usr/bin/python
# Import required libraries
import sys, time, threading
import anyio.GPIO as GPIO

def init(delay = 0.0015):
  global running, StepCount, StepDir, stepsToDo, StepPosition, StepPins
  global StepCounter, Seq, WaitTime
  # Use physical pin numbers
  GPIO.setmode(GPIO.BCM)
 
  # Define GPIO signals to use
#  StepPins = [35,36,32,33]   # RoboHat
  StepPins = [4, 17, 27, 18]  # ZeroPoint
 
  # Set all pins as output
  for pin in StepPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)

  # Define pin sequence
  Seq = [[1,0,0,1],
       [1,0,1,0],
       [0,1,1,0],
       [0,1,0,1]]
       
  StepCount = len(Seq)
  StepDir = 1 # 1 == clockwise, -1 = anticlockwise
  StepsToDo = 0 #number of steps to move
  StepPosition = 0 # current steps anti-clockwise from the zero position

  # Initialise variables
  StepCounter = 0
  WaitTime = delay
  running = True
  # Move pointer to zero position
  StepDir = -1
  stepsToDo = 700
  step()

#======================================================================
  
# Create step loop which can run in separate thread
def step():
  global running, StepCounter, stepsToDo
  while running and stepsToDo>0:
    for pin in range(0,4):
      xpin = StepPins[pin]# Get GPIO
      if Seq[StepCounter][pin]!= 0:
        GPIO.output(xpin, True)
      else:
        GPIO.output(xpin, False)   
    StepCounter += StepDir
    if (StepCounter>=StepCount):
      StepCounter = 0
    if (StepCounter<0):
      StepCounter = StepCount + StepDir
    stepsToDo -= 1
    #print stepsToDo
    time.sleep(WaitTime)
  # clear the output pins
  for pin in StepPins:
    GPIO.output(pin, False)
  running = False

def cleanup():
  running = False
  time.sleep(1)
  GPIO.cleanup()

def stepToZero():
  global StepPosition, StepDir, stepsToDo, running
  #override existing command and force zero position
  running = False
  time.sleep(WaitTime * 4)
  StepDir = -1
  stepsToDo = 700
  StepPosition = 0
  threadN = threading.Thread(target = step)
  running = True
  threadN.start()
  
def stepTo (pos):
  global StepPosition, StepDir, stepsToDo, running
  if (not running):
    stepsToDo = pos - (StepPosition - stepsToDo*StepDir)
    StepDir = 1
    if (stepsToDo < 0):
      StepDir = -1
      stepsToDo = -stepsToDo
    StepPosition = pos
    # Startup the stepping thread
    threadC = threading.Thread(target = step)
    running = True
    threadC.start()

