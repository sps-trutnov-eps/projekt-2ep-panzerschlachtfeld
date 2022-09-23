# Začátek Panzerschlachtfeld im Labyrinth ##################################################

import pygame, sys
import math


# proměnné ##################################################################################

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 800,800
RGB = R, G, B, = 255, 255, 255

#TĚLESA/TANKY
x1 = ROZLISENI_X/2
y1 = ROZLISENI_Y/2
r1 = 12


# inicializace aplikace #####################################################################

pygame.init()

pygame.display.set_caption('Panzerschlachtfeld im Labyrinth')
okno = pygame.display.set_mode(ROZLISENI_OKNA)


while True:
    
# ovladani aplikace ########################################################################
    
    udalosti = pygame.event.get()
    for u in udalosti:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    stisknuto = pygame.key.get_pressed()
    if stisknuto[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
        
    #kolize
    if x1 > ROZLISENI_X:
        x1 = r1
    if y1 > ROZLISENI_Y:
        y1 = r1
    if x1 < 0:
        x1 = ROZLISENI_X
    if y1 < 0:
        y1 = ROZLISENI_Y
        
    #pohyb
    x1 += 0.04
    y1 += 0.02
    
# vykreslovani ##############################################################################
    
    okno.fill(RGB)
    pygame.draw.circle(okno, (205,8,0), (x1,y1), r1)
    pygame.display.update()
        