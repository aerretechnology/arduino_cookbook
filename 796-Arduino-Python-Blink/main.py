from machine import Pin
import time 

#pin fisico 10 = pin python 21
pin = Pin(21, Pin.OUT)

while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(1)
