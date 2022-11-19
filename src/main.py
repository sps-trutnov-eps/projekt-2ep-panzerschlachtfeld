# Začátek Panzerschlachtfeld im Labyrinth ##################################################
import pygame, sys, math, random
from os import path
vec = pygame.math.Vector2
# proměnné ##################################################################################

PLAYER_SPEED = 300.0
PLAYER_ROT_SPEED = 250.0

###
ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1080,800
RGB = R, G, B, = 100, 145, 84
h = 30
rychlost = 100
poloha = False
MENU = True
Done = False
pohyb_tanku = True
in_game_menu = False
p_zmacknuto_pred_tim = False
pin = False
povoleni_zmacknuti_cisla = True
zadavani = False
zadavani_overovaciho_pinu = False
cekat = False
pauza_v_menu = False
odezva_nacitani_framu_tanku = 9
tank_frame_ted = 0
tank_posledni_snimek = pygame.Surface((800,608))
clock = pygame.time.Clock()
bila = 255,255,255
cerna = 0,0,0
mapa1_pozadi = pygame.image.load("..\doc\mapa-1.png")
mapa2_pozadi = pygame.image.load("..\doc\mapa-2.png")
mapa3_pozadi = pygame.image.load("..\doc\mapa-3.png")
animovany_tank = pygame.image.load("../doc/animation_tank.png")
#############################################################################################

pygame.font.init()

typ_pisma_hlavni_menu = pygame.font.Font('freesansbold.ttf', 25)
typ_pisma_in_game_menu = pygame.font.SysFont('freesansbold.ttf', 32)
typ_pisma_pin_menu = pygame.font.SysFont('freesansbold.ttf', 250)
typ_pisma_overovaci_menu = pygame.font.SysFont('freesansbold.ttf', 250)
typ_pisma_pin_menu2 = pygame.font.SysFont('freesansbold.ttf', 50)

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
np4 = ((55, 20), (400, 75), (0,0,0), "text" )
cl_exit2 = ((190, 250), (150, 50), (0,0,0), "text")
cl_close3 = ((55, 420), (210, 50), (0,0,0), "text")
cl_pin = ((190, 150), (150, 50), (0,0,0), "text")

#pin menu
pindik = ((780, 525), (0, 0), (0,0,0), "text")
cl_close4 = ((410, 525), (150, 50), (0,0,0), "text")

# obrazovky menu
hlavni_menu = [(190,190,190), "Panzerschlachtfeld", (cl_hl1, cl_hl2, cl_hl3, np1, cl_exit1)]
menu_vyberu = [(190,190,190), "Panzerschlachtfeld", (cl_v1, cl_v2, cl_v3, np2, cl_close1)]
menu_CREDITS = [(190,190,190), "Panzerschlachtfeld", (np3, cl_close2)]
pause_menu = [(190, 190, 0), "Panzerschlachtfeld", (np4, cl_exit2, cl_pin, cl_close3)]
pin_menu = [(170, 170, 170), "Panzerschlachtfeld", (pindik,cl_close4)]
aktivni_obrazovka = hlavni_menu
#  #################################################################################################

def cekaci_menu_animation(animovany_tank):
    global tank_frame_ted, odezva_nacitani_framu_tanku, tank_posledni_snimek
    
    frame_textura_tanku = pygame.Surface((800,608))
    if odezva_nacitani_framu_tanku >= 9:
        frame_textura_tanku.blit(animovany_tank, (0,0), (800*tank_frame_ted, 0, 800, 608))
        tank_posledni_snimek = frame_textura_tanku
        odezva_nacitani_framu_tanku = 0
    else:
        odezva_nacitani_framu_tanku += 1
        frame_textura_tanku = tank_posledni_snimek
    
    if tank_frame_ted >= 15:
        tank_frame_ted = 0
    else:
        tank_frame_ted += 1
    return frame_textura_tanku 

def popisky_k_pin_menu(bila, okno, cerna):
    popisek_pin = typ_pisma_pin_menu2.render('Zadejte 4 místný číselný kód!', True, bila, (170, 170, 170))
    popisek_pinRect = popisek_pin.get_rect()
    popisek_pinRect.center = (670, 270)
    okno.blit(popisek_pin, popisek_pinRect)
    
    nadpis_close4 = typ_pisma_hlavni_menu.render('Close', True, bila, cerna)
    nadpis_close4Rect = nadpis_close4.get_rect()
    nadpis_close4Rect.center = (480, 550)
    okno.blit(nadpis_close4, nadpis_close4Rect)
    
