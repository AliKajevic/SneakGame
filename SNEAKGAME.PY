import pygame
import time
import random
SS = 15
x = 720
y = 480
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
pygame.init()

pygame.display.set_caption('SNEAKGAME')
GW = pygame.display.set_mode((x, y))
fps = pygame.time.Clock()

SP = [100, 50]

SB = [[100, 50],
      [90, 50],
      [80, 50],
      [70, 50]
]

score_position = [random.randrange(1, (x//10)) * 10, 
                  random.randrange(1, (y//10)) * 10]

score_spawn = True

direction = 'DOWN'
change_to = direction

score = 0

def show_score(choice, color, font, size):
  
    score_font = pygame.font.SysFont(font, size)
    
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    score_rect = score_surface.get_rect()
    
    GW.blit(score_surface, score_rect)

def game_over():
  
    my_font = pygame.font.SysFont('times new roman', 50)
    
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    
    game_over_rect = game_over_surface.get_rect()
    
    game_over_rect.midtop = (x/2, y/4)
    
    GW.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    pygame.quit()
    
    quit()


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                change_to = 'UP'
            if event.key == pygame.K_s:
                change_to = 'DOWN'
            if event.key == pygame.K_a:
                change_to = 'LEFT'
            if event.key == pygame.K_d:
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                quit()

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        SP[1] -= 10
    if direction == 'DOWN':
        SP[1] += 10
    if direction == 'LEFT':
        SP[0] -= 10
    if direction == 'RIGHT':
        SP[0] += 10

    SB.insert(0, list(SP))
    if SP[0] == score_position[0] and SP[1] == score_position[1]:
        score += 10
        score_spawn = False
    else:
        SB.pop()
        
    if not score_spawn:
        score_position = [random.randrange(1, (x//10)) * 10, 
                          random.randrange(1, (y//10)) * 10]
        
    score_spawn = True
    GW.fill(black)
    
    for pos in SB:
        pygame.draw.rect(GW, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(GW, white, pygame.Rect(
        score_position[0], score_position[1], 10, 10))

    if SP[0] < 0 or SP[0] > x-10:
        game_over()
    if SP[1] < 0 or SP[1] > y-10:
        game_over()

    for block in SB[1:]:
        if SP[0] == block[0] and SP[1] == block[1]:
            game_over()

    show_score(1, white, 'times new roman', 20)

    pygame.display.update()
    fps.tick(SS)
