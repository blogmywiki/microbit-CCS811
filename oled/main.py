# Adapted from https://github.com/Notthemarsian/CCS811/ for BBC micro:bit

from microbit import *
import time
import CCS811
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

def main():
    # Adafruit sensor breakout has i2c addr: 90; Sparkfun: 91
    s = CCS811.CCS811(addr=90)
    time.sleep(1)
    while True:
        if s.data_ready():
            print('eCO2:%d' % (s.eCO2))
            print('TVOC:%d' % (s.tVOC))
            add_text(0,0,'eCO2: %d       ' % s.eCO2)     
            add_text(0,2,'TVOC: %d       ' % s.tVOC)     
            time.sleep(1)
initialize()
clear_oled()
add_text(9,1,'ppm')
add_text(9,3,'ppb')
main()
