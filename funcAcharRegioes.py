import pyautogui as pg
import time

def check_battle():
    return pg.locateOnScreen('ssamight_img/MIGHT_NO_DEDO.png', confidence=0.9)

while True:
    try:
        is_battle = check_battle()
        if is_battle is not None:
            print(is_battle)
        else:
            print('Não achei')
    except pg.ImageNotFoundException:
        print('Não achei')
    time.sleep(1)  # Adicione um pequeno intervalo de tempo entre as tentativas para não sobrecarregar o sistema



