from machine import Pin
import time

led=Pin(25, Pin.OUT)

while True:
    led.value(1)
    print('a')
    time.sleep(1)
    led.value(0)
    print('b')
    time.sleep(1)