import time
import RPi.GPIO as GPIO

DirPin = 2
StepPin = 3

CW = 0
CCW = 1
Delay = 0.005

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DirPin, GPIO.OUT)
GPIO.setup(StepPin, GPIO.OUT)


try:
    while True:
        Steps = input('Enter number of steps: ')
        Dir = input('Enter a Dir!!!!!!!!!!!!!!')
        Dir = Dir.upper()
        if Dir == 'CW':
            GPIO.output(DirPin, CW)
        elif Dir == 'CCW':
            GPIO.output(DirPin, CCW)
        else:
            Dir = input('Enter a Dir you twat')
        for step in range(Steps):
            GPIO.output(StepPin, True)
            time.sleep(Delay)
            GPIO.output(StepPin, False)
            time.sleep(Delay)
except KeyboardInterrupt:
    print('Fuck off then')

GPIO.cleanup()

  File "/home/pi/Rubiks-Cube/PiBasicRotation.py", line 26, in SetupGPIOPins
    GPIO.setup(DirPin, GPIO.OUT)
NameError: name 'DirPin' is not defined
