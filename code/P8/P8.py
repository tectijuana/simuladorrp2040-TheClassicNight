from machine import Pin
from time import sleep_ms
from lcd import LCD

figura_1 = (0x0A,0x0A,0x0A,0x00,0x11,0x11,0x0E,0x00)
figura_2 = (0x0A,0x0A,0x0A,0x00,0x0E,0x11,0x11,0x00)
figura_3 = (0x00,0x0A,0x1F,0x1F,0x1F,0x0E,0x04,0x00)
figura_4 = (0x04,0x11,0x0E,0x04,0x04,0x0A,0x11,0x00)
figura_5 = (0x04,0x0E,0x1F,0x04,0x04,0x04,0x04,0x00)
figura_6 = (0x0E,0x0A,0x11,0x11,0x11,0x1F,0x1F,0x00)
figura_7 = (0x04,0x0E,0x04,0x04,0x15,0x15,0x0E,0x00)
figura_8 = (0x1F,0x11,0x0A,0x04,0x0A,0x11,0x1F,0x00)

lcd = LCD(0,1,2,3,4,5)                          # RS, E, D4, D5, D6, D7
lcd.cgram_init()                                # Accede a la CGRAM para guardar caracteres especiales
lcd.cgram_create_char(0, figura_1)              # Guarda los caracteres especiales en las posiciones 0 a 7 de la CGRAM
lcd.cgram_create_char(1, figura_2)
lcd.cgram_create_char(2, figura_3)
lcd.cgram_create_char(3, figura_4)
lcd.cgram_create_char(4, figura_5)
lcd.cgram_create_char(5, figura_6)
lcd.cgram_create_char(6, figura_7)
lcd.cgram_create_char(7, figura_8)
lcd.cgram_close()                               # Sale de la CGRAM
lcd.clear()                                     # Limpia la pantalla LCD

while True:
    lcd.move_to(4,0)
    lcd.putstr("LCD 16x2")
    lcd.move_to(3,1)
    lcd.putstr("Modo 4 Bits")
    lcd.blink()
    sleep_ms(3000)
    lcd.no_blink()
    lcd.clear()
    sleep_ms(200)
    
    lcd.move_to(0,0)
    lcd.putstr("Hola Que Tal")
    sleep_ms(1000)
    lcd.move_to(0,1)
    lcd.putstr("Excelente Dia")
    sleep_ms(2000)
    lcd.clear()
    sleep_ms(200)
    
    lcd.move_to(0,0)
    lcd.putstr("Electronica")
    lcd.move_to(0,1)
    lcd.putstr("y Circuitos")
    sleep_ms(1000)
    for x in range(15):
        lcd.shift_right()
        sleep_ms(300)
    for x in range(15):
        lcd.shift_left()
        sleep_ms(300)
    sleep_ms(500)
    lcd.clear()
    sleep_ms(200)
    
    lcd.move_to(0,0)
    lcd.putstr("CGRAM Characters")
    lcd.move_to(0,1)
    lcd.cgram_putc(0)
    lcd.move_to(2,1)
    lcd.cgram_putc(1)
    lcd.move_to(4,1)
    lcd.cgram_putc(2)
    lcd.move_to(6,1)
    lcd.cgram_putc(3)
    lcd.move_to(8,1)
    lcd.cgram_putc(4)
    lcd.move_to(10,1)
    lcd.cgram_putc(5)
    lcd.move_to(12,1)
    lcd.cgram_putc(6)
    lcd.move_to(14,1)
    lcd.cgram_putc(7)
    sleep_ms(3000)
    lcd.clear()
    sleep_ms(200)
    
    lcd.move_to(4,0)
    lcd.putstr("Contador")
    lcd.move_to(4,1)
    lcd.putstr("V: ")
    for x in range(101):
        lcd.move_to(7,1)
        lcd.putstr(str(x))
        sleep_ms(150)
    sleep_ms(2000)
    lcd.clear()
    sleep_ms(4000)