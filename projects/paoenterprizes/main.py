import pygame
import random

clock = pygame.time.Clock()
pygame.init()
screen_w = 300
screen_h = 500
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("Game")

bg = pygame.Surface((screen_w,screen_h))



player = pygame.Surface((16,16))
player.fill('Orange')
player_x = 134
player_y = 480
player_speed = 5

enemy_y = 0
enemy = pygame.Surface((16,16))
enemy.fill('Violet')
enemy_list =[]
difficulty = pygame.USEREVENT + 2
pygame.time.set_timer(difficulty, 500)
delta_time = 400
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, delta_time)



font = pygame.font.Font(None, 36)
lose_label = font.render("Game Over",True, (255, 255, 255))
restart_label = font.render("Pres r to restart",True, (255, 255, 255))
score = 0
running = True
gameplay = True


while running:
    font_score = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(bg,(0,0))
    screen.blit(player,(player_x,player_y))
    screen.blit(font_score, (20, 20))

    if gameplay:
        player_rect = player.get_rect(topleft = (player_x,player_y))

        if enemy_list:
            for (i, el) in enumerate(enemy_list):
                screen.blit(enemy, el)
                el.y += 10
                if el.y > screen_h + 30:
                    enemy_list.pop(i)
                    score += 1
                if player_rect.colliderect(el):
                    gameplay = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_x > 0:
            player_x -= player_speed
        elif keys[pygame.K_d] and player_x < screen_w - 16:
            player_x += player_speed
        for event in pygame.event.get():
            if event.type == enemy_timer:
                enemy_list.append(enemy.get_rect(topleft=(random.randint(0, screen_w - 16), enemy_y)))
            if event.type == difficulty and delta_time - 25 > 0:
                delta_time -= 10
                pygame.time.set_timer(enemy_timer, delta_time)

    else:
        screen.fill('Red')
        screen.blit(font_score, (100, 150))
        screen.blit(lose_label,(80, 200))
        screen.blit(restart_label, (60, 250))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            gameplay = True
            player_x = 134
            player_y = 480
            enemy_list.clear()
            score = 0
            delta_time = 400
    pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


    clock.tick(60)
