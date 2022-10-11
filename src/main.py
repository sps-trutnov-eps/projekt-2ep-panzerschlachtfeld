# Začátek Panzerschlachtfeld im Labyrinth ##################################################
import pygame, sys, math, random
# proměnné ##################################################################################

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1080,800
RGB = R, G, B, = 255,255,255
poloha = False
h = 30
rychlost = 1
MENU = True
Done = False
bila = 255,255,255
cerna = 0,0,0
##############################

pygame.font.init()

typ_pisma = pygame.font.Font('freesansbold.ttf', 25)


# cudliky
np1 = ((200,80), (700,100), (0,0,0), "text" )
cl_hl1 = ((375, 260), (375, 100), (0,0,0), "text")
cl_hl2 = ((375, 440), (375, 100), (0,0,0), "text")
cl_hl3 = ((375, 620), (375, 100), (0,0,0), "text")

np2 = ((200, 40), (700,100), (0,0,0), "text" )
cl_v1 = ((375, 180), (375, 100), (0,190,0), "text")
cl_v2 = ((375, 360), (375, 100), (0,190,0), "text")
cl_v3 = ((375, 540), (375, 100), (0,190,0), "text")

cl_exit = ((925, 725), (150, 50), (0,0,0), "text")

cl_close = ((25, 725), (150, 50), (0,0,0), "text")

# obrazovky menu
hlavni_menu = [(190,190,190), "Panzerschlachtfeld", (cl_hl1, cl_hl2, cl_hl3, np1, cl_exit)]
menu_vyberu = [(190,190,190), "Panzerschlachtfeld", (cl_v1, cl_v2, cl_v3, np2, cl_close)]
pause_menu = [(190, 190, 190), "Panzerschlachtfeld",()]
aktivni_obrazovka = hlavni_menu
#  ######################################################################################   

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
"WWW       N      WWW",
"WW       WW       WW",
"W   W  WWWWWW  W   W",
"W  WW          WW  W",
"W  WW          WW  W",
"W   W  WWWWWW  W   W",
"WW       WW       WW",
"WWW      H       WWW",
"WWWWWWWWWWWWWWWWWWWW",
]

