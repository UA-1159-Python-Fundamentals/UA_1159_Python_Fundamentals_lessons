import pygame
from random import randint

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

display = pygame.display.set_mode((600, 200))
clock = pygame.time.Clock()
font1 = pygame.font.SysFont("Calibri", 17, True)
font2 = pygame.font.SysFont("Calibri", 25, True)
font3 = pygame.font.SysFont("Calibri", 100, True)

current_text = "Hello I create a number, guess it!"
user_number = ''
randomed = randint(1, 100)
attempt = 0

pygame.display.set_caption("The beautiful guesser")


program = True
while program:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.unicode in "0123456789" and len(user_number) < 2 :
                user_number += event.unicode
            elif event.unicode == "\x08":
                user_number = user_number[:-1]
            elif event.unicode == "\r" and len(user_number) > 0:
                if attempt == 10:
                    current_text = f"Sorry you lose.... it was {str(randomed)}"
                    break
                if user_number == str(randomed):
                    current_text = f"Beautiful!!! Correct number is {str(randomed)}"
                    randomed = randint(1, 100)
                    attempt = 0
                elif int(user_number) < randomed:
                    current_text = "Yor number is less:("
                elif int(user_number) > randomed:
                    current_text = "Yor number bigger1:("
                attempt += 1
                    
        elif event.type == pygame.QUIT:
            quit()


    display.fill(BLACK)

    text1 = font1.render(">>>enter number and press enter", True, WHITE)
    text2 = font2.render(current_text, True, WHITE)
    number = font3.render(user_number, True, WHITE)

    display.blit(text1, [10, 10])
    display.blit(text2, [10, 40])
    display.blit(number, [10, 70])
    
    pygame.display.update()
    clock.tick(60)