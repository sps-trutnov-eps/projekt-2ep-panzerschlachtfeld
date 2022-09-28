# Začátek Panzerschlachtfeld im Labyrinth ##################################################

import pygame, sys
import math
# proměnné ##################################################################################

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1100,800
RGB = R, G, B, = 255, 255, 255
cerna = 0, 0, 0
poloha = False
#  ######################################################################################
class zed(object):
    global mezery, mezery_y
    def __init__(self, pos):
        zdi.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], mezery +1 , mezery_y +1 )

zdi = []

level = [
"WWWWWWWWWWWWWWWWWWWW",
"W H    W        W  W",
"W        WWWWWWW   W",
"W   WWWW       W   W",
"W   W        WWWW  W",
"W WWW  WWWW        W",
"W   W     WWW N    W",
"W   W      W  WWW WW",
"W   WWW WWW   W W  W",
"W     W   W   W W  W",
"WWW   W   WWWWW W  W",
"W W      WW        W",
"W W   WWWW   WWW   W",
"W     W N  W   W   W",
"WWWWWWWWWWWWWWWWWWWW",
]

level1 = [
"WWWWWWWWWWWWWWWWWWWW",
"WN     W        W  W",
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
"W     W H  W   W   W",
"WWWWWWWWWWWWWWWWWWWW",
]

level2 = [
"WWWWWWWWWWWWWWWWWWWWWWW",
"WH     W        W   W W",
"W        WWWWWWW      W",
"W   WWWW       W      W",
"W   W        WWWW     W",
"W WWW  WWWW           W",   
"W   W     WWW         W",  
"W   W      W  WWW W   W",
"W   WWW WWW   W W     W",
"W     W   W   W W     W",
"WWW   W   WWWWW W     W",
"W W      WW           W",
"W W   WWWW   WWW    W W",
"W     W N  W   W      W",
"WWWWWWWWWWWWWWWWWWWWWWW",
]

vyber = level1

# pro responzivitu s velikostí okna

#vykreslování okna H=hrac N=nepřítel W=zed
x = y = 0
if vyber == level:
    mezery = ROZLISENI_X/len(level[0])
    mezery_y = ROZLISENI_Y/len(level)
    RAD_HRACE = 20
    for radek in level:
        for element in radek:
            if element == "W":
                zed((x, y))
            if element == "H":
                hrac1 = [x + mezery/2, y + mezery_y/2]
            if element == "N":
                hrac2 = [x + mezery/2, y + mezery_y/2]
            x += mezery
        y += mezery_y
        x = 0
if vyber == level1:
    mezery = ROZLISENI_X/len(level1[0])
    mezery_y = ROZLISENI_Y/len(level1)
    RAD_HRACE = 20
    for radek in level1:
        for element in radek:
            if element == "W":
                zed((x, y))
            if element == "H":
                hrac1 = [x + mezery/2, y + mezery_y/2]
            if element == "N":
                hrac2 = [x + mezery/2, y + mezery_y/2]
            x += mezery
        y += mezery_y
        x = 0
if vyber == level2:
    mezery = ROZLISENI_X/len(level2[0])
    mezery_y = ROZLISENI_Y/len(level2)
    RAD_HRACE = 20
    for radek in level2:
        for element in radek:
            if element == "W":
                zed((x, y))
            if element == "H":
                hrac1 = [x + mezery/2, y + mezery_y/2]
            if element == "N":
                hrac2 = [x + mezery/2, y + mezery_y/2]
            x += mezery
        y += mezery_y
        x = 0
#TĚLESA/TANKY/proměnné
v_y = 0.5
v_x = 0.5
if hrac1[0] < hrac2[0]:
    poloha = True
else:
    poloha = False

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
    if poloha:
        if stisknuto[pygame.K_UP]:
            hrac2[1] -= 1
        if stisknuto[pygame.K_DOWN]:
            hrac2[1] += 1
        if stisknuto[pygame.K_LEFT]:
            hrac2[0] -= 1
        if stisknuto[pygame.K_RIGHT]:
            hrac2[0] += 1
        if stisknuto[pygame.K_w]:
            hrac1[1] -= 1
        if stisknuto[pygame.K_s]:
            hrac1[1] += 1
        if stisknuto[pygame.K_a]:
            hrac1[0] -= 1
        if stisknuto[pygame.K_d]:
            hrac1[0] += 1
    else:
        if stisknuto[pygame.K_UP]:
            hrac1[1] -= 1
        if stisknuto[pygame.K_DOWN]:
            hrac1[1] += 1
        if stisknuto[pygame.K_LEFT]:
            hrac1[0] -= 1
        if stisknuto[pygame.K_RIGHT]:
            hrac1[0] += 1
        if stisknuto[pygame.K_w]:
            hrac2[1] -= 1
        if stisknuto[pygame.K_s]:
            hrac2[1] += 1
        if stisknuto[pygame.K_a]:
            hrac2[0] -= 1
        if stisknuto[pygame.K_d]:
            hrac2[0] += 1
# vykreslovani ##############################################################################
    
    okno.fill(RGB)
    
    for zed in zdi:
        pygame.draw.rect(okno, (0, 0, 0), zed.rect)
    pygame.draw.circle(okno, (255, 8, 0), hrac2, RAD_HRACE)
    pygame.draw.circle(okno, (0, 200, 0), hrac1, RAD_HRACE)
    pygame.display.flip()