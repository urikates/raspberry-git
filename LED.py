import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BORAD)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,True)
time.sleep(5)
GPIO.output(7,0)
time.sleep(5)
GPIO.cleanup(7)
