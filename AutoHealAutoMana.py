import pyautogui as pg
import time
import constants

#f3 magia cura
#f4 pot mana
#f8 pot vida

def Auto():
    
    while True:
        if pg.pixelMatchesColor(*constants.POSITION_LEFT_LIFE, constants.COLOR_MEIOGREEN_LIFE):  #cor verde
            pg.press('F3')
            time.sleep(0.05)
            if pg.pixelMatchesColor(*constants.POSITION_MANA, constants.COLOR_MANA_AUSENTE) == True:
                pg.press('F4')
                time.sleep(0.05)
            pg.press('F3')
            print('Curando no verde')
            pg.sleep(1)
            
        elif pg.pixelMatchesColor(*constants.POSITION_LEFT_LIFE, constants.COLOR_YELLOW_LIFE):  #cor amarelo
            pg.press('F3')
            time.sleep(0.05)
            pg.press('F8')
            if pg.pixelMatchesColor(*constants.POSITION_MANA, constants.COLOR_MANA_AUSENTE) == True:
                pg.press('F4')
                time.sleep(0.05)
            pg.press('F3')
            print('Curando no verde')
            pg.press('F8')
            pg.sleep(1)

        elif pg.pixelMatchesColor(*constants.POSITION_LEFT_LIFE, constants.COLOR_RED_LIFE):  #cor vermeio
            pg.press('F3')
            time.sleep(0.05)
            pg.press('F8')
            if pg.pixelMatchesColor(*constants.POSITION_MANA, constants.COLOR_MANA_AUSENTE) == True:
                pg.press('F4')
                time.sleep(0.05)
            pg.press('F3')
            print('Curando no verde')
            pg.press('F8')
            pg.sleep(1)
            
        elif pg.pixelMatchesColor(*constants.POSITION_LEFT_LIFE, constants.COLOR_RED_LIFE):  #cor vermeio
            pg.press('F3')
            time.sleep(0.05)
            pg.press('F8')
            if pg.pixelMatchesColor(*constants.POSITION_MANA, constants.COLOR_MANA_AUSENTE) == True:
                pg.press('F4')
                time.sleep(0.05)
            pg.press('F3')
            print('Curando no verde')
            pg.press('F8')
            pg.sleep(1)
        
        else:
            if pg.pixelMatchesColor(*constants.POSITION_MANA, constants.COLOR_MANA_AUSENTE) == True:
                pg.press('F4')
                time.sleep(1)
        

Auto()

