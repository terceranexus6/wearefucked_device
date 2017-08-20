import serial # you need to install the pySerial :pyserial.sourceforge.net
import time
from sys import argv
from collections import Counter
from string import punctuation

#connect to the serial port, arduino. Yours may change
arduino = serial.Serial('/dev/ttyACM0', 9600)

#read the file and count the times a word appears
def lcount(keyword, fname):
  with open(fname, 'r') as fin:
    return sum([1 for line in fin if keyword in line])

#count different censored countries
datat = lcount('twitter','/usr/local/bro/logs/current/x509.log') 
dataf = lcount('facebook','/usr/local/bro/logs/current/x509.log') 
dataw = lcount('wikipedia','/usr/local/bro/logs/current/x509.log')

#sum them
data = datat+dataf+dataw

print data #to see the number itself, could be removed
      

def onOffFunction():
  #command = raw_input("Type something..: (blue/ red / green / bye )");
  if (data < 3):
    print "LED BLUE" #if there're less than 3, led blue
    time.sleep(1)
    arduino.write('B')
    onOffFunction()

  elif (data >= 3):
    print "RED LED" #if there are more than 3 or three, led red
    time.sleep(1)
    arduino.write('Y') #off the rest colors
    arduino.write('R')
    onOffFunction()
#add more options

time.sleep(2) #waiting the initialization...
onOffFunction()
