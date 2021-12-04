import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
from datetime import datetime

GPIO.setmode(GPIO.BOARD)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#LED setup
led1 = 11
led2 = 15
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.output(led1,False)
GPIO.output(led2,False)

#Button setup
button1 = 29
button2 = 37
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

B1 = False
B2 = False

#Reader setup
reader = SimpleMFRC522()

def prichodOdchod(button, led, prichod_odchod, timeout):
    print()
    GPIO.output(led,TRUE)
    id, _ = reader.read()
    print(id)
    print("shit")


    if GPIO.input(button) == 0:
        GPIO.outpu(led,True)
        id, _ = reader.read()
        print(id)
        if prichod_odchod == 0:
            print("shit")

try:
    while True:
        if GPIO.input(button1) == 0:
            print("Button 1 was pressed")
            print("Prilozte kartu")
            print("====================")
            GPIO.output(led1,True)
            for i in range(100):
                id, _ = reader.read()
                if id == "":
                    continue
                else:
                    print(id)
                    text="Příchod v "
                    print(text, current_time)
                    GPIO.output(led1,False)
                    break
                sleep(0.1)
            if id == "":
                print("Karta nebyla prilozena")
                GPIO.output(led1,False)
        if GPIO.input(button2) == 0:
            print("Button 2 was pressed")
            GPIO.output(led2,True)
            id, _ = reader.read()
            print(id)
            text="Odchod v "
            print(text, current_time)
            sleep(5)
        id = ""
        sleep(0.1)
        #sleep(0.5)
        #id, text = reader.read()
        #print(id)
        #print(text)

finally:
        GPIO.cleanup()
