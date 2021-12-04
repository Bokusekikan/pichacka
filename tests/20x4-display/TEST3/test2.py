#! /usr/bin/env python

# Import necessary libraries for communication and display use
import drivers
from datetime import datetime
from time import sleep


def disp_setup():
    display = drivers.Lcd()
    cc = drivers.CustomCharacters(display)
    cc.char_1_data = ["00000",
                      "00000",
                      "11111",
                      "11111",
                      "01110",
                      "01110",
                      "00100",
                      "00000"]
    cc.load_custom_characters_data()


def disp_default():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    current_date = now.strftime("%d/%m/%Y")
    current_td = current_time + "     " + current_date 
    display.lcd_display_string(current_td, 1)  # Write line of text to first line of display
    display.lcd_display_string(" Prichod     Odchod ", 3)
    display.lcd_display_extended_string("     {0x00}        {0x00}     ", 4)  # Write line of text to second line of display
    sleep(5) # Give time for the message to be read

def full_disp():
    display = drivers.Lcd()
    cc = drivers.CustomCharacters(display)
    cc.char_1_data = ["00000",
                      "00000",
                      "11111",
                      "11111",
                      "01110",
                      "01110",
                      "00100",
                      "00000"]
    cc.load_custom_characters_data()
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    current_date = now.strftime("%d/%m/%Y")
    current_td = current_time + "     " + current_date 
    display.lcd_display_string(current_td, 1)  # Write line of text to first line of display
    display.lcd_display_string(" Prichod     Odchod ", 3)
    display.lcd_display_extended_string("     {0x00}        {0x00}     ", 4)  # Write line of text to second line of display
    sleep(5) # Give time for the message to be read
    return display



if __name__ == '__main__':
    print("fuck you")
    #disp_setup()
    try:
        while True:
            #disp_default()
            full_disp()
    
    except KeyboardInterrupt:
        print("Cleaning up!")
        display.lcd_clear()
