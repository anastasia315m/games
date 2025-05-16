#add game over display
#add compliments when clear a row

import pygame, sys
from game import Game
from colors import Colors

pygame.init()

# creating titles
tittle_font = pygame.font.SysFont("Comic Sans", 40) #here
game_over_font = pygame.font.SysFont(None, 40)
score_surface = tittle_font.render("Score", True, (255, 255, 255)) #white font
next_surface = tittle_font.render("Next", True, (255, 255, 255))
game_over_surface = game_over_font.render("GAME OVER", True, (255, 255, 255))

score_rect = pygame.Rect(320, 80, 170, 60) #position of the score background (rect)
next_rect = pygame.Rect(320, 240, 170, 180) #position of the next block background

#set a screen
screen = pygame.display.set_mode((500, 620))
#set a caption
pygame.display.set_caption("Tetris: Glamour Grid edition")
#set a logo
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 250)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    #show score
    score_value_surface = tittle_font.render(str(game.score), True, (255, 255, 255))
    #screen
    screen.fill((180, 70, 109)) #screen color (dark pink)
    #blit titles
    screen.blit(score_surface, (350, 20, 50, 50)) #position of the score
    screen.blit(next_surface, (360, 180, 50, 50)) #position of the title "next"

    #if player loses, then "game over" appears
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 460, 50, 50)) #positions of the "game over" text

    #blit backgrounds (rect)
    pygame.draw.rect(screen, (225, 94, 137), score_rect, 0, 10) #0 and 10 are the rounded corners
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, (225, 94, 137), next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
