# Začátek Panzerschlachtfeld im Labyrinth ##################################################
import pygame, sys
import math
# proměnné ##################################################################################

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1100,800
RGB = R, G, B, = 0, 0, 0
poloha = False
h = 30
rychlost = 1
menu = True
#  ######################################################################################

def menu():
    global RGB, menu
    while menu:
        udalosti = pygame.event.get()
        for u in udalosti:
            if u.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        stisknuto = pygame.key.get_pressed()
        if stisknuto[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        
        okno.fill(RGB)
        
        pygame.display.update()

class player():
    
    def __init__(self, x, y , h):
        self.rect = pygame.Rect(x, y, h ,h )
        self.x = x
        self.y = y
        
    def pohyb(self, x, y):
        self.x = x
        self.y = y
        if x != 0:
            self.pohyb_kolize(self.x, 0)
        if y != 0:
            self.pohyb_kolize(0, self.y)
    
    def pohyb_kolize(self, dx, dy):
        
        # pohyb pro tank
        self.rect.x += dx
        self.rect.y += dy

        for zed in zdi:
            if self.rect.colliderect(zed.rect):
                if dx > 0: 
                    self.rect.right = zed.rect.left
                if dx < 0:
                    self.rect.left = zed.rect.right
                if dy > 0:
                    self.rect.bottom = zed.rect.top
                if dy < 0:
                    self.rect.top = zed.rect.bottom

class zed(object):
    
    def __init__(self, pos):
        zdi.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], mezery +1 , mezery_y +1 )

zdi = []
level = [
"WWWWWWWWWWWWWWWWWWWW",
"W   W   H N     W  W",
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
"W     W    W   W   W",
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
"WN     W        W   W W",
"W        WWWWWWW      W",
"W   WWWW       W      W",
"W   W        WWWW     W",
"W WWW  WWWW           W",   
"W   W     WWW         W",  
"W   W      W  WWW WH  W",
"W   WWW WWW   W W     W",
"W     W   W   W W     W",
"WWW   W   WWWWW W     W",
"W W      WW           W",
"W W   WWWW   WWW    W W",
"W     W    W   W      W",
"WWWWWWWWWWWWWWWWWWWWWWW",
]

vyber = level2

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
                hrac1 = player(x + mezery/(h/6),y + mezery_y/(h/6), h)
            if element == "N":
                hrac2 = player(x + mezery/(h/6),y + mezery_y/(h/6), h)
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
                hrac1 = player(x + mezery/(h/6),y + mezery_y/(h/6), h)
            if element == "N":
                hrac2 = player(x + mezery/(h/6),y + mezery_y/(h/6), h)
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
                hrac1 = player(x + mezery/(h/6),y + mezery_y/(h/6), h)
            if element == "N":
                hrac2 = player(x + mezery/(h/6),y + mezery_y/(h/6), h)
            x += mezery
        y += mezery_y
        x = 0
#pro pohyb
if hrac1.x < hrac2.x: 
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
        
   #menu a pod.
    menu()
        
   #pohyb
    if poloha:
        if stisknuto[pygame.K_UP]:
            hrac2.pohyb(0,-rychlost)
        if stisknuto[pygame.K_DOWN]:
            hrac2.pohyb(0, rychlost)
        if stisknuto[pygame.K_LEFT]:
            hrac2.pohyb(-rychlost, 0)
        if stisknuto[pygame.K_RIGHT]:
            hrac2.pohyb(rychlost,0)
        if stisknuto[pygame.K_w]:
            hrac1.pohyb(0,-rychlost)
        if stisknuto[pygame.K_s]:
            hrac1.pohyb(0,rychlost)
        if stisknuto[pygame.K_a]:
            hrac1.pohyb(-rychlost,0)
        if stisknuto[pygame.K_d]:
            hrac1.pohyb(rychlost,0)
    else:
        if stisknuto[pygame.K_UP]:
            hrac1.pohyb(0,-rychlost)
        if stisknuto[pygame.K_DOWN]:
            hrac1.pohyb(0, rychlost)
        if stisknuto[pygame.K_LEFT]:
            hrac1.pohyb(-rychlost, 0)
        if stisknuto[pygame.K_RIGHT]:
            hrac1.pohyb(rychlost,0)
        if stisknuto[pygame.K_w]:
            hrac2.pohyb(0,-rychlost)
        if stisknuto[pygame.K_s]:
            hrac2.pohyb(0,rychlost)
        if stisknuto[pygame.K_a]:
            hrac2.pohyb(-rychlost,0)
        if stisknuto[pygame.K_d]:
            hrac2.pohyb(rychlost,0)
# vykreslovani ##############################################################################
    
    okno.fill(RGB)
    
    for zed in zdi:
        pygame.draw.rect(okno, (0, 0, 0), zed.rect)
    pygame.draw.rect(okno, (255, 8, 0), hrac2.rect)
    pygame.draw.rect(okno, (0, 200, 0), hrac1.rect)
    pygame.display.update()