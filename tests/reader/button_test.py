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

B1=False
B2=False


try:
    while True:
        if GPIO.input(button1)==0:
            #print "Button 1 was pressed"
            if B1==False:
                GPIO.output(led1,True)
                B1=True
                print("Button 1 was pressed (OFF->ON)")
                #sleep(0.5)
            else:
                GPIO.output(led1,False)
                B1=False
                print("Button 1 was pressed (ON->OFF)")
                #sleep(0.5)
        if GPIO.input(button2)==0:
            #print "Button 2 was pressed"
            if B2==False:
                GPIO.output(led2,True)
                B2=True
                print("Button 2 was pressed (OFF->ON)")
                #sleep(0.5)
            else:
                GPIO.output(led2,False)
                B2=False
                print("Button 2 was pressed (ON->OFF)")
                #sleep(0.5)
        sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
