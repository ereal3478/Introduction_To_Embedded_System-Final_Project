from rpi_lcd import LCD

def LCDDisplay(color):
    lcd = LCD()
    lcd.backlight(0x08)
    lcd.text(color, 0)
