import pygame, sys
from pygame import K_s, K_SPACE  # librairie pour détecter l'appuie sur la barre d'espace
from pygame.math import Vector2
import core
from bird import Bird # import la classe Bird
from obstacle import Obstacle # import la classe obstacle
import random

def dessiner_sol():
    ecran.blit(sol, (sol_posX, 750))
    ecran.blit(sol, (sol_posX + 576, 750))
def affichage_bird(x,y):
    ecran.blit(bird, (x,y))
def affichage_obstacle(height):
    pygame.draw.rect(ecran, obstacle_color, (obstacle_X, 0, obstacle_width, height))
    Bottom_obstacle_height = 635 - height - 150
    pygame.draw.rect(ecran, obstacle_color, (obstacle_X, 635, obstacle_width, -Bottom_obstacle_height))

pygame.init()
ecran = pygame.display.set_mode((500, 800)) #initialise la taille de l'écran
clock = pygame.time.Clock()

#obstacle
obstacle_width = 70
obstacle_height = random.randint(150, 450)
obstacle_color = (51, 153, 102)
obstacle_X_change = -4
obstacle_X = 500

# background
fond = pygame.image.load('images/fond.png').convert()# import une image en tant que fond d'écrans
fond = pygame.transform.scale2x(fond) #traite cette image pour l'agrandir car elle est trop petite

#bird
bird = pygame.image.load('images/bird.png').convert()#import une image pour le bird
bird = pygame.transform.scale2x(bird)
bird_x = 50
bird_y = 300
bird_y_change = 0

#floor
sol = pygame.image.load('images/sol.png').convert()
sol = pygame.transform.scale2x(sol)
sol_posX = 0

running = True
while running:

    ecran.blit(fond,(0,0))
    sol_posX -= 1
    dessiner_sol()
    if sol_posX <= -576:
        sol_posX = 0



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = -6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = +3

    bird_y += bird_y_change

    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 700:
        bird_y = 700

    obstacle_X += obstacle_X_change
    if obstacle_X <=-10:
        obstacle_X = 500
        obstacle_height = random.randint(200, 400)
    affichage_obstacle(obstacle_height)

    affichage_bird(bird_x,bird_y)
    pygame.display.update()
    clock.tick(80)

pygame.quit()
