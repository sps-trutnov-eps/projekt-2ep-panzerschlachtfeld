# Začátek Panzerschlachtfeld im Labyrinth ##################################################
import pygame, sys, math, random
# proměnné ##################################################################################

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1080,800
RGB = R, G, B, = 255,255,255
h = 30
rychlost = 100
poloha = False
MENU = True
Done = False
in_game_menu = False
p_zmacknuto_pred_tim = False
pohyb_tanku = True
bila = 255,255,255
cerna = 0,0,0
mapa1_pozadi = pygame.image.load("..\doc\mapa-1.png")
mapa2_pozadi = pygame.image.load("..\doc\mapa-2.png")
mapa3_pozadi = pygame.image.load("..\doc\mapa-3.png") 
##############################

pygame.font.init()

typ_pisma = pygame.font.Font('freesansbold.ttf', 25)

# cudliky
#hlavní menu
np1 = ((200,80), (700,100), (0,0,0), "text" )
cl_hl1 = ((375, 260), (375, 100), (0,0,0), "text")
cl_hl2 = ((375, 440), (375, 100), (0,0,0), "text")
cl_hl3 = ((375, 620), (375, 100), (0,0,0), "text")
cl_exit1 = ((925, 725), (150, 50), (0,0,0), "text")

#menu výběru
np2 = ((200, 40), (700,100), (0,0,0), "text" )
cl_close1 = ((25, 725), (150, 50), (0,0,0), "text")
cl_v1 = ((155, 350), (150, 150), (0,0,0), "text")
cl_v2 = ((460, 350), (150, 150), (0,0,0), "text")
cl_v3 = ((765, 350), (150, 150), (0,0,0), "text")

#menu credits
np3 = ((200, 40), (700,100), (0,0,0), "text" )
cl_close2 = ((25, 725), (150, 50), (0,0,0), "text")
 
#ingame menu
np4 = ((365, 175), (400,75), (0,0,0), "text" )
cl_exit2 = ((492, 420), (150, 50), (0,0,0), "text")
cl_close3 = ((340, 580), (150, 50), (0,0,0), "text")
cl_pin = ((492, 325), (150, 50), (0,0,0), "text")

# obrazovky menu
hlavni_menu = [(190,190,190), "Panzerschlachtfeld", (cl_hl1, cl_hl2, cl_hl3, np1, cl_exit1)]
menu_vyberu = [(190,190,190), "Panzerschlachtfeld", (cl_v1, cl_v2, cl_v3, np2, cl_close1)]
menu_CREDITS = [(190,190,190), "Panzerschlachtfeld", (np3, cl_close2)]
pause_menu = [(190, 190, 0), "Panzerschlachtfeld", (np4, cl_exit2, cl_pin, cl_close3)]
aktivni_obrazovka = hlavni_menu
#  ######################################################################################   

class player(pygame.sprite.Sprite):
    
    def __init__(self, x, y , h):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, h ,h )
        self.rychlost1 = 0 
        self.rychlost2 = 0
        self.pohyb = 1
        
    def update(self):
        self.rychlost1 = 0
        self.rychlost2 = 0
       
        ##pohyb
        if stisknuto[pygame.K_UP]:
            self.rychlost1 += -self.pohyb
        if stisknuto[pygame.K_DOWN]:
            self.rychlost1 += self.pohyb
        
        if stisknuto[pygame.K_w]:
            self.rychlost2 += -self.pohyb
        if stisknuto[pygame.K_s]:
            self.rychlost2 += self.pohyb
        
        #kolize
        if self.rect.x + h > ROZLISENI_X:
            self.rect.x = ROZLISENI_X - h
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y + h > ROZLISENI_Y:
            self.rect.y = ROZLISENI_Y - h
        if self.rect.y < 0:
            self.rect.y = 0
        
        if pohyb_tanku:
            if poloha:
                hrac1.rect.y += hrac1.rychlost1
                hrac2.rect.y += hrac2.rychlost2
            else:
                hrac1.rect.y += hrac1.rychlost2
                hrac2.rect.y += hrac2.rychlost1
        else:
            pass
        
        for zed in zdi:
            if pygame.Rect.colliderect(hrac1.rect, zed.rect):
                if poloha:
                    if self.rychlost1 > 0:
                        hrac1.rect.bottom = zed.rect.top
                        self.rychlost1 = 0 
                    if self.rychlost1 < 0:    
                        hrac1.rect.top = zed.rect.bottom
                        self.rychlost1 = 0 
                else:
                    if self.rychlost2 > 0:
                        hrac1.rect.bottom = zed.rect.top
                        self.rychlost2 = 0 
                    if self.rychlost2 < 0:    
                        hrac1.rect.top = zed.rect.bottom
                        self.rychlost2 = 0
           
            if pygame.Rect.colliderect(hrac2.rect, zed.rect):
                if poloha == False:
                    if self.rychlost1 > 0:
                        hrac2.rect.bottom = zed.rect.top
                        self.rychlost1 = 0 
                    if self.rychlost1 < 0:    
                        hrac2.rect.top = zed.rect.bottom
                        self.rychlost1 = 0 
                else:
                    if self.rychlost2 > 0:
                        hrac2.rect.bottom = zed.rect.top
                        self.rychlost2 = 0 
                    if self.rychlost2 < 0:    
                        hrac2.rect.top = zed.rect.bottom
                        self.rychlost2 = 0

