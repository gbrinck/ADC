#leyendo voltaje entre 0 y 3.3 Volts
import machine
import utime

pot = machine.ADC(27)
factor = 3.3/ (65535)

while True:
    voltaje = pot.read_u16() * factor
    print (round(voltaje,2))    
    utime.sleep(2)