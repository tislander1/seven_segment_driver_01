# seven_segment_driver_01
Seven segment driver

3. This Python 2 program provides a rather sophisticated 7-segment display driver for the Raspberry Pi.
Features:

ss = SevenSegment([3, 5, 7, 8, 10, 11, 12]) (A list of 7 raspberry pi pins) instantiates the seven segment display.
ss.off() turns the seven segment display off, while ss.on() turns it on again.
ss.digit(4) displays a 4 on the LED.
ss.number(1234567890, 0.3) displays the number 1234567890 with one digit every 0.3 sec.
