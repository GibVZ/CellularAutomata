import pygame
import cells

def body_print(body, surf, temp2clr = None):
    if temp2clr is None:
        temp2clr = lambda t: [int(t) * 2, 0, 0]
    w, h = surf.get_size()
    cell_w, cell_h = w/body.SPACEW, h/body.SPACEH
    # print(cell_w, cell_h)
    # print('1\n\n\n\n\n')
    for x in range(body.SPACEW):
        for y in range(body.SPACEH):
            # print(temp2clr(body.space[y][x].temp))
            pygame.draw.rect(surf, temp2clr(body.space[y][x].temp), (x * cell_w, y * cell_h, cell_w, cell_h))


SPACEW = 30
SPACEH = 30
FPS = 90
space = [[None for x in range(SPACEW)] for y in range(SPACEH)]
for y in range(SPACEH):
    for x in range(SPACEW):
        if x * y * (SPACEH - 1 - y) * (SPACEW - 1 - x) == 0:
            space[y][x] = cells.EmptyCell()
        elif (x - 1) * (SPACEW - 2 - x) == 0:
            space[y][x] = cells.ConstCell(temp = 20)
        elif (x - 1) * (y - 1) * (SPACEH - 2 - y) * (SPACEW - 2 - x) == 0:
            space[y][x] = cells.ConstCell(temp = 100)
        else:
            space[y][x] = cells.Cell()
for y in range(SPACEH):
    for x in range(SPACEW):
        if x * y * (SPACEH - 1 - y) * (SPACEW - 1 - x) == 0:
            space[y][x].neighbours = []
        else:
            neighbours = [space[y-1][x], space[y][x-1],
                          space[y+1][x], space[y][x+1]]
            space[y][x].neighbours = neighbours

body = cells.CellBody(SPACEW, SPACEH, space)
W, H = 600, 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W, H))
is_done = False
while not is_done:
    clock.tick(FPS)
    body_print(body, screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_done = True
    pygame.display.update()
    body.update()
pygame.quit()







