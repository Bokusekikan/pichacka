import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

led1=11
led2=15
button1=29
button2=37

#LED setup
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.output(led1,False)
GPIO.output(led2,False)

#Button setup
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
    while True:
        if GPIO.input(button1)==0:
            print("Button 1 was pressed")
            GPIO.output(led1,True)
            #sleep(2)
            #GPIO.output(led1,False)
        if GPIO.input(button2)==0:
            print("Button 2 was pressed")
            GPIO.output(led2,True)
            #sleep(2)
            #GPIO.output(led2,False)
        sleep(2)
        GPIO.output(led1,False)
        GPIO.output(led2,False)

except KeyboardInterrupt:
    GPIO.cleanup()