class Zed(object): #jakýkoliv objekt s VELKÝM počátčním písmenem SAMEEEEEEEEEEE!!!
    
    def __init__(self, pos):
        zdi.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], mezery +1 , mezery_y +1 )

zdi = []
level = [
"WWWWWWWWWWWWWWWWWWWW",
"WWW       N      WWW",
"WW       WW       WW",
"W   W  WWWWWW  W   W",
"W WWW          WWW W",
"W WWW          WWW W",
"W   W  WWWWWW  W   W",
"WW       WW       WW",
"WWW      H       WWW",
"WWWWWWWWWWWWWWWWWWWW",
]

level1 = [
"WWWWWWWWWWWWWWWWWWWW",
"WW    W   H   W    W",
"W  W             W W",
"W  W  WWWWWWWWW  W W",
"W  W      W      W W",
"W  W   WW   WW  W  W",
"W  W      W      W W",
"W  W  WWWWWWWWW  W W",
"W  W             W W",
"WW    W   N   W    W",
"WWWWWWWWWWWWWWWWWWWW",
]

level2 = [
"WWWWWWWWW NWWWWWWWWW",
"W                  W",
"W  WWW   WW   WWW  W",
"W  W            W  W",
"W     WWW  WWW     W",
"WW  WWWW    WWWW  WW",
"W     WWW  WWW     W",
"W  W            W  W",
"W  WWW   WW   WWW  W",
"W                  W",
"WWWWWWWWWH WWWWWWWWW",
]

# pro responzivitu s velikostí okna
levely = [level, level1, level2]
vyber = level

pygame.init()

