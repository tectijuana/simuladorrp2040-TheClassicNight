#Espinoza Castillo Alejandro
#Cada vez que presionas el boton se prende el led

from machine import Pin
import utime

#Espinoza Castillo Alejandro
#Si se presiona el boton o esta activado el switch el led se prende

led = Pin(16,Pin.OUT)

button = Pin(15,Pin.IN)

while True:
  if button.value()==1:
    led.toggle()
    utime.sleep(0.2)
