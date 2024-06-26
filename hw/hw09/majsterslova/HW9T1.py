import pygame
import random
import sys
from random import randint 

pygame.init()
pygame.font.init()

gameDisplay = pygame.display.set_mode((500,300))
pygame.display.set_caption('Guess the number from "0" to "100"')
clock = pygame.time.Clock()
INPUT_BOX_WIDTH = 200
INPUT_BOX_HEIGHT = 70
DONE = False
COLOR = (0, 0, 128)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE =(255, 255, 255)
last_message_font_size = 15
font_size = 60
random_number = random.randint(1, 100)


input_string = ""
last_message = ""
last_message = "I'm thinking of a number between 1 and 100."
attempts = 0
MAX_ATTEMPTS = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                user_guess = int(input_string)
                attempts += 1
                
                if user_guess < random_number:
                    last_message = "Too low! Try again."
                elif user_guess > random_number:
                    last_message = "Too high! Try again."
                elif user_guess == random_number:
                    last_message = "Win! You guessed the number in {} attempts.".format(attempts)
                else:
                    last_message = "Sorry, you didn't guess the number. It was {}.".format(random_number)
                
                if attempts >= MAX_ATTEMPTS:
                    last_message = "You've used all your attempts. The number was {}.".format(random_number)
                    pygame.time.wait(3000)  
                    
            elif event.key == pygame.K_BACKSPACE:
                input_string = input_string[:-1]
            elif event.unicode.isdigit():
                input_string += event.unicode

    gameDisplay.fill(COLOR)
    font_size = 60  
    last_message_font_size = 30
    input_box = pygame.Rect((gameDisplay.get_width() - INPUT_BOX_WIDTH) // 2, (gameDisplay.get_height() - INPUT_BOX_HEIGHT) // 2, INPUT_BOX_WIDTH, INPUT_BOX_HEIGHT)
    pygame.draw.rect(gameDisplay, YELLOW, input_box)
    font = pygame.font.Font(None, font_size)
    last_message_font = pygame.font.Font(None, last_message_font_size)
    text_surface = font.render(input_string, True, BLACK)
    text_rect = text_surface.get_rect(center=input_box.center)
    gameDisplay.blit(text_surface, text_rect)

    last_message_surface = last_message_font.render(last_message, True, WHITE)
    gameDisplay.blit(last_message_surface, ((gameDisplay.get_width() - last_message_surface.get_width()) // 2, input_box.y - 50))


    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()
sys.exit()
    
    