level1 = [
"WWWWWWWWWWWWWWWWWWWW",
"W                  W",
"W                  W",
"W                  W",
"W                  W",
"W                  W",
"W                  W",
"W                  W",
"W                  W",
"W                  W",
"W                  W",
"W                  W",
"W                  W",
"W                  W",
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

# pro responzivitu s velikostí okna
levely = [level, level1, level2]
vyber = level

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
    while MENU:
        udalosti = pygame.event.get()
        for u in udalosti:
            if u.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        stisknuto = pygame.key.get_pressed()
        if stisknuto[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        
        okno.fill(aktivni_obrazovka[0])
        for cudlik in aktivni_obrazovka[2]:
            pygame.draw.rect(okno,cudlik[2], (cudlik[0], cudlik[1]))
        
        if aktivni_obrazovka == hlavni_menu:
            if cl_hl1[0][0] < pygame.mouse.get_pos()[0] < (cl_hl1[0][0] + cl_hl1[1][0]) and cl_hl1[0][1] < pygame.mouse.get_pos()[1] < (cl_hl1[0][1] + cl_hl1[1][1]) and pygame.mouse.get_pressed()[0]:
                aktivni_obrazovka = menu_vyberu
       
            if cl_hl2[0][0] < pygame.mouse.get_pos()[0] < (cl_hl2[0][0] + cl_hl2[1][0]) and cl_hl2[0][1] < pygame.mouse.get_pos()[1] < (cl_hl2[0][1] + cl_hl2[1][1]) and pygame.mouse.get_pressed()[0]:
                vyber = random.choice(levely)
                Done = True
                MENU = False
            if cl_exit[0][0] < pygame.mouse.get_pos()[0] < (cl_exit[0][0] + cl_exit[1][0]) and cl_exit[0][1] < pygame.mouse.get_pos()[1] < (cl_exit[0][1] + cl_exit[1][1]) and pygame.mouse.get_pressed()[0] and aktivni_obrazovka == hlavni_menu:
                pygame.quit()
                sys.exit()
                
        if aktivni_obrazovka == menu_vyberu:
            if cl_v1[0][0] < pygame.mouse.get_pos()[0] < (cl_v1[0][0] + cl_v1[1][0]) and cl_v1[0][1] < pygame.mouse.get_pos()[1] < (cl_v1[0][1] + cl_v1[1][1]) and pygame.mouse.get_pressed()[0]:
                vyber = levely[0]
                Done = True
                MENU = False
            if cl_v2[0][0] < pygame.mouse.get_pos()[0] < (cl_v2[0][0] + cl_v2[1][0]) and cl_v2[0][1] < pygame.mouse.get_pos()[1] < (cl_v2[0][1] + cl_v2[1][1]) and pygame.mouse.get_pressed()[0]:    
                vyber = levely[1]
                Done = True
                MENU = False
            if cl_v3[0][0] < pygame.mouse.get_pos()[0] < (cl_v3[0][0] + cl_v3[1][0]) and cl_v3[0][1] < pygame.mouse.get_pos()[1] < (cl_v3[0][1] + cl_v3[1][1]) and pygame.mouse.get_pressed()[0]:
                vyber = levely[2]
                Done = True
                MENU = False
            if cl_close[0][0] < pygame.mouse.get_pos()[0] < (cl_close[0][0] + cl_close[1][0]) and cl_close[0][1] < pygame.mouse.get_pos()[1] < (cl_close[0][1] + cl_close[1][1]) and pygame.mouse.get_pressed()[0]:  
                aktivni_obrazovka = hlavni_menu
                
        if aktivni_obrazovka == hlavni_menu:
            hl_nadpis1 = typ_pisma.render('Panzerschlachtfeld im Labyrinth:', True, bila, cerna)
            hl_nadpis1Rect = hl_nadpis1.get_rect()
            hl_nadpis1Rect.center = (550, 128)
            

            nadpis_menu1 = typ_pisma.render('vybrat mapu', True, bila, cerna)
            nadpis_menu1Rect = nadpis_menu1.get_rect()
            nadpis_menu1Rect.center = (560, 308)
            
            
            nadpis_menu2 = typ_pisma.render('náhodná mapa', True, bila, cerna)
            nadpis_menu2Rect = nadpis_menu2.get_rect()
            nadpis_menu2Rect.center = (560, 488)
            

            nadpis_menu3 = typ_pisma.render('CREDITS', True, bila, cerna)
            nadpis_menu3Rect = nadpis_menu3.get_rect()
            nadpis_menu3Rect.center = (560, 668)
            
            nadpis_exit = typ_pisma.render('EXIT', True, bila, cerna)
            nadpis_exitRect = nadpis_exit.get_rect()
            nadpis_exitRect.center = (1000, 750)
        
        if aktivni_obrazovka == menu_vyberu:
            hl_nadpis2 = typ_pisma.render('Panzerschlachtfeld im Labyrinth:', True, bila, cerna)
            hl_nadpis2Rect = hl_nadpis2.get_rect()
            hl_nadpis2Rect.center = (550, 88)
            
            nadpis_close = typ_pisma.render('CLOSE', True, bila, cerna)
            nadpis_closeRect = nadpis_close.get_rect()
            nadpis_closeRect.center = (100, 750)
            
            

            
    ############################################################################################################################################################################################################   
        
        if aktivni_obrazovka == hlavni_menu:
            okno.blit(nadpis_exit, nadpis_exitRect)
            okno.blit(hl_nadpis1, hl_nadpis1Rect)
            okno.blit(nadpis_menu1, nadpis_menu1Rect)
            okno.blit(nadpis_menu2, nadpis_menu2Rect)
            okno.blit(nadpis_menu3, nadpis_menu3Rect)
            
        if aktivni_obrazovka == menu_vyberu:
            okno.blit(hl_nadpis2, hl_nadpis2Rect)
            okno.blit(nadpis_close, nadpis_closeRect)
        
        ######vykreslovani
        if Done == True:
            mezery = ROZLISENI_X/len(vyber[0])
            mezery_y = ROZLISENI_Y/len(vyber)
            x = y = 0
            for radek in vyber:
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
            if hrac1.x < hrac2.x: 
                poloha = True 
            else: 
                poloha = False      
        pygame.display.update()
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
    clockobject = pygame.time.Clock()
    clockobject.tick(100)
    pygame.display.update()