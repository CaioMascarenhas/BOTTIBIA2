import pyautogui as pg
import keyboard  
import wasp_script
import pirat_script_lb
import threading
import time
import rot_lb_script

def main():
    print('Welcome to tibia bot! choose the specified script you wanna use!.')
    print('rot_lb_script = 1')
    print('pirat_script_lb = 2')

    script = int(input())

    if script == 1:
        print('digite a letra: h para começar!.')
        keyboard.wait('h')
        while True:
            rot_lb_script.hunt_rot()
            time.sleep(1)

    if script == 2:
        print('digite a letra: h para começar!.')
        keyboard.wait('h')
        while True:
            pirat_script_lb.hunt_pirat()
            time.sleep(1)
        

# def stop():
#    global parada
#    parada = True
#    while True:
#         if keyboard.is_pressed('p'):
#             parada = not parada
#             print('Parando execução do script')
#             break
#         time.sleep(1)

# thread_stop = threading.Thread(target=stop)

# thread_stop.start()

main()

# thread_stop.join()