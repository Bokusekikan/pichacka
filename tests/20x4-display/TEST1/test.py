from rpi_lcd import LCD
from time import sleep
from datetime import datetime


lcd = LCD()

lcd.text('Raspberry Pi', 2)
lcd.text(' Prichod     Odchod ', 3, 'center')
#lcd.text('Odchod', 3, 'right')
lcd.text(' D                D ', 4, 'center')
lcd.write()
#lcd.text('▼', 3, 'left')
#lcd.text('↑', 3, 'left')

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    lcd.text(current_time, 1)
    sleep(1)
    #lcd.clear()
