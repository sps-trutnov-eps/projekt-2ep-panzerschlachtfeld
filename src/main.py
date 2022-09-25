# Začátek Panzerschlachtfeld im Labyrinth ##################################################

import pygame, sys
import math

# mapa ######################################################################################

VELIKOST_RASTRU = 100

mapa = [
        [0,1,2,3,4,5,6,7,8,9,10], #0
        [0,1,2,3,4,5,6,7,8,9,10], #1
        [0,1,2,3,4,5,6,7,8,9,10], #2
        [0,1,2,3,4,5,6,7,8,9,10], #3
        [0,1,2,3,4,5,6,7,8,9,10], #4
        [0,1,2,3,4,5,6,7,8,9,10], #5
        [0,1,2,3,4,5,6,7,8,9,10], #6
        [0,1,2,3,4,5,6,7,8,9,10], #7
        [0,1,2,3,4,5,6,7,8,9,10], #8
        [0,1,2,3,4,5,6,7,8,9,10], #9
        ]
# levý horní roh
A = mapa[0],[0]
B = mapa[0],[1]
C = mapa[0],[2]
D = mapa[1],[0]
E = mapa[1],[1]
F = mapa[2],[0]

# pravý horní roh
G = mapa[0],[8]
H = mapa[0],[9]
CH = mapa[0],[10]
I = mapa[1],[9]
J = mapa[1],[10]
K = mapa[2],[10]

# levý dolní roh
L = mapa[7],[0]
M = mapa[8],[0]
O = mapa[8],[1]
P = mapa[9],[0]
Q = mapa[9],[1]
R = mapa[9],[2]

# pravý horní roh
S = mapa[9],[8]
T = mapa[9],[9]
U = mapa[9],[10]
V = mapa[8],[9]
W = mapa[8],[10]
Z = mapa[7],[10]

# proměnné ##################################################################################

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1100,1000
RGB = R, G, B, = 255, 255, 255


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
    #pygame.draw.rect(okno,)
    pygame.draw.circle(okno, (205,8,0), (x1,y1), r1)
    pygame.display.update()
        