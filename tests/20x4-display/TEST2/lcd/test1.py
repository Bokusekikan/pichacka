#! /usr/bin/env python

# Import necessary libraries for communication and display use
import drivers
from datetime import datetime
from time import sleep

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()

# Create object with custom characters data
cc = drivers.CustomCharacters(display)

# Redefine the default characters:
# Custom caracter #1. Code {0x00}.
cc.char_1_data = ["00000",
                  "00000",
                  "11111",
                  "11111",
                  "01110",
                  "01110",
                  "00100",
                  "00000"]

# Load custom characters data to CG RAM:
cc.load_custom_characters_data()


# Main body of code
try:
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_date = now.strftime("%d/%m/%Y")
        current_td = current_time + "     " + current_date 
        display.lcd_display_string(current_td, 1)  # Write line of text to first line of display
        display.lcd_display_string(" Prichod     Odchod ", 3)
        display.lcd_display_extended_string("     {0x00}        {0x00}     ", 4)  # Write line of text to second line of display
        sleep(5) # Give time for the message to be read
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
