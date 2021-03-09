#leyendo voltaje entre 0 y 3.3 Volts
from machine import ADC
from utime import sleep

pot = ADC(27)

while True:
    print (pot.read_u16())
    sleep(2)