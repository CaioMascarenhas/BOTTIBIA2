import pyautogui as pg
import time
import keyboard

pg.useImageNotFoundException(False)

REGION_SSA_NO_HOTKEY=(730,886,37,25)
REGION_SSA_NO_PESCOCO=(1749,155,39,23)
REGION_MIGHT_NO_HOTKEY=(766,887,36,24)
REGION_MIGHT_NO_DEDO=(1750,227,37,23)

paused = True

def toggle_pause():
    global paused
    paused = not paused
    print("Automatização pausada" if paused else "Automatização retomada")

keyboard.add_hotkey('ctrl+shift+p', toggle_pause)  # Define 'ctrl+shift+p' como tecla para pausar/despausar

def autoSSAMight():
    print('Iniciando!, precisone cntrl + shift + p . para iniciar e também para pausar a qualquer momento')
    while True:
        if not paused:
            if pg.locateOnScreen('ssamight_img/ssa_no_f11.png', region=REGION_SSA_NO_HOTKEY, confidence=0.9):
                if pg.locateOnScreen('ssamight_img/SSA_NO_PESCOCO.png', region=REGION_SSA_NO_PESCOCO, confidence=0.9):
                    continue
                else:
                    keyboard.press('F11')
                    print('Colocando SSA, IMPOSSIVEL MORRER PORRA!!')
            if pg.locateOnScreen('ssamight_img/might_no_f12.png', region=REGION_MIGHT_NO_HOTKEY, confidence=0.9):
                if pg.locateOnScreen('ssamight_img/MIGHT_NO_DEDO.png', region=REGION_MIGHT_NO_DEDO, confidence=0.9):
                    continue
                else:
                    keyboard.press('F12')
                    print('Colocando MIGHT RING, TANKA CARALHO!!')
        time.sleep(0.1)

autoSSAMight()