def popisky_k_cekacimu_menu(bila, cerna, okno):
    popisek_odemceni = typ_pisma_pin_menu2.render('Zopakujte vámi zadaný kód, pro odemčení!', True, bila, (211, 194, 139))
    popisek_odemceniRect = popisek_odemceni.get_rect()
    popisek_odemceniRect.center = (547, 100)
    okno.blit(popisek_odemceni, popisek_odemceniRect)

def vykreslovani_policek_v_pinu(okno):
    pygame.draw.rect(okno, (0, 0, 0), ((505,370), (54,5)))
    pygame.draw.rect(okno, (0, 0, 0), ((605,370), (54,5)))
    pygame.draw.rect(okno, (0, 0, 0), ((705,370), (54,5)))
    pygame.draw.rect(okno, (0, 0, 0), ((805,370), (54,5)))
    
def vykreslovani_policek_v_cekacim_menu(okno):
    pygame.draw.rect(okno, (0, 0, 0), ((355,320), (54,5)))
    pygame.draw.rect(okno, (0, 0, 0), ((455,320), (54,5)))
    pygame.draw.rect(okno, (0, 0, 0), ((555,320), (54,5)))
    pygame.draw.rect(okno, (0, 0, 0), ((655,320), (54,5)))
    
def cekaci_obrazovka(okno):
    pygame.draw.rect(okno, (211, 194, 139), ((10,10), (1060,780)))
    
def zapis():
    global povoleni_zmacknuti_cisla
    global zadavani
    global cekat
    global pin_kod
    global zadavani_overovaciho_pinu
    if zadavani == True:
        cislo = None
        if z[pygame.K_KP0] and povoleni_zmacknuti_cisla:
            cislo = 0
            povoleni_zmacknuti_cisla = False
            
        elif z[pygame.K_KP1] and povoleni_zmacknuti_cisla:
            cislo = 1
            povoleni_zmacknuti_cisla = False
            
        elif z[pygame.K_KP2] and povoleni_zmacknuti_cisla:
            cislo = 2
            povoleni_zmacknuti_cisla = False
            
        elif z[pygame.K_KP3] and povoleni_zmacknuti_cisla:
            cislo = 3
            povoleni_zmacknuti_cisla = False
            
        elif z[pygame.K_KP4] and povoleni_zmacknuti_cisla:
            cislo = 4
            povoleni_zmacknuti_cisla = False
            
        elif z[pygame.K_KP5] and povoleni_zmacknuti_cisla:
            cislo = 5
            povoleni_zmacknuti_cisla = False

        elif z[pygame.K_KP6] and povoleni_zmacknuti_cisla:
            cislo = 6
            povoleni_zmacknuti_cisla = False

        elif z[pygame.K_KP7] and povoleni_zmacknuti_cisla:
            cislo = 7
            povoleni_zmacknuti_cisla = False

        elif z[pygame.K_KP8] and povoleni_zmacknuti_cisla:
            cislo = 8
            povoleni_zmacknuti_cisla = False

        elif z[pygame.K_KP9] and povoleni_zmacknuti_cisla:
            cislo = 9
            povoleni_zmacknuti_cisla = False

        if cislo != None:
            pin_kod.append(cislo)

        elif (z[pygame.K_KP0] or z[pygame.K_KP1] or z[pygame.K_KP2] or z[pygame.K_KP3] or z[pygame.K_KP4] or z[pygame.K_KP5] or z[pygame.K_KP6] or z[pygame.K_KP7] or z[pygame.K_KP8] or z[pygame.K_KP9]) and povoleni_zmacknuti_cisla == False:
            pass
        else:
            povoleni_zmacknuti_cisla = True
            
        for i in range(len(pin_kod)):
            povrch = typ_pisma_pin_menu.render("*", True, (0,0,0,))
            okno.blit(povrch, ((i*100)+500,300))
            print(pin_kod)
                
        if len(pin_kod) == 4:
            zadavani = False
            cekat = True
            zadavani_overovaciho_pinu = True
            print(pin_kod)
                
def zobraz_okno(okno):
    pygame.draw.rect(okno, (200, 20, 20), ((365,195), (610,410)))
    pygame.draw.rect(okno, (170, 170, 170), ((370,200), (600,400)))
   
