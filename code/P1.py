from machine import Pin
import utime

led = Pin(16,Pin.OUT)

button = Pin(15,Pin.IN)

while True:
  if button.value()==1:
    led.toggle()
    utime.sleep(0.2)