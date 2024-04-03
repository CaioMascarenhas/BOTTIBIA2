import pyautogui as pg
import time
import constants
pg.useImageNotFoundException(False)


def check_battle():
    return pg.locateOnScreen('imgs/region_battle.png', region=constants.REGION_BATTLE)

def kill_monster():
    while True:
        if pg.locateOnScreen('imgs/region_battle.png', confidence=0.8, region=constants.REGION_BATTLE) or pg.locateOnScreen('imgs/region_battle2.png', confidence=0.9, region=constants.REGION_BATTLE):
            break
        is_battle = check_battle()
        if is_battle == None:
            pg.press('space')
            # battleKnight()
            while pg.locateOnScreen('imgs/battle_red.png',confidence=0.7, region=constants.REGION_BATTLE) !=None or pg.locateOnScreen('imgs/battle_red2.png', confidence=0.7, region=constants.REGION_BATTLE) !=None:
                if pg.locateOnScreen('imgs/region_battle.png', region=constants.REGION_BATTLE, confidence=0.9) or pg.locateOnScreen('imgs/region_battle2.png', region=constants.REGION_BATTLE, confidence=0.9):
                    # pg.sleep(1)
                    break
                print('esperando o monstro morrer')
                # battleKnight()
            # time.sleep(1)
            print('procurando outro monstro')
        print(is_battle)
    pg.scroll(150)



def check_status(name,delay,x,y,rgb,button_name):
    print(f'checkando {name}...')
    pg.sleep(delay)
    if pg.pixelMatchesColor(x,y, rgb):
        pg.press(button_name)


def eat_food():
    pg.press('F5')
    print('comendo comida...')



def hole_down():
    box = pg.locateOnScreen('imgs/hole_down.png', confidence=0.8)
    if box:
        x,y = pg.center(box)
        pg.moveTo(x,y)
        pg.click()
        pg.sleep(5)
        kill_monster()



def hole_up(img_anchor, plus_X,plus_Y):
    box = pg.locateOnScreen(img_anchor, confidence=0.8)
    if box:
        x,y = pg.center(box)
        pg.moveTo(x + plus_X, y + plus_Y)
        pg.press('F6')
        pg.click()
        time.sleep(5)
        kill_monster()
        



def goto(img,delay=7):
    if img:
        imagem = img
        vai = pg.locateOnScreen(img, confidence=0.8,region=constants.REGION_MINIMAP)
        if vai is None:
            print('nao consegui achar o local')
        if vai is not None:
            x, y = pg.center(vai)
            pg.moveTo(x, y)
            pg.click()
            pg.moveTo(300,500)
            pg.sleep(delay)
            kill_monster()
            if pg.locateOnScreen('imgs/fotobase.png',confidence=0.9, region=constants.REGION_MINIMAP) != None or pg.locateOnScreen('imgs/fotobaseh.png',confidence=0.9, region=constants.REGION_MINIMAP):
                print('nao chegou ainda no local!!')
                kill_monster()
                print('indo ao local!')
                goto(imagem)
        

def battleKnight():
    if (pg.locateOnScreen('imgs/exori.png',confidence=0.8, region=constants.REGION_EXORI)):
        pg.press('F7')
        print('dando exori')
        return
    
    elif (pg.locateOnScreen('imgs/exoriico.png', confidence=0.7, region=constants.REGION_EXORI_ICO)):
        pg.press('F6')
        print('dando exori ico')
        return
    
    else:
        print('nao usando nada')
        return
    
            
