import time
import RPi.GPIO as rpi ## Import Raspberry Pi GPIO library

rpi.setmode(rpi.BOARD)
rpi.cleanup()

class LED(object):
    #Use LED(pinnumber) to set the correct pin.
    #Get and set the LED.state to True or False to turn on the LED and off.
    def __init__(self, pin):
        self.pin = pin
        rpi.setup( pin, rpi.OUT)

    def __str__(self):
        if self.state == True:
            return "LED at pin #"+str(self.pin)+" is on."
        else:
            return "LED at pin #"+str(self.pin)+" is off."

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        if self._state == True:
            rpi.output(self.pin, True)
        else:
            rpi.output(self.pin, False)

    @state.getter
    def state(self):
        return self._state
    

###Call LED.  Put an LED in pin 3 and blink it
##myled = LED(3)
##myled.state=True
##
##for i in range(0,20):
##    myled.state = not myled.state
##    print myled
##    time.sleep(1)

class SevenSegment(object):
    #Pins on top of display are (from left to right) 1, 2, ground, 3, and 4.
    #Pins on bottom of display are 5, 6, ground, 7, and 8.
    #Pass a list of all 8 pin numbers as pinlist.
    #Example: ss = SevenSegment([3, 5, 7, 8, 10, 11, 12])
    #
    #Usage:
    #ss = SevenSegment([3, 5, 7, 8, 10, 11, 12]) #List of 7 pins.
    #ss.off() #Turn display off.
    #ss.digit(4) #Display a 4.
    #time.sleep(3)
    #ss.number(1234567890, 0.3) #Display 1234567890 with one digit each 0.3 sec.
    
    def __init__(self, pinlist):
        self.pinlist = pinlist
        self.LEDlist = []
        self.poslist = []
        for pin in pinlist:
            thisLED = LED(pin)
            thisLED.state = False
            self.LEDlist.append(thisLED)
            self.poslist.append(0)
    
    def digit(self, digit):
        #Displays the digit on the seven segment display.
        if digit == 0:
            self.poslist = [0, 1, 1, 1, 1, 1, 1]
        if digit == 1:
            self.poslist = [0, 0, 0, 1, 0, 0, 1]
        if digit == 2:
            self.poslist = [1, 0, 1, 1, 1, 1, 0]
        if digit == 3:
            self.poslist = [1, 0, 1, 1, 0, 1, 1]
        if digit == 4:
            self.poslist = [1, 1, 0, 1, 0, 0, 1]
        if digit == 5:
            self.poslist = [1, 1, 1, 0, 0, 1, 1]
        if digit == 6:
            self.poslist = [1, 1, 1, 0, 1, 1, 1]
        if digit == 7:
            self.poslist = [0, 0, 1, 1, 0, 0, 1]
        if digit == 8:
            self.poslist = [1, 1, 1, 1, 1, 1, 1]
        if digit == 9:
            self.poslist = [1, 1, 1, 1, 0, 1, 1]
        i=0
        for led in self.LEDlist:
            if self.poslist[i] == 1:
                led.state = True
            else:
                led.state = False
            i+=1
            
    def number(self, number, delay):
        #Displays an integer as a string of digits
        # with a short delay (sec) between each digit
        num = [int(x) for x in str(number)]
        for dig in num:
            self.digit(dig)
            time.sleep(delay)
        return number
            
    def off(self):
        #Turns LED off
        for led in self.LEDlist:
            led.state = False
    def on(self):
        #Turns LED on
        for led in self.LEDlist:
            led.state = False