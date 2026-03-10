import pygame
import random


def update_ca(state, rule, border_val='0'):
    new_state = [border_val]
    for num in range(1, len(state)-1):
        new_state.append(rule[''.join(state[num-1:num+2])])
    new_state.append(border_val)
    return new_state

def draw_ca(screen, state):
    for raw_ind, raw in enumerate(state):
        for col_ind, el in enumerate(raw):
            pygame.draw.rect(screen, (BLACK if el=='1' else WHITE), (cell_width*raw_ind, cell_height*col_ind, cell_width, cell_height))

WIDTH = 640
HEIGHT = 480
FPS = 30


# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cellular automaton")
clock = pygame.time.Clock()


# Теперь то, что нужно непосредственно для клеточного автомата
# Сюда мы будем закидывать ВСЕ состояния
#(автомат одномерный, а мы работаем в 2D - почему бы этим не воспользоваться ;))

X, Y = 100, 100
cell_width = WIDTH/X
cell_height = HEIGHT/Y
##rule = {'000': '0', '001': '1', '010': '1', '011': '1', '100': '1', '101': '0', '110': '0', '111': '0'}
rule = {'000': '1', '001': '0', '010': '0', '011': '0', '100': '0', '101': '1', '110': '0', '111': '1'}
States = [['1' if i==X//2 else '0' for i in range(X)]]
for i in range(Y):
    States.append(update_ca(States[-1], rule, '1'))

draw_ca(screen, States)
pygame.display.update()
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
##    screen.fill(WHITE)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
##    pygame.display.update()

pygame.quit()
