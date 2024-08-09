from machine import Pin, ADC, PWM
from time import sleep

led=PWM(Pin(25))
led.freq(1000)

potentiometer=ADC(28)

while True:
  potentiometer_value=potentiometer.read_u16()
  print(potentiometer_value)
  led.duty_u16(potentiometer_value)
  sleep(0.25)