def zapis_pro_overovaci_pin():#načtení dat
    global overovaci_pin_kod
    global povoleni_zmacknuti_cisla
    global zadavani_overovaciho_pinu
    global pin_kod
    global pin
    global cekat
    if zadavani_overovaciho_pinu == True:
        cislo = None
        if z[pygame.K_KP0] and povoleni_zmacknuti_cisla:
            cislo = 0
            povoleni_zmacknuti_cisla = False
            
        elif z[pygame.K_KP1] and povoleni_zmacknuti_cisla:
            cislo = 1
            povoleni_zmacknuti_cisla = False
            
        elif z[pygame.K_KP2] and povoleni_zmacknuti_cisla:
            cislo = 2
            povoleni_zmacknuti_cisla = False
            
        elif z[pygame.K_KP3] and povoleni_zmacknuti_cisla:
            cislo = 3
            povoleni_zmacknuti_cisla = False
            
        elif z[pygame.K_KP4] and povoleni_zmacknuti_cisla:
            cislo = 4
            povoleni_zmacknuti_cisla = False
            
        elif z[pygame.K_KP5] and povoleni_zmacknuti_cisla:
            cislo = 5
            povoleni_zmacknuti_cisla = False

        elif z[pygame.K_KP6] and povoleni_zmacknuti_cisla:
            cislo = 6
            povoleni_zmacknuti_cisla = False

        elif z[pygame.K_KP7] and povoleni_zmacknuti_cisla:
            cislo = 7
            povoleni_zmacknuti_cisla = False

        elif z[pygame.K_KP8] and povoleni_zmacknuti_cisla:
            cislo = 8
            povoleni_zmacknuti_cisla = False

        elif z[pygame.K_KP9] and povoleni_zmacknuti_cisla:
            cislo = 9
            povoleni_zmacknuti_cisla = False

        if cislo != None:
            overovaci_pin_kod.append(cislo)

        elif (z[pygame.K_KP0] or z[pygame.K_KP1] or z[pygame.K_KP2] or z[pygame.K_KP3] or z[pygame.K_KP4] or z[pygame.K_KP5] or z[pygame.K_KP6] or z[pygame.K_KP7] or z[pygame.K_KP8] or z[pygame.K_KP9]) and povoleni_zmacknuti_cisla == False:
            pass
        else:
            povoleni_zmacknuti_cisla = True
            
    for i in range(len(overovaci_pin_kod)):
        povrch2 = typ_pisma_pin_menu.render("*", True, (0,0,0,))
        okno.blit(povrch2, ((i*100)+350,250))
        print(overovaci_pin_kod)
                
        if len(overovaci_pin_kod) == 4:
            zadavani_overovaciho_pinu = False
            print(overovaci_pin_kod)
            if pin_kod == overovaci_pin_kod:
                overovaci_pin_kod = []
                cekat = False
                pin = False
                pin_kod = []
                
            else:
                overovaci_pin_kod = []
                zadavani_overovaciho_pinu = True
                
class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        #šablona
        pygame.sprite.Sprite.__init__(self)
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, '../doc')
        self.player_img = pygame.image.load(path.join(img_folder, "Tank.png")).convert_alpha()
        self.image = self.player_img
        self.rect = self.image.get_rect()
        self.image.set_colorkey(cerna)
        
        #pro vnější kód
        self.rect.x = x
        self.rect.y = y
             
        #pro loop, kolizi apod#
        self.rychlost1 = 0 
        self.rychlost2 = 0
        self.dt = 60/100000
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot1 = 180
        self.rot2 = 0
        
    def update(self):
        self.rychlost1 = 0
        self.rychlost2 = 0
        self.rot_speed1 = 0
        self.rot_speed2 = 0
        self.vel = vec(0, 0)
       
        ##pohyb
        if stisknuto[pygame.K_UP]:
            self.rychlost1 += -PLAYER_SPEED
        if stisknuto[pygame.K_DOWN]:
            self.rychlost1 += PLAYER_SPEED/2
        if stisknuto[pygame.K_LEFT]:
            self.rot_speed1 = PLAYER_ROT_SPEED
        if stisknuto[pygame.K_RIGHT]:
            self.rot_speed1 = -PLAYER_ROT_SPEED
         
        if stisknuto[pygame.K_w]:
            self.rychlost2 += -PLAYER_SPEED
        if stisknuto[pygame.K_s]:
            self.rychlost2 += PLAYER_SPEED/2
        if stisknuto[pygame.K_a]:
            self.rot_speed2 = PLAYER_ROT_SPEED
        if stisknuto[pygame.K_d]:
            self.rot_speed2 = -PLAYER_ROT_SPEED
        
        self.rot1 = (self.rot1 + self.rot_speed1 * self.dt) % 360
        self.rot2 = (self.rot2 + self.rot_speed2 * self.dt) % 360
        
        #kolize        
        if pohyb_tanku:
            if poloha:
                hrac1.vel = vec(0, hrac1.rychlost1).rotate(-self.rot1)
                hrac1.image = pygame.transform.rotate(self.player_img, self.rot1)
                hrac2.vel = vec(0, hrac2.rychlost2).rotate(-self.rot2)
                hrac2.image = pygame.transform.rotate(self.player_img, self.rot2)
            else:
                hrac1.vel = vec(0, hrac1.rychlost2).rotate(-self.rot2)
                hrac1.image = pygame.transform.rotate(self.player_img, self.rot2)
                hrac2.vel = vec(0, hrac2.rychlost1).rotate(-self.rot1)
                hrac2.image = pygame.transform.rotate(self.player_img, self.rot1)    
        else:
            pass
        
        self.rect = self.image.get_rect()
        hrac1.image.set_colorkey(cerna)
        hrac2.image.set_colorkey(cerna)
        self.pos += self.vel * self.dt
        self.rect.center = self.pos
       
