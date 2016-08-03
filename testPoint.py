#!/usr/bin/python
# Import required libraries
import zeropoint as zp

#======================================================================
# Reading single character by forcing stdin to raw mode
import sys
import tty
import termios

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)  # 16=Up, 17=Down, 18=Right, 19=Left arrows

# End of single character reading
#======================================================================

print ('ZeroPoint Test script')
print ('Press 0..6 to to move to position, or z to force to zero position')
print ('Press ctrl-c to exit')

zp.init(delay = 0.0011)

try:
  while True:
    keyp = readkey()
    if keyp == '1':
      zp.stepTo(100)
      print ('Step to 100')
    elif keyp == '2':
      zp.stepTo(200)
      print ('Step to 200')
    elif keyp == '3':
      zp.stepTo(300)
      print ('Step to 300')
    elif keyp == '4':
      zp.stepTo(400)
      print ('Step to 400')
    elif keyp == '5':
      zp.stepTo(500)
      print ('Step to 500')
    elif keyp == '6':
      zp.stepTo(600)
      print ('Step to 600')
    elif keyp == '7':
      zp.stepTo(650)
      print ('Step to 700')
    elif keyp == '0':
      zp.stepTo(0)
      print ('Step to 0')
    elif keyp == 'z':
      zp.stepToZero()
      print ('Force to Zero')
    elif keyp == 'l':
      StepDir = -1
    elif keyp == 'r':
      StepDir = 1
    elif ord(keyp) == 3:
      break
    else:
      stepMotor = -1
      print ('Stop')

except KeyboardInterrupt:
    print

finally:
  zp.cleanup()
    

