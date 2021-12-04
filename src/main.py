from mfrc522 import SimpleMFRC522 #card reader library
import RPi.GPIO as GPIO

import drivers #20x4 display library

from time import sleep
from datetime import datetime



def main_loop():
    pass


if __name__ == '__main__':
    try:
        while True:
            main_loop()
            sleep(1)
    except KeyboardInterrupt: 






### Setup ##
#display = drivers.Lcd()
#cc = drivers.CustomCharacters(display)
#cc.char_1_data = ["00000",
#                  "00000",
#                  "11111",
#                  "11111",
#                  "01110",
#                  "01110",
#                  "00100",
#                  "00000"]
#cc.load_custom_characters_data()
#
#
#def idle_display():
#    now = datetime.now()
#    current_time = now.strftime("%H:%M")
#    current_date = now.strftime("%d/%m/%Y")
#    idle_display.current_td = current_time + "     " + current_date 
#    display.lcd_display_string(idle_display.current_td, 1)
#    display.lcd_display_string(" Prichod     Odchod ", 3)
#    display.lcd_display_extended_string("     {0x00}        {0x00}     ", 4)
#
#def display_clear():
#    display.lcd_clear()
