from machine import ADC, Pin
from time import sleep

# Espinoza Castillo Alejandro
# Muestra en la consola cuanta luz se proyecta en el ldr

photoPIN = 26

def readLight(photoGP):
    photoRes = ADC(Pin(26))
    light = photoRes.read_u16()
    light = round(light/65535*100,2)
    return light

while True:
    print("light: " + str(readLight(photoPIN)) +"%")
    sleep(1) # set a delay between readings