class Zed(object): #jakákoliv classa s VELKÝM počátčním písmenem SAMEEEEEEEEEEE!!!
    
    def __init__(self, pos):
        zdi.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], mezery +1 , mezery_y +1 )

##################################################################################################

overovaci_pin_kod = []
pin_kod = []
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
"WW    W   N   W    W",
"W  W             W W",
"W  W  WWWWWWWWW  W W",
"W  W      W      W W",
"W  W   WW   WW  W  W",
"W  W      W      W W",
"W  W  WWWWWWWWW  W W",
"W  W             W W",
"WW    W   H   W    W",
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
    z = pygame.key.get_pressed()
    
    udalosti = pygame.event.get()
    for u in udalosti:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    stisknuto = pygame.key.get_pressed()
    if stisknuto[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
        
# menu a pod. ###############################################################################
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
            hl_nadpis1 = typ_pisma_hlavni_menu.render('Panzerschlachtfeld im Labyrinth:', True, bila, cerna)
            hl_nadpis1Rect = hl_nadpis1.get_rect()
            hl_nadpis1Rect.center = (550, 128)
    
            nadpis_menu1 = typ_pisma_hlavni_menu.render('Vybrat mapu', True, bila, cerna)
            nadpis_menu1Rect = nadpis_menu1.get_rect()
            nadpis_menu1Rect.center = (560, 308)
            
            
            nadpis_menu2 = typ_pisma_hlavni_menu.render('Náhodná mapa', True, bila, cerna)
            nadpis_menu2Rect = nadpis_menu2.get_rect()
            nadpis_menu2Rect.center = (560, 488)
            

            nadpis_menu3 = typ_pisma_hlavni_menu.render('CREDITS', True, bila, cerna)
            nadpis_menu3Rect = nadpis_menu3.get_rect()
            nadpis_menu3Rect.center = (560, 668)
            
            nadpis_exit = typ_pisma_hlavni_menu.render('EXIT', True, bila, cerna)
            nadpis_exitRect = nadpis_exit.get_rect()
            nadpis_exitRect.center = (1000, 750)
        
        if aktivni_obrazovka == menu_vyberu:
            hl_nadpis2 = typ_pisma_hlavni_menu.render('Panzerschlachtfeld im Labyrinth:', True, bila, cerna)
            hl_nadpis2Rect = hl_nadpis2.get_rect()
            hl_nadpis2Rect.center = (550, 88)
            
            nadpis_close1 = typ_pisma_hlavni_menu.render('CLOSE', True, bila, cerna)
            nadpis_close1Rect = nadpis_close1.get_rect()
            nadpis_close1Rect.center = (100, 750)
        
        if aktivni_obrazovka == menu_CREDITS:
            hl_nadpis3 = typ_pisma_hlavni_menu.render('Panzerschlachtfeld im Labyrinth:', True, bila, cerna)
            hl_nadpis3Rect = hl_nadpis3.get_rect()
            hl_nadpis3Rect.center = (550, 88)
            
            nadpis_close2 = typ_pisma_hlavni_menu.render('CLOSE', True, bila, cerna)
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
                        hrac1 = Player(x + mezery/(h/15),y + mezery/(h/21.8))
                    if element == "N":
                        hrac2 = Player(x + mezery/(h/15),y + mezery/(h/21.8))
                    x += mezery
                y += mezery_y
                x = 0
            if hrac1.rect.y < hrac2.rect.y: 
                poloha = True 
            else: 
                poloha = False
            sprites.add(hrac1,hrac2)
            
        pygame.display.update()        
        
########## herní logika ################################################################################################
        
    p_zmacknuto_ted = stisknuto[pygame.K_p]

    if in_game_menu == False:
        pohyb_tanku = True 
    else:
        pohyb_tanku = False
    
    if p_zmacknuto_pred_tim !=  p_zmacknuto_ted:
        if p_zmacknuto_ted:
            in_game_menu = not in_game_menu  
    
    p_zmacknuto_pred_tim = p_zmacknuto_ted
          
######## vykreslovani ##############################################################################################

    okno.fill(RGB)
    sprites.update()
    for zed in zdi:
        pygame.draw.rect(okno, (0, 0, 0), zed.rect)   
    sprites.draw(okno)
    
# cudliky v pause menu ################################################################################################ 
    
    if in_game_menu == True:
        aktivni_obrazovka = pause_menu
        pygame.draw.rect(okno, (200, 0, 0), ((0,0), (520,520)))
        pygame.draw.rect(okno, (190, 190, 190), ((10,10), (500,500)))
        
        for cudlik in pause_menu[2]:
            pygame.draw.rect(okno, cudlik[2], (cudlik[0], cudlik[1]))
            
        if cl_exit2[0][0] < pygame.mouse.get_pos()[0] < (cl_exit2[0][0] + cl_exit2[1][0]) and cl_exit2[0][1] < pygame.mouse.get_pos()[1] < (cl_exit2[0][1] + cl_exit2[1][1]) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()
            
        if cl_close3[0][0] < pygame.mouse.get_pos()[0] < (cl_close3[0][0] + cl_close3[1][0]) and cl_close3[0][1] < pygame.mouse.get_pos()[1] < (cl_close3[0][1] + cl_close3[1][1]) and pygame.mouse.get_pressed()[0]:
            aktivni_obrazovka = hlavni_menu
            in_game_menu = False
            Done = False
            hrac1.kill()
            hrac2.kill()
            MENU = True
        
        hl_nadpis4 = typ_pisma_in_game_menu.render('Panzerschlachtfeld im Labyrinth:', True, bila, cerna)
        hl_nadpis4Rect = hl_nadpis4.get_rect()
        hl_nadpis4Rect.center = (255, 55)
        
        nadpis_exit1 = typ_pisma_in_game_menu.render('Exit', True, bila, cerna)
        nadpis_exit1Rect = nadpis_exit1.get_rect()
        nadpis_exit1Rect.center = (265, 275)
        
        nadpis_close3 = typ_pisma_in_game_menu.render('Zpátky do menu', True, bila, cerna)
        nadpis_close3Rect = nadpis_close3.get_rect()
        nadpis_close3Rect.center = (160, 445)
        
        nadpis_pin = typ_pisma_in_game_menu.render('Pauza', True, bila, cerna)
        nadpis_pinRect =  nadpis_pin.get_rect()
        nadpis_pinRect.center = (265, 175)
        
        okno.blit(nadpis_pin, nadpis_pinRect)
        okno.blit(nadpis_exit1, nadpis_exit1Rect)
        okno.blit(nadpis_close3, nadpis_close3Rect)
        okno.blit(hl_nadpis4, hl_nadpis4Rect)
              
########################
        mys_zmacknuta_ted = pygame.mouse.get_pressed()[0]   
        if pin == True:
            zobraz_okno(okno) 
            aktivni_obrazovka = pin_menu
            for cudlik in pin_menu[2]:
                pygame.draw.rect(okno, cudlik[2], ((cudlik[0]), (cudlik[1])))
            vykreslovani_policek_v_pinu(okno)
            zapis()
            popisky_k_pin_menu(bila, okno, cerna)
            
            if cl_close4[0][0] < pygame.mouse.get_pos()[0] < (cl_close4[0][0] + cl_close4[1][0]) and cl_close4[0][1] < pygame.mouse.get_pos()[1] < (cl_close4[0][1] + cl_close4[1][1]) and pygame.mouse.get_pressed()[0]:
                pin = False
                pin_kod = []
##########################
                
        if cekat == True:
            pygame.draw.rect(okno, (200, 20, 20), ((0, 0), (1080, 800)))
            cekaci_obrazovka(okno)
            okno.blit(cekaci_menu_animation(animovany_tank), (80, 80))
            vykreslovani_policek_v_cekacim_menu(okno)
            zapis_pro_overovaci_pin()
            popisky_k_cekacimu_menu(bila, cerna, okno)
        
        if cl_pin[0][0] < pygame.mouse.get_pos()[0] < (cl_pin[0][0] + cl_pin[1][0]) and cl_pin[0][1] < pygame.mouse.get_pos()[1] < (cl_pin[0][1] + cl_pin[1][1]) and pygame.mouse.get_pressed()[0]:
            if mys_zmacknuta_ted:
                pin = True
            zadavani = True
    
    pygame.display.update()
    clock.tick(70)