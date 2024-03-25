import pygame

FPS = 60

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

COORD_X=50
COORD_Y=50
WIDTH_RECTANGLE=50
HEIGHT_RECTANGLE=50
DELTA_STEP=10

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()


gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")


run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
                run = False
        key = event.dict.get("key")

        if key==1073741904 and COORD_X > 0: #1073741904 ключ кнопки вліво
            COORD_X = COORD_X-DELTA_STEP
        if key==1073741903 and COORD_X < WIDTH_DISPLAY - WIDTH_RECTANGLE: # 1073741903 ключ кнопки вправо
            COORD_X = COORD_X+DELTA_STEP
        if key==1073741906 and COORD_Y > 0:
            COORD_Y = COORD_Y-DELTA_STEP #1073741906 ключ кнопки вверх
        if key==1073741905 and COORD_Y < HEIGHT_DISPLAY - HEIGHT_RECTANGLE: #1073741905 ключ кнопки вниз
            COORD_Y = COORD_Y+DELTA_STEP


    gameDisplay.fill(BLACK_COLOR)

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
                                              COORD_Y,
                                              WIDTH_RECTANGLE,
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)


