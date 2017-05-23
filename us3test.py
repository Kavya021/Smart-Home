import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
import urllib2

TRIG = 23                                  #Associate pin 23 to TRIG
ECHO = 24                                  #Associate pin 24 to ECHO
TRIG2 = 17 
ECHO2 = 27
TRIG3 = 22 
ECHO3 = 25


print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in
GPIO.setup(TRIG2,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO2,GPIO.IN)                   #Set pin as GPIO in
GPIO.setup(TRIG3,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO3,GPIO.IN)                   #Set pin as GPIO in

while True:
  #Egg
  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  print "Waitng For Sensor To Settle"
  time.sleep(1)                            #Delay of 1 seconds

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance > 2 and distance < 20:      #Check whether the distance is within range
    print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
    flag = 1
  else:
    while(flag):
      print "Egg Is Empty"  
      #urllib2.urlopen('http://iothome.esy.es/indexsms.php')
      urllib2.urlopen('http://iothome.esy.es/info.php?message=egg')
      flag = 0
      #GPIO.cleanup()

  #Bootle
  GPIO.output(TRIG2, False)                 #Set TRIG as LOW
  print "Waitng For Sensor To Settle"
  time.sleep(1)                            #Delay of 1 seconds

  GPIO.output(TRIG2, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG2, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO2)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO2)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance > 2 and distance < 20:      #Check whether the distance is within range
    print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
    send = 1
  else:
    while(send == 1):
       print "Bottle Is Empty"  
       #urllib2.urlopen('http://iothome.esy.es/indexsms.php')
       urllib2.urlopen('http://iothome.esy.es/info.php?message=bottle')
       send = 0
       #GPIO.cleanup()

  #Door
  GPIO.output(TRIG3, False)                 #Set TRIG as LOW
  print "Waitng For Sensor To Settle"
  time.sleep(1)                            #Delay of 1 seconds

  GPIO.output(TRIG3, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG3, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO3)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO3)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance > 2 and distance < 20:      #Check whether the distance is within range
    print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
    door = 1
  else:
    while(door == 1):
       print "Door Is Open"  
       urllib2.urlopen('http://iothome.esy.es/door.php')
       door = 0
       #GPIO.cleanup()
GPIO.cleanup()
