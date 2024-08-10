#!/usr/bin/env python
# encoding: utf-8

import machine
import utime
import urandom
 
r = machine.Pin(15, machine.Pin.OUT)
g = machine.Pin(18, machine.Pin.OUT)
b = machine.Pin(14, machine.Pin.OUT)
 
pwm_r = machine.PWM(r)
pwm_g = machine.PWM(g)
pwm_b = machine.PWM(b)
 
pwm_r.freq(1000)
pwm_g.freq(1000)
pwm_b.freq(1000)
 
def light(red, green, blue):
    pwm_r.duty_u16(65535 - red * 255)
    pwm_g.duty_u16(65535 - green * 255)
    pwm_b.duty_u16(65535 - blue * 255)
 
while True:
    light(urandom.randint(0,250), urandom.randint(0,250), urandom.randint(0,250))
    utime.sleep(0.3)