#Espinoza Castillo Alejandro
#Muestra en la consola la medicion del sensor de ultrasonido y una variacion de colores en el led rgb 

from machine import Pin
import utime
 
red = Pin(16, Pin.OUT)
green = Pin(18, Pin.OUT)
blue = Pin(20, Pin.OUT)

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()

   while echo.value() == 0:
       signaloff = utime.ticks_us()

   while echo.value() == 1:
       signalon = utime.ticks_us()
       
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   print("La Distancia del Objeto es ",distance,"cm")

while True:
   ultra()
   utime.sleep(1)

while True:
    red.value(1)
    green.value(1)
    blue.value(1)
    utime.sleep(1)
 
    red.value(0)
    green.value(1)
    blue.value(1)
    utime.sleep(1)
 
    red.value(1)
    green.value(0)
    blue.value(1)    
    utime.sleep(1)
 
    red.value(1)
    green.value(1)
    blue.value(0)
    utime.sleep(1)