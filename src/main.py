# Začátek Panzerschlachtfeld im Labyrinth ##################################################

import pygame, sys
import math
from maps import level1 

# proměnné ##################################################################################

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1100,1000
RGB = R, G, B, = 255, 255, 255
cerna = 0, 0, 0
VELIKOST_RASTRU = 100

#TĚLESA/TANKY
x1 = ROZLISENI_X/2
y1 = ROZLISENI_Y/2
r1 = 12

v_y = 0.078
v_x = 0.078

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
    if x1 - r1 > ROZLISENI_X:
        x1 = r1
    if y1 - r1 > ROZLISENI_Y:
        y1 = r1
    if x1 + r1 < 0:
        x1 = ROZLISENI_X
    if y1 + r1< 0:
        y1 = ROZLISENI_Y
        
    #pohyb
    if stisknuto[pygame.K_UP]:
        y1 -= v_y
    if stisknuto[pygame.K_DOWN]:
        y1 += v_y
    if stisknuto[pygame.K_RIGHT]:
        x1 += v_x
    if stisknuto[pygame.K_LEFT]:
        x1 -= v_x
# vykreslovani ##############################################################################
    
    okno.fill(RGB)
    
    for ctverecek in level1:
        pygame.draw.rect(okno, cerna,((ctverecek[1]*VELIKOST_RASTRU,ctverecek[0]*VELIKOST_RASTRU), (100,100)))
    
    pygame.draw.circle(okno, (205,8,0), (x1,y1), r1)
    pygame.display.update()
        