import pygame
import sys
from random import randint

SIZE_BLOCK = 20
COUNT_BLOCK = 30
MARGIN = 1
HEADER_MARGIN = 70

size = [SIZE_BLOCK*COUNT_BLOCK + 2*SIZE_BLOCK + MARGIN*COUNT_BLOCK, 
         SIZE_BLOCK*COUNT_BLOCK + 2*SIZE_BLOCK + MARGIN*COUNT_BLOCK + HEADER_MARGIN]

RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (230, 231, 231)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (147, 149, 152)

pygame.init()
display = pygame.display.set_mode((size))
pygame.display.set_caption("Snake")
time =pygame.time.Clock()
courier = pygame.font.SysFont("courier", 36)

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < COUNT_BLOCK and 0 <= self.y < COUNT_BLOCK
    
    def __eq__(self, other):
        return isinstance(other, Snake) and self.x == other.x and self.y == other.y
    
def get_random_empty_block():
    x = randint(0, COUNT_BLOCK -1)
    y = randint(0, COUNT_BLOCK -1)
    empty_block = Snake(x, y)
    while empty_block in snake_block:
        empty_block.x = randint(0, COUNT_BLOCK -1)
        empty_block.y = randint(0, COUNT_BLOCK -1)
    return empty_block


def draw_block(color, row, column):
    pygame.draw.rect(display, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column+1),
                                      HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row+1),
                                      SIZE_BLOCK, 
                                      SIZE_BLOCK])

snake_block = [Snake(14, 13), Snake(14, 14), Snake(14, 15)]
apple = get_random_empty_block()

total = 0
d_row = buf_row = 0
d_col = buf_col = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:
                buf_row = -1
                buf_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                buf_row = 1
                buf_col = 0
            elif event.key == pygame.K_RIGHT and d_row != 0:
                buf_row = 0
                buf_col = 1
            elif event.key == pygame.K_LEFT and d_row != 0:
                buf_row = 0
                buf_col = -1


    display.fill(BLACK)
    pygame.draw.rect(display, DARK_GRAY, [0, 0, size[0], HEADER_MARGIN])

    text_total = courier.render(f"Total: {total}", 0, WHITE)
    display.blit(text_total, (20, 20))

    for row in range(COUNT_BLOCK):
        for column in range(COUNT_BLOCK):
            if (row + column) % 2 == 0:
                color = GRAY
            else:
                color = WHITE
            draw_block(color, row, column)

    head = snake_block[-1]
    if not head.is_inside():
        print("crash")
        pygame.quit()
        sys.exit()
    
    draw_block(RED, apple.x, apple.y)

    for block in snake_block:
        draw_block(GREEN, block.x, block.y)
        
    pygame.display.flip()
    
    if apple == head:
        total += 1
        snake_block.append(apple)
        apple = get_random_empty_block()

    d_row = buf_row
    d_col = buf_col

    new_head = Snake(head.x + d_row, head.y + d_col)
    
    if new_head in snake_block:
        print("crash yourself")
        pygame.quit()
        sys.exit()
    
    snake_block.append(new_head)
    snake_block.pop(0)

    time.tick(7)