pygame.display.set_caption('Panzerschlachtfeld im Labyrinth')
okno = pygame.display.set_mode(ROZLISENI_OKNA)
sprites = pygame.sprite.Group()

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
            pygame.draw.rect(okno, cudlik[2], (cudlik[0], cudlik[1]))
        
        if aktivni_obrazovka == hlavni_menu:
            if cl_hl1[0][0] < pygame.mouse.get_pos()[0] < (cl_hl1[0][0] + cl_hl1[1][0]) and cl_hl1[0][1] < pygame.mouse.get_pos()[1] < (cl_hl1[0][1] + cl_hl1[1][1]) and pygame.mouse.get_pressed()[0]:
                aktivni_obrazovka = menu_vyberu
       
            if cl_hl2[0][0] < pygame.mouse.get_pos()[0] < (cl_hl2[0][0] + cl_hl2[1][0]) and cl_hl2[0][1] < pygame.mouse.get_pos()[1] < (cl_hl2[0][1] + cl_hl2[1][1]) and pygame.mouse.get_pressed()[0]:
                vyber = random.choice(levely)
                Done = True
                MENU = False
                
            if cl_exit1[0][0] < pygame.mouse.get_pos()[0] < (cl_exit1[0][0] + cl_exit1[1][0]) and cl_exit1[0][1] < pygame.mouse.get_pos()[1] < (cl_exit1[0][1] + cl_exit1[1][1]) and pygame.mouse.get_pressed()[0] and aktivni_obrazovka == hlavni_menu:
                pygame.quit()
                sys.exit()
            
            if cl_hl3[0][0] < pygame.mouse.get_pos()[0] < (cl_hl3[0][0] + cl_hl3[1][0]) and cl_hl3[0][1] < pygame.mouse.get_pos()[1] < (cl_hl3[0][1] + cl_hl3[1][1]) and pygame.mouse.get_pressed()[0] and aktivni_obrazovka == hlavni_menu:
                aktivni_obrazovka = menu_CREDITS
             
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
                
            if cl_close1[0][0] < pygame.mouse.get_pos()[0] < (cl_close1[0][0] + cl_close1[1][0]) and cl_close1[0][1] < pygame.mouse.get_pos()[1] < (cl_close1[0][1] + cl_close1[1][1]) and pygame.mouse.get_pressed()[0]:  
                aktivni_obrazovka = hlavni_menu
        
        if aktivni_obrazovka == menu_CREDITS:
            if cl_close2[0][0] < pygame.mouse.get_pos()[0] < (cl_close2[0][0] + cl_close2[1][0]) and cl_close2[0][1] < pygame.mouse.get_pos()[1] < (cl_close2[0][1] + cl_close2[1][1]) and pygame.mouse.get_pressed()[0]:  
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
            
            nadpis_close1 = typ_pisma.render('CLOSE', True, bila, cerna)
            nadpis_close1Rect = nadpis_close1.get_rect()
            nadpis_close1Rect.center = (100, 750)
        
        if aktivni_obrazovka == menu_CREDITS:
            hl_nadpis3 = typ_pisma.render('Panzerschlachtfeld im Labyrinth:', True, bila, cerna)
            hl_nadpis3Rect = hl_nadpis3.get_rect()
            hl_nadpis3Rect.center = (550, 88)
            
            nadpis_close2 = typ_pisma.render('CLOSE', True, bila, cerna)
            nadpis_close2Rect = nadpis_close2.get_rect()
            nadpis_close2Rect.center = (100, 750)
 
    ###############vykreslovani########################################################################################################################################################################   
        
        if aktivni_obrazovka == hlavni_menu:
            okno.blit(nadpis_exit, nadpis_exitRect)
            okno.blit(hl_nadpis1, hl_nadpis1Rect)
            okno.blit(nadpis_menu1, nadpis_menu1Rect)
            okno.blit(nadpis_menu2, nadpis_menu2Rect)
            okno.blit(nadpis_menu3, nadpis_menu3Rect)
            
        if aktivni_obrazovka == menu_vyberu:
            okno.blit(hl_nadpis2, hl_nadpis2Rect)
            okno.blit(nadpis_close1, nadpis_close1Rect)
            
            okno.blit(mapa1_pozadi, (155, 350))
            okno.blit(mapa2_pozadi, (460, 350))
            okno.blit(mapa3_pozadi, (766, 350))
            
        if aktivni_obrazovka == menu_CREDITS:
            okno.blit(hl_nadpis3, hl_nadpis3Rect)
            okno.blit(nadpis_close2, nadpis_close2Rect)
        
        if Done == True:
            zdi = []
            mezery = ROZLISENI_X/len(vyber[0])
            mezery_y = ROZLISENI_Y/len(vyber)
            x = y = 0
            for radek in vyber:
                for element in radek:
                    if element == "W":
                        Zed((x, y))
                    if element == "H":
                        hrac1 = player(x + mezery/(h/6),y + mezery_y/(h/6), h)
                    if element == "N":
                        hrac2 = player(x + mezery/(h/6),y + mezery_y/(h/6), h)
                    x += mezery
                y += mezery_y
                x = 0
            if hrac1.rect.y < hrac2.rect.y: 
                poloha = True 
            else: 
                poloha = False
            sprites.add(hrac1,hrac2)
        pygame.display.update()        
        
    #herní logika
        
    p_zmacknuto_ted = stisknuto[pygame.K_p]   

    if in_game_menu == False:
        pohyb_tanku = True 
    else:
        pohyb_tanku = False
    
    if p_zmacknuto_pred_tim !=  p_zmacknuto_ted:
        if p_zmacknuto_ted:
            in_game_menu = not in_game_menu  
    
    p_zmacknuto_pred_tim = p_zmacknuto_ted
          
# vykreslovani ##############################################################################

    okno.fill(RGB)
    sprites.update()
    for zed in zdi:
        pygame.draw.rect(okno, (0, 0, 0), zed.rect)   
    pygame.draw.rect(okno, (255, 8, 0), hrac2.rect)
    pygame.draw.rect(okno, (0, 200, 0), hrac1.rect)
    
# cudliky v pause menu

    if in_game_menu == True:
        aktivni_obrazovka = pause_menu
        pygame.draw.rect(okno, (200, 0, 0), ((305,140), (520,520)))
        pygame.draw.rect(okno, (190, 190, 190), ((315,150), (500,500)))
        
        for cudlik in pause_menu[2]:
            pygame.draw.rect(okno, cudlik[2], (cudlik[0], cudlik[1]))
            
        if cl_exit2[0][0] < pygame.mouse.get_pos()[0] < (cl_exit2[0][0] + cl_exit2[1][0]) and cl_exit2[0][1] < pygame.mouse.get_pos()[1] < (cl_exit2[0][1] + cl_exit2[1][1]) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()
            
        if cl_close3[0][0] < pygame.mouse.get_pos()[0] < (cl_close3[0][0] + cl_close3[1][0]) and cl_close3[0][1] < pygame.mouse.get_pos()[1] < (cl_close3[0][1] + cl_close3[1][1]) and pygame.mouse.get_pressed()[0]:
            aktivni_obrazovka = hlavni_menu
            in_game_menu = False
            Done = False            
            MENU = True
        
        if cl_pin[0][0] < pygame.mouse.get_pos()[0] < (cl_pin[0][0] + cl_pin[1][0]) and cl_pin[0][1] < pygame.mouse.get_pos()[1] < (cl_pin[0][1] + cl_pin[1][1]) and pygame.mouse.get_pressed()[0]:    
            print("ahoj")    

    clockobject = pygame.time.Clock()
    clockobject.tick(rychlost)
    pygame.display.update()