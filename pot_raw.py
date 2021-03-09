#leyendo voltaje entre 0 y 3.3 Volts
import machine
import utime

pot = machine.ADC(27)

while True:
    print (pot.read_u16())
    utime.sleep(2)