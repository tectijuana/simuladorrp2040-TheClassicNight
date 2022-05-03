#Espinoza Castillo Alejandro
#Muestra en la consola la medicion de los 2 potenciometros

import machine
import utime

pot=machine.ADC(28)

while True:
  value=pot.read_u16()
  print(value)
  utime.sleep_ms(200)