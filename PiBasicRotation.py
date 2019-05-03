import time
import RPi.GPIO as GPIO
#TODO
#implement method to work with 6 steppermotors that can rotate at the same time if possible (think top \n
#and bottom rotation vs top and left rotation)

#setup some physical system that will allow 6 motors to be run from 4 pins and a data cable for scheduling \n
#what motors to turn at a specific time (scheduler)

#find more adequete, higher current, 5v power supply and regulate

class MotorControl(object):
    def __init__(self):
        self.SetupGPIOPins()

    def SetupGPIOPins(self):
        self.DirPin = 2
        self.StepPin = 3

        self.Steps = 50
        self.CW = 0
        self.CCW = 1
        self.Delay = 0.005
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.DirPin, GPIO.OUT)
        GPIO.setup(self.StepPin, GPIO.OUT)

    def OrganiseMotorInput(self, inputString):
        """CW is clockwise, CCW is counter clockwise, will rotate motor depending on Direction"""
        if inputString == "1":
            ####################################
            MotorID = 5
            Direction = "CW"
            print("LCW")
        elif inputString == "3":
            MotorID = 2
            Direction = "CCW"
            print("RCCW")
        elif inputString == "q":
            #####################################
            MotorID = 5
            Direction = "CCW"
            print("LCCW")
        # elif inputString == "w":
        #  print("MCCW")
        elif inputString == "e":
            MotorID = 2
            Direction = "CW"
            print("RCW")
        elif inputString == "4":
            MotorID = 1
            Direction = "CW"
            print("BCW")
        # elif inputString == "5":
        # 	print("MCW")
        elif inputString == "6":
            MotorID = 4
            Direction = "CCW"
            print("TCCW")
        elif inputString == "r":
            MotorID = 1
            Direction = "CCW"
            print("BCCW")
        # elif inputString == "t":
        #  print("MCCW")
        elif inputString == "y":
            MotorID = 4
            Direction = "CW"
            print("TCW")

        elif inputString == "7":
            MotorID = 3
            Direction = "CW"
            print("BACW")
        # elif inputString == "8":
        #   print("MCW")
        elif inputString == "9":
            MotorID = 0
            Direction = "CCW"
            print("FCCW")
        elif inputString == "u":
            MotorID = 3
            Direction = "CCW"
            print("BACCW")
        # elif inputString == "i":
        #print("MCCW")
        elif inputString == "o":
            MotorID = 0
            Direction = "CW"
            print("FCW")
        self.Rotate90(MotorID, Direction)

    def Rotate90(self, MotorID, Direction):
        print("rotated ", MotorID, " 90 degrees ", Direction)
        if Direction == 'CCW':
            GPIO.output(self.DirPin, self.CCW)
        elif Direction == 'CW':
            GPIO.output(self.DirPin, self.CW)
        for step in range(self.Steps):
            GPIO.output(self.StepPin, True)
            time.sleep(self.Delay)
            GPIO.output(self.StepPin, False)
            time.sleep(self.Delay)
    

# def main():
# 	motors = MotorControl()

# 	motors.rotate90(0, "CW")
# 	motors.rotate90(0, "CCW")


# if __name__ == '__main__':
# 	main()
# 	GPIO.cleanup()
