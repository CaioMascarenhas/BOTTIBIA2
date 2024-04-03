import pyautogui as pg
import actions
import constants


#script to hunt wasps cave in ab'dendriel, using the flags described in the photos as a way to click, this script does not heal os use spells, only basic hits and uses healling spells if
# your mana is full, watch that hotkeys used during hunting are fixed as seem in the code below, since monster are weak, no other complex actions are required...


def hunt_pirat():
    #while True:
    actions.check_battle()
    pg.scroll(100)
    actions.goto('rot_lb_img/check.png',5)
    actions.eat_food()

    pg.scroll(100)
    actions.goto('rot_lb_img/interrog.png',7)
    actions.eat_food()

    pg.scroll(100)
    actions.goto('rot_lb_img/exclamacao.png',9)
    actions.eat_food()


    pg.scroll(100)
    actions.goto('rot_lb_img/star.png',8)
    actions.eat_food()

    pg.scroll(100)
    actions.goto('rot_lb_img/x.png',16)
    actions.eat_food()

    pg.scroll(100)
    actions.goto('rot_lb_img/igreja.png',16)
    actions.eat_food()
    
    # actions.goto('rot_lb_img/boca.png')
    # actions.eat_food()

    # actions.goto('rot_lb_img/espadavermeia.png')
    # actions.eat_food()

    # actions.goto('rot_lb_img/espadanormal.png')
    # actions.eat_food()

    # actions.goto('rot_lb_img/bandeiraazul.png')
    # actions.eat_food()

    # actions.goto('rot_lb_img/cadeado.png')
    # actions.eat_food()

    # actions.goto('rot_lb_img/bolsa.png')
    # actions.eat_food()

    # actions.goto('rot_lb_img/caveira.png')
    # actions.eat_food()
    pg.scroll(100)
    actions.goto('rot_lb_img/check.png',18)
    actions.eat_food()

