import pyautogui as pg
import actions
import constants


#script to hunt wasps cave in ab'dendriel, using the flags described in the photos as a way to click, this script does not heal os use spells, only basic hits and uses healling spells if
# your mana is full, watch that hotkeys used during hunting are fixed as seem in the code below, since monster are weak, no other complex actions are required...
# F1 TO HEALLING SPELLS
# F6 TO ROPE
# F5 TO EAT FOOD

def hunt_rot():
    #while True:
    actions.check_battle()

    actions.goto('rot_lb_img/check.png')
    actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
    actions.eat_food()

    actions.goto('rot_lb_img/interrog.png')
    actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
    actions.eat_food()

    actions.goto('rot_lb_img/exclamacao.png')
    actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
    actions.eat_food()


    actions.goto('rot_lb_img/star.png')
    actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
    actions.eat_food()

    actions.goto('rot_lb_img/x.png')
    actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
    actions.eat_food()

    actions.goto('rot_lb_img/igreja.png')
    actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
    actions.eat_food()
    
    actions.goto('rot_lb_img/boca.png')
    actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
    actions.eat_food()

    actions.goto('rot_lb_img/espadavermeia.png')
    actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
    actions.eat_food()

    actions.goto('rot_lb_img/espadanormal.png')
    actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
    actions.eat_food()

    actions.goto('rot_lb_img/bandeiraazul.png')
    actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
    actions.eat_food()

    actions.goto('rot_lb_img/cadeado.png')
    actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
    actions.eat_food()

    actions.goto('rot_lb_img/bolsa.png')
    actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
    actions.eat_food()

    actions.goto('rot_lb_img/caveira.png')
    actions.check_status('mana',1,*constants.POSITION_MANA_FULL,(0,54,119),'F1')
    actions.eat_food()

