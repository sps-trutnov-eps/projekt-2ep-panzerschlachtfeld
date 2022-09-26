# Začátek Panzerschlachtfeld im Labyrinth ##################################################

import pygame, sys
import math

#  ######################################################################################

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
A = [0,0]
B = [0,1]
C = [0,2]
D = [1,0]
E = [1,1]
F = [2,0]

# pravý horní roh
G = [0,8]
H = [0,9]
CH = [0,10]
I = [1,9]
J = [1,10]
K = [2,10]

# levý dolní roh
L = [7,0]
M = [8,0]
O = [8,1]
P = [9,0]
Q = [9,1]
R = [9,2]

# pravý horní roh
S = [9,8]
T = [9,9]
U = [9,10]
V = [8,9]
W = [8,10]
Z = [7,10]

# střed
aA = [4,1]
bB = [5,1]
cC = [3,2]
dD = [4,2]
eE = [5,2]
fF = [6,2]
gG = [3,4]
hH = [3,5]
chCH = [3,6]
iI = [2,5]
jJ = [6,4]
kK = [6,5]
lL = [6,6]
mM = [7,5]
nN = [3,8]
oO = [4,8]
pP = [5,8]
qQ = [6,8]
rR = [4,9]
sS = [5,9]
    
ctverecky = [A,B,C,D,E,F,G,H,CH,I,J,K,L,M,O,P,Q,R,S,T,U,V,W,Z,aA,bB,cC,dD,eE,fF,gG,hH,chCH,iI,jJ,kK,lL,mM,nN,oO,pP,qQ,rR,sS]

# proměnné ##################################################################################

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1100,1000
RGB = R, G, B, = 255, 255, 255
cerna = 0, 0, 0


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
    
    for ctverecek in ctverecky:
        pygame.draw.rect(okno, cerna,((ctverecek[1]*VELIKOST_RASTRU,ctverecek[0]*VELIKOST_RASTRU), (100,100)))
    
    pygame.draw.circle(okno, (205,8,0), (x1,y1), r1)
    pygame.display.update()
        