from pynput.mouse import Button, Controller
import time

mouse = Controller()

# Pressiona o botão do scroll
mouse.click(Button.middle, 1)  # O segundo argumento (1) representa o número de cliques, que é 1 neste caso

# Aguarde um curto período de tempo (por exemplo, 0,1 segundo) se necessário
time.sleep(0.1)