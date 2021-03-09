#medidor de temperatura
import machine
import utime

sensor_temp_int = machine.ADC(4)

factor = 3.3 / (65535)

while True:
    lectura = sensor_temp_int.read_u16() * factor
    tempC = 27 - (lectura - 0.706)/0.001721
    print (round(tempC,2))
    utime.sleep(2)