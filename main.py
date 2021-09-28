# Adapted from https://github.com/Notthemarsian/CCS811/ for BBC micro:bit

from microbit import *
#from machine import Pin, I2C
import time
import CCS811

def main():
#    i2c = I2C(scl=Pin(5), sda=Pin(4))
    # Adafruit sensor breakout has i2c addr: 90; Sparkfun: 91
    s = CCS811.CCS811(addr=90)
    time.sleep(1)
    while True:
        if s.data_ready():
            print('eCO2:%d' % (s.eCO2))
            print('TVOC:%d' % (s.tVOC))
            time.sleep(1)

main()
