# Začátek Panzerschlachtfeld im Labyrinth ##################################################

import pygame, sys
import math


# proměnné ##################################################################################

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1100,800
RGB = R, G, B, = 255, 255, 255
cerna = 0, 0, 0


#  ######################################################################################
class zed(object):
    global mezery, mezery_y
    def __init__(self, pos):
        zdi.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], mezery, mezery_y +1 )

zdi = []

level = [
"WWWWWWWWWWWWWWWWWWWW",
"WH     W        W   W",
"W        WWWWWWW   W",
"W   WWWW       W   W",
"W   W        WWWW  W",
"W WWW  WWWW        W",
"W   W     WWW      W",
"W   W      W  WWW WW",
"W   WWW WWW   W W  W",
"W     W   W   W W  W",
"WWW   W   WWWWW W  W",
"W W      WW        W",
"W W   WWWW   WWW   W",
"W     W N  W   W   W",
"WWWWWWWWWWWWWWWWWWWW",
]

# pro responzivitu s velikostí okna
mezery = ROZLISENI_X/len(level[0])
mezery_y = ROZLISENI_Y/len(level)
RAD_HRACE = 20
#vykreslování okna H=hrac N=nepřítel W=zed
x = y = 0
for radek in level:
    for element in radek:
        if element == "W":
            zed((x, y))
        if element == "H":
            hrac1 = (x + mezery/2, y + mezery_y/2)
        if element == "N":
            hrac2 = (x + mezery/2, y + mezery_y/2)
        x += mezery
    y += mezery_y
    x = 0


#TĚLESA/TANKY
v_y = 0.5
v_x = 0.5

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
        
    
        
    #pohyb
    
# vykreslovani ##############################################################################
    
    okno.fill(RGB)
    
    
    
    for zed in zdi:
        pygame.draw.rect(okno, (0, 0, 0), zed.rect)
    pygame.draw.circle(okno, (255, 8, 0), hrac2, RAD_HRACE)
    pygame.draw.circle(okno, (0, 200, 0), hrac1, RAD_HRACE)
    pygame.display.flip()
        