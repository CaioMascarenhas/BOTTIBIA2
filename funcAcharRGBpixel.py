import pyautogui as pg
import time

def get_pixel_color(x, y):
    return pg.pixel(x, y)

# Exemplo de uso:
x = 1223
y = 32
while True:
    color = get_pixel_color(x, y)
    print(f'A cor do pixel em ({x}, {y}) é: {color}')
    time.sleep(1)
    