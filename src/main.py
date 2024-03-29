# Začátek Panzerschlachtfeld im Labyrinth ##################################################
import pygame, sys, math, random
from os import path
vec = pygame.math.Vector2
# proměnné ##################################################################################
#hráč
speed = 300
PLAYER_ROT_SPEED = 250.0
obr = "Tank.png"
cekat_do_nove = 0
znovu = 3000
odpocet = int(znovu/1000) + 1
cas_na_spawn_abilitek = 17500

#nesahat
PLAYER_SPEED = 0
odpocet_odpoctu = 0
abilitky_spawn = 0
spawn_bool = True
time_p = False
#speed up, shotgun, freeze, síťová karta, z ničeho nic.
typy_abilitek = ["Speed_UP","Shotgun","Freeze","NIC"]
uhly = [80,90,100]
#střely
strela_img = "bullet.png"
strela_speed = 350
strela_lifetime = 4000
strela_delay = 3500
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
zpatky_do_menu = False
odchod_ze_hry = False
varovani = False
vykreslovani_skore_sever = False
skore = False
skorovani_sever = 0
skorovani_jih = 2
odezva_nacitani_framu_tanku = 9
tank_frame_ted = 0
tank_posledni_snimek = pygame.Surface((800,608))
clock = pygame.time.Clock()
bila = 255,255,255
cerna = 0,0,0
cervena = 237, 28, 36
mapa1_pozadi = pygame.image.load("..\doc\mapa-1.png")
mapa2_pozadi = pygame.image.load("..\doc\mapa-2.png")
mapa3_pozadi = pygame.image.load("..\doc\mapa-3.png")
animovany_tank = pygame.image.load("../doc/animation_tank.png")
#############################################################################################

pygame.font.init()

typ_pisma_skore = pygame.font.Font('freesansbold.ttf', 48)
typ_pisma_hlavni_menu = pygame.font.Font('freesansbold.ttf', 30)
typ_pisma_in_game_menu = pygame.font.SysFont('freesansbold.ttf', 32)
typ_pisma_pin_menu = pygame.font.SysFont('freesansbold.ttf', 250)
typ_pisma_pin_menu2 = pygame.font.SysFont('freesansbold.ttf', 50)
typ_pisma_text_skore = pygame.font.Font('freesansbold.ttf', 30)
typ_pisma_odpocet = pygame.font.Font('freesansbold.ttf', 300)
typ_pisma_text_napoveda = pygame.font.Font('freesansbold.ttf', 30)

# cudliky
#hlavní menu
np1 = ((0,80), (1080,100), (0,0,0), "text" )
cl_hl1 = ((375, 255), (375, 100), (0,0,0), "text")
cl_hl2 = ((375, 435), (375, 100), (0,0,0), "text")
cl_hl3 = ((375, 615), (375, 100), (0,0,0), "text")
cl_exit1 = ((925, 720), (150, 50), (0,0,0), "text")
napoveda = ((20, 200), (50, 50), (180,0,0), "text")

#menu výběru
np2 = ((0, 40), (1080,100), (0,0,0), "text" )
cl_close1 = ((25, 725), (150, 50), (0,0,0), "text")
cl_v1 = ((155, 350), (150, 150), (0,0,0), "text")
cl_v2 = ((460, 350), (150, 150), (0,0,0), "text")
cl_v3 = ((765, 350), (150, 150), (0,0,0), "text")

#menu credits
np3 = ((0, 40), (1080,100), (0,0,0), "text" )
cl_close2 = ((25, 725), (150, 50), (0,0,0), "text")
 
#ingame menu
np4 = ((10, 20), (500, 75), (0,0,0), "text" )
cl_exit2 = ((190, 250), (150, 50), (0,0,0), "text")
cl_close3 = ((55, 420), (210, 50), (0,0,0), "text")
cl_pin = ((190, 150), (150, 50), (0,0,0), "text")

#pin menu
pindik = ((780, 525), (0, 0), (0,0,0), "text")
cl_close4 = ((410, 525), (150, 50), (0,0,0), "text")

#okno vyhra
cl_pokracovat =  ((600, 570), (150, 50), (0,0,0), "text")
cl_exit3 = ((330, 570), (150, 50), (0,0,0), "text")


# obrazovky menu
hlavni_menu = [(190,190,190), "Panzerschlachtfeld", (cl_hl1, cl_hl2, cl_hl3, np1, cl_exit1, napoveda)]
menu_vyberu = [(190,190,190), "Panzerschlachtfeld", (cl_v1, cl_v2, cl_v3, np2, cl_close1)]
menu_CREDITS = [(190,190,190), "Panzerschlachtfeld", (np3, cl_close2)]
pause_menu = [(190, 190, 0), "Panzerschlachtfeld", (np4, cl_exit2, cl_pin, cl_close3)]
pin_menu = [(170, 170, 170), "Panzerschlachtfeld", (pindik,cl_close4)]
menu_skore = [(170, 170, 170), "Panzerschlachtfeld", (cl_pokracovat,cl_exit3)]
menu_napoveda = [(170, 170, 170), "Panzerschlachtfeld", (cl_close2, np3)]
aktivni_obrazovka = hlavni_menu
#  #################################################################################################
def skore_sever(bila, cerna, cervena):
    global skorovani_sever 
    text_skore_sever = typ_pisma_skore.render(str(skorovani_sever) + ':', True, bila)
    text_skore_severRect = text_skore_sever.get_rect()
    text_skore_severRect.center = (510, 30)
    okno.blit(text_skore_sever, text_skore_severRect)
    
    text_sever = typ_pisma_text_skore.render('Sever', True, cervena, cerna)
    text_severRect = text_sever.get_rect()
    text_severRect.center = (420, 36)
    okno.blit(text_sever,text_severRect)
    
    if stisknuto[pygame.K_k] and skorovani_sever <= 2:
        skorovani_sever += 1
    
def skore_jih(bila, cerna, cervena):
    global skorovani_jih
    text_skore_jih = typ_pisma_skore.render(str(skorovani_jih) + ' ', True, bila)
    text_skore_jihRect = text_skore_jih.get_rect()
    text_skore_jihRect.center = (555, 30)
    okno.blit(text_skore_jih, text_skore_jihRect)
    
    text_jih = typ_pisma_text_skore.render('Jih', True, cervena, cerna)
    text_jihRect = text_jih.get_rect()
    text_jihRect.center = (610, 36)
    okno.blit(text_jih,text_jihRect)

    if stisknuto[pygame.K_l] and skorovani_jih <= 2 :
        skorovani_jih += 1

def kontrola_skore(okno):
    global skorovani_jih, skorovani_sever, menu_skore, MENU, Done, hlavni_menu, in_game_menu, aktivni_obrazovka
    
    if skorovani_jih == 3 and skorovani_sever <= 2 or skorovani_jih > 3 and skorovani_sever <= 2:
        pygame.draw.rect(okno, (200, 20, 20), ((280,140), (520,520)))
        pygame.draw.rect(okno, (180, 180, 180), ((290,150), (500,500)))
        
        text_jih_vyhra = typ_pisma_skore.render("Jižní linie vyhrála", True, (0, 255, 255), (180, 180 ,180))
        text_jih_vyhraRect = text_jih_vyhra.get_rect()
        text_jih_vyhraRect.center = (540, 250)
        okno.blit(text_jih_vyhra, text_jih_vyhraRect)
        
        for cudlik in menu_skore[2]:
            pygame.draw.rect(okno, cudlik[2], (cudlik[0], cudlik[1]))
        
        popisky_k_vyhernimu_oknu(okno, bila, cerna)
        
        if cl_pokracovat[0][0] < pygame.mouse.get_pos()[0] < (cl_pokracovat[0][0] + cl_pokracovat[1][0]) and cl_pokracovat[0][1] < pygame.mouse.get_pos()[1] < (cl_pokracovat[0][1] + cl_pokracovat[1][1]) and pygame.mouse.get_pressed()[0]:
            hrac1.tanky_kolize = False
            hrac2.tanky_kolize = False 
            skorovani_jih = 0
            skorovani_sever = 0
            
        if cl_exit3[0][0] < pygame.mouse.get_pos()[0] < (cl_exit3[0][0] + cl_exit3[1][0]) and cl_exit3[0][1] < pygame.mouse.get_pos()[1] < (cl_exit3[0][1] + cl_exit3[1][1]) and pygame.mouse.get_pressed()[0]:
            MENU = True
            Done = False
            hrac1.kill()
            hrac2.kill()
            aktivni_obrazovka = hlavni_menu
            
    if skorovani_sever == 3 and skorovani_jih <= 2 or skorovani_sever > 3 and skorovani_jih <= 2:
        pygame.draw.rect(okno, (200, 20, 20), ((280,140), (520,520)))
        pygame.draw.rect(okno, (180, 180, 180), ((290,150), (500,500)))
        
        text_sever_vyhra = typ_pisma_skore.render("Severní linie vyhrála", True, (0, 255, 255), (180, 180 ,180))
        text_sever_vyhraRect = text_sever_vyhra.get_rect()
        text_sever_vyhraRect.center = (540, 250)
        okno.blit(text_sever_vyhra, text_sever_vyhraRect)
        
        for cudlik in menu_skore[2]:
            pygame.draw.rect(okno, cudlik[2], (cudlik[0], cudlik[1]))
         
        popisky_k_vyhernimu_oknu(okno, bila, cerna)
        
        if cl_pokracovat[0][0] < pygame.mouse.get_pos()[0] < (cl_pokracovat[0][0] + cl_pokracovat[1][0]) and cl_pokracovat[0][1] < pygame.mouse.get_pos()[1] < (cl_pokracovat[0][1] + cl_pokracovat[1][1]) and pygame.mouse.get_pressed()[0]:
            hrac1.tanky_kolize = False
            hrac2.tanky_kolize = False
            skorovani_jih = 0
            skorovani_sever = 0
            
        if cl_exit3[0][0] < pygame.mouse.get_pos()[0] < (cl_exit3[0][0] + cl_exit3[1][0]) and cl_exit3[0][1] < pygame.mouse.get_pos()[1] < (cl_exit3[0][1] + cl_exit3[1][1]) and pygame.mouse.get_pressed()[0]:
            MENU = True
            Done = False
            hrac1.kill()
            hrac2.kill()
            aktivni_obrazovka = hlavni_menu

def cekaci_menu_animation(animovany_tank, clock):
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
    clock.tick(80)

    return frame_textura_tanku
    
def pipsiky_k_credits(okno, bila, cerna):
    simon = typ_pisma_pin_menu2.render('Šimon - tvůrce map a všeho co se týče menu.', True, cerna)
    sam = typ_pisma_pin_menu2.render('Samuel - fungování hry, kolize, střely, tanky, otáčení', True, cerna) 
    pavel = typ_pisma_pin_menu2.render('Pavel - pomoc s debuggingem a s vytvoření menu', True, cerna)
    karel = typ_pisma_pin_menu2.render('Karel - texturář', True, cerna)
    
    okno.blit(sam, (50, 200))
    okno.blit(simon, (50, 300))
    okno.blit(pavel, (50, 400))
    okno.blit(karel, (50, 500))

def text_napoveda(okno, bila, cerna):
    prvni_radek = typ_pisma_text_napoveda.render('- Toto je hra pro 2 hráče. Tanky se ovládají pomocí WASD a střelba', True, cerna)
    prvni_radek1 = typ_pisma_text_napoveda.render(' pomocí mezerníku, pro severní tank.', True, cerna)
    druhy_radek = typ_pisma_text_napoveda.render('- Jižní tank se ovládá pomocí šipek a střelba pomocí enteru', True, cerna)
    druhy_radek1 = typ_pisma_text_napoveda.render(' u numerické části klávesnice.', True, cerna)
    treti_radek = typ_pisma_text_napoveda.render('- Střely se odrážejí od stěn.', True, cerna)
    ctvrty_radek = typ_pisma_text_napoveda.render('- Na mapě se po časovém intervalu začnou objevovat abilities.', True, cerna)
    ctvrty_radek1 = typ_pisma_text_napoveda.render(' Když je seberete tak neuvidíte co přesně jste sebrali.', True, cerna)
    paty_radek = typ_pisma_text_napoveda.render('- Brokovnice- vystřelí 3 rány vedle sebe', True, cerna)
    sesty_radek = typ_pisma_text_napoveda.render('- Speed- zrychlí tank na 7.5 sekundy', True, cerna)
    sedmy_radek = typ_pisma_text_napoveda.render('- Freeze- zmrazí druhému hráči dělo na 7.5 sekundy', True, cerna)
    devaty_radek = typ_pisma_text_napoveda.render('- Hra končí po 3 vyhraných kolech pro jednu stranu.', True, cerna)
    desaty_radek = typ_pisma_text_napoveda.render('- Zmáčknutím p se dostanete do sekundárního menu hry.', True, cerna)
    
    okno.blit(prvni_radek, (15, 180))
    okno.blit(prvni_radek1, (15, 215))
    okno.blit(druhy_radek, (15, 270))
    okno.blit(druhy_radek1,(15, 305))
    okno.blit(desaty_radek, (15, 355))
    okno.blit(treti_radek, (15, 405))
    okno.blit(devaty_radek, (15, 455))
    okno.blit(ctvrty_radek, (15, 505))
    okno.blit(ctvrty_radek1, (15, 545))
    okno.blit(paty_radek, (15, 595))
    okno.blit(sesty_radek, (15, 635))
    okno.blit(sedmy_radek, (15, 675))
    
def popisky_k_vyhernimu_oknu(okno, bila, cerna):
    popisek_exit = typ_pisma_pin_menu2.render('Exit', True, bila, cerna)
    popisek_exitRect = popisek_exit.get_rect()
    popisek_exitRect.center = (400, 595)
    okno.blit(popisek_exit, popisek_exitRect)
    
    popisek_znovu = typ_pisma_pin_menu2.render('Znovu', True, bila, cerna)
    popisek_znovuRect = popisek_znovu.get_rect()
    popisek_znovuRect.center = (675, 595)
    okno.blit(popisek_znovu, popisek_znovuRect)

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
                
        if len(pin_kod) == 4:
            zadavani = False
            cekat = True
            zadavani_overovaciho_pinu = True
                
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
    global varovani
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
            
    if varovani == True:
        nadpis_varovani = typ_pisma_hlavni_menu.render('Špatně zadaný pin, zkuste to znovu', True, cervena, (211, 194, 139))
        nadpis_varovaniRect = nadpis_varovani.get_rect()
        nadpis_varovaniRect.center = (547, 170)
        okno.blit(nadpis_varovani, nadpis_varovaniRect)
            
    for i in range(len(overovaci_pin_kod)):
        povrch2 = typ_pisma_pin_menu.render("*", True, (0,0,0,))
        okno.blit(povrch2, ((i*100)+350,250))
                
        if len(overovaci_pin_kod) == 4:
            zadavani_overovaciho_pinu = False
            if pin_kod == overovaci_pin_kod:
                overovaci_pin_kod = []
                varovani = False
                cekat = False
                pin = False
                pin_kod = []
            else:
                overovaci_pin_kod = []
                zadavani_overovaciho_pinu = True
                varovani = True
                
class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y, obr):
        #šablona
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, '../doc')
        pygame.sprite.Sprite.__init__(self)
        self.player_img = pygame.image.load(path.join(img_folder, obr)).convert_alpha()
        self.image = self.player_img
        self.rect = self.image.get_rect()
        self.image.set_colorkey(cerna)
        
        #pro vnější kód
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        
        #pro loop, kolizi apod#
        self.abilita_freeze_sebrana = False
        self.abilita_speed_sebrana = False
        self.h = self.rect.h
        self.kontrola = vec(0,0)
        self.povoleni = True
        self.tanky_kolize = True
        self.strela_kolize = True
        
        self.otaceni = True
        self.rychlost1 = 0 
        self.rychlost2 = 0
        self.dt = 60/100000
        self.zrychleni = 1
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot1 = 0
        self.rot2 = 180
        self.last_shot = -strela_delay
        global strela_lifetime
        
        #freeze a abilitky
        self.shotgun = False
        self.casovac_freeze = 0
        self.casovac_speed = 0
        self.cas = 0
        
    def kolize(self):
        if poloha == False:
            hrac2.kontrola = hrac2.pos + vec(0,hrac2.h/1.75 + 11).rotate(-self.rot2 - 180)
            hrac1.kontrola = hrac1.pos + vec(0,hrac1.h/1.75 + 11).rotate(-self.rot1 - 180)
        else:
            hrac1.kontrola = hrac1.pos + vec(0,hrac1.h/1.75 + 11).rotate(-self.rot2 - 180)
            hrac2.kontrola = hrac2.pos + vec(0,hrac2.h/1.75 + 11).rotate(-self.rot1 - 180)
            
        #se stranama
        if self.pos.x + self.rect.w/2 > ROZLISENI_X:
            self.pos.x = ROZLISENI_X - self.rect.w/2
        if self.pos.x - self.rect.w/2 < 0:
            self.pos.x = self.rect.w/2
        if self.pos.y + self.rect.h/2 > ROZLISENI_Y :
            self.pos.y = ROZLISENI_Y - self.rect.h/2
        if self.pos.y - self.rect.h/2 < 0:
            self.pos.y = self.rect.h/2
       
        if self.tanky_kolize:
            if hrac2.rect.x + hrac2.rect.w + 0.25 > hrac1.rect.x + hrac1.rect.w and hrac2.rect.x - 0.25 < hrac1.rect.x + hrac1.rect.w  and hrac2.rect.y + hrac2.rect.h + 0.25 > hrac1.rect.y and hrac2.rect.y - 0.25 < hrac1.rect.y or hrac2.rect.x + hrac2.rect.w + 0.25 > hrac1.rect.x and hrac2.rect.x - 0.25 < hrac1.rect.x and hrac2.rect.y + hrac2.rect.h + 0.25 > hrac1.rect.y + hrac1.rect.h and hrac2.rect.y - 0.25 < hrac1.rect.y + hrac1.rect.h or hrac2.rect.x + hrac2.rect.w + 0.25 > hrac1.rect.x and hrac2.rect.x - 0.25 < hrac1.rect.x and hrac2.rect.y + hrac2.rect.h + 0.25 > hrac1.rect.y and hrac2.rect.y - 0.25 < hrac1.rect.y or hrac2.rect.x + hrac2.rect.w + 0.25 > hrac1.rect.x + hrac1.rect.w and hrac2.rect.x - 0.25 < hrac1.rect.x + hrac1.rect.w and hrac2.rect.y + hrac2.rect.h + 0.25 > hrac1.rect.y + hrac1.rect.h and hrac2.rect.y - 0.25 < hrac1.rect.y + hrac1.rect.h or hrac1.rect.x + hrac1.rect.w + 0.25 > hrac2.rect.x + hrac2.rect.w and hrac1.rect.x - 0.25 < hrac2.rect.x + hrac2.rect.w  and hrac1.rect.y + hrac1.rect.h + 0.25 > hrac2.rect.y and hrac1.rect.y - 0.25 < hrac2.rect.y or hrac1.rect.x + hrac1.rect.w + 0.25 > hrac2.rect.x and hrac1.rect.x - 0.25 < hrac2.rect.x and hrac1.rect.y + hrac1.rect.h + 0.25 > hrac2.rect.y + hrac2.rect.h and hrac1.rect.y - 0.25 < hrac2.rect.y + hrac2.rect.h or hrac1.rect.x + hrac1.rect.w + 0.25 > hrac2.rect.x and hrac1.rect.x - 0.25 < hrac2.rect.x and hrac1.rect.y + hrac1.rect.h + 0.25 > hrac2.rect.y and hrac1.rect.y - 0.25 < hrac2.rect.y or hrac1.rect.x + hrac1.rect.w + 0.25 > hrac2.rect.x + hrac2.rect.w and hrac1.rect.x - 0.25 < hrac2.rect.x + hrac2.rect.w and hrac1.rect.y + hrac1.rect.h + 0.25 > hrac2.rect.y + hrac2.rect.h and hrac1.rect.y - 0.25 < hrac2.rect.y + hrac2.rect.h:
                hrac1.otaceni = False
                hrac2.otaceni = False
                
            # tanky mezi sebou    
            if pygame.Rect.colliderect(hrac1.rect, hrac2.rect):

                if hrac1.rect.x > hrac2.rect.x + hrac2.rect.width / 2 and hrac2.rect.x + hrac2.rect.w - 1.45 < hrac1.rect.x :
                       hrac2.pos.x = hrac1.rect.x - hrac2.rect.width / 2
                       hrac1.pos.x = hrac2.rect.right + hrac1.rect.width / 2
                if hrac1.rect.x + hrac1.rect.w - 1.45 < hrac2.rect.x and hrac2.rect.x > hrac1.rect.x + hrac1.rect.width / 2:
                       hrac1.pos.x = hrac2.rect.x - hrac1.rect.width / 2
                       hrac2.pos.x = hrac1.rect.right + hrac2.rect.width / 2
                if hrac2.rect.y > hrac1.rect.y + hrac1.rect.h - 1.45 and hrac1.rect.y + hrac1.rect.h - 1.45 < hrac2.rect.y:
                       hrac2.pos.y = hrac1.rect.bottom + hrac2.rect.h / 2
                       hrac1.pos.y = hrac2.rect.top - hrac1.rect.h / 2
                if hrac1.rect.y > hrac2.rect.y + hrac2.rect.h - 1.45 and hrac2.rect.y + hrac2.rect.h - 1.45 < hrac1.rect.y:
                       hrac1.pos.y = hrac2.rect.bottom + hrac1.rect.h / 2
                       hrac2.pos.y = hrac1.rect.top - hrac2.rect.h / 2
            
        for zed in zdi:
            #kolize pro střely
            if hrac1.kontrola.x > zed.rect.x and hrac1.kontrola.x < zed.rect.x + zed.rect.w and hrac1.kontrola.y > zed.rect.y and hrac1.kontrola.y < zed.rect.y + zed.rect.h:
               hrac1.povoleni = False
            if hrac2.kontrola.x > zed.rect.x and hrac2.kontrola.x < zed.rect.x + zed.rect.w and hrac2.kontrola.y > zed.rect.y and hrac2.kontrola.y < zed.rect.y + zed.rect.h:
               hrac2.povoleni = False
                
            if zed.rect.x + zed.rect.w > hrac1.rect.x + hrac1.rect.w and zed.rect.x - 0.5 < hrac1.rect.x + hrac1.rect.w  and zed.rect.y + zed.rect.h > hrac1.rect.y and zed.rect.y - 0.5 < hrac1.rect.y or zed.rect.x + zed.rect.w > hrac1.rect.x and zed.rect.x - 0.5 < hrac1.rect.x and zed.rect.y + zed.rect.h > hrac1.rect.y + hrac1.rect.h and zed.rect.y - 0.5 < hrac1.rect.y + hrac1.rect.h or zed.rect.x + zed.rect.w > hrac1.rect.x and zed.rect.x - 0.5 < hrac1.rect.x and zed.rect.y + zed.rect.h > hrac1.rect.y and zed.rect.y - 0.5 < hrac1.rect.y or zed.rect.x + zed.rect.w > hrac1.rect.x + hrac1.rect.w and zed.rect.x - 0.5 < hrac1.rect.x + hrac1.rect.w and zed.rect.y + zed.rect.h > hrac1.rect.y + hrac1.rect.h and zed.rect.y - 0.5 < hrac1.rect.y + hrac1.rect.h:
                hrac1.otaceni = False
            if zed.rect.x + zed.rect.w > hrac2.rect.x + hrac2.rect.w and zed.rect.x - 0.5 < hrac2.rect.x + hrac2.rect.w  and zed.rect.y + zed.rect.h > hrac2.rect.y and zed.rect.y - 0.5 < hrac2.rect.y or zed.rect.x + zed.rect.w > hrac2.rect.x and zed.rect.x - 0.5 < hrac2.rect.x and zed.rect.y + zed.rect.h > hrac2.rect.y + hrac2.rect.h and zed.rect.y - 0.5 < hrac2.rect.y + hrac2.rect.h or zed.rect.x + zed.rect.w > hrac2.rect.x and zed.rect.x - 0.5 < hrac2.rect.x and zed.rect.y + zed.rect.h > hrac2.rect.y and zed.rect.y - 0.5 < hrac2.rect.y or zed.rect.x + zed.rect.w > hrac2.rect.x + hrac2.rect.w and zed.rect.x - 0.5 < hrac2.rect.x + hrac2.rect.w and zed.rect.y + zed.rect.h > hrac2.rect.y + hrac2.rect.h and zed.rect.y - 0.5 < hrac2.rect.y + hrac2.rect.h:
                hrac2.otaceni = False
                
            if pygame.Rect.colliderect(self.rect, zed.rect):
                seznam_delicu_y = [self.rect.h,1,2,1.5,4,5]
                seznam_delicu_w = [self.rect.w,1,2,1.5,4,5]
                for delic_y in seznam_delicu_y:
                    for delic_w in seznam_delicu_w:
                        #pravá strana zdi a levá playera
                        if self.rect.x < zed.rect.x + zed.rect.w and self.rect.x > zed.rect.x + zed.rect.w - zed.rect.w/4 and self.rect.y + (self.rect.h/delic_y) > zed.rect.y + zed.rect.h/25 and self.rect.y + (self.rect.h/delic_y) < zed.rect.y + zed.rect.h - zed.rect.h/25:
                            self.pos.x = zed.rect.right + self.rect.width / 2
                        #levá strana zdi a pravá playera
                        if self.rect.x + self.rect.w > zed.rect.x and self.rect.x + self.rect.w < zed.rect.x + zed.rect.w/4 and self.rect.y + (self.rect.h/delic_y) > zed.rect.y + zed.rect.h/25 and self.rect.y + (self.rect.h/delic_y) < zed.rect.y + zed.rect.h - zed.rect.h/25:
                            self.pos.x = zed.rect.x - self.rect.width / 2
                        #hořejšek playera a dolejšek zdi
                        if self.rect.y < zed.rect.y + zed.rect.h and self.rect.y > zed.rect.y + zed.rect.h - zed.rect.h/5 and self.rect.x + (self.rect.w/delic_w) > zed.rect.x + zed.rect.w/25 and self.rect.x + (self.rect.w/delic_w) < zed.rect.x + zed.rect.w - zed.rect.w/25:
                            self.pos.y = zed.rect.bottom + self.rect.h / 2
                        #dolejšek playera a hořejšek zdi
                        if self.rect.y + self.rect.h > zed.rect.y and self.rect.y + self.rect.h < zed.rect.y + zed.rect.h/5 and self.rect.x + (self.rect.w/delic_w) > zed.rect.x + zed.rect.w/25 and self.rect.x + (self.rect.w/delic_w) < zed.rect.x + zed.rect.w - zed.rect.w/25:
                            self.pos.y = zed.rect.top - self.rect.h/2
                        
    def palba(self):
        
        if poloha:
            if stisknuto[pygame.K_SPACE]:
                now1 = pygame.time.get_ticks()
                if now1 - hrac1.last_shot > strela_delay and hrac1.povoleni == True:
                    hrac1.last_shot = now1
                    if hrac1.shotgun == False:
                        Strela(hrac1.pos + vec(0,hrac1.h/1.75).rotate(-self.rot2 - 180), vec(1, 0).rotate(-self.rot2 - 90), strela_img, strela_lifetime, False)
                    if hrac1.shotgun == True:
                        for uhel in uhly:
                            Strela(hrac1.pos + vec(0,hrac1.h/1.75).rotate(-self.rot2 - 180), vec(1.5, 0).rotate(-self.rot2 - uhel), strela_img, strela_lifetime - 2000, True)
                        hrac1.shotgun = False
                    
            if stisknuto[pygame.K_KP_ENTER]:
                now2 = pygame.time.get_ticks()
                if now2 - hrac2.last_shot > strela_delay and hrac2.povoleni == True:
                    hrac2.last_shot = now2
                    if hrac2.shotgun == False:
                        Strela(hrac2.pos + vec(0,hrac2.h/1.75).rotate(-self.rot1 - 180), vec(1, 0).rotate(-self.rot1 - 90), strela_img, strela_lifetime, False)
                    if hrac2.shotgun == True:
                        for uhel in uhly:
                            Strela(hrac2.pos + vec(0,hrac2.h/1.75).rotate(-self.rot1 - 180), vec(1.5, 0).rotate(-self.rot1 - uhel), strela_img, strela_lifetime - 2000, True)
                        hrac2.shotgun = False
                    
        else:
            if stisknuto[pygame.K_SPACE]:
                now2 = pygame.time.get_ticks()
                if now2 - hrac2.last_shot > strela_delay and hrac2.povoleni == True:
                    hrac2.last_shot = now2
                    if hrac2.shotgun == False:
                        Strela(hrac2.pos + vec(0,hrac2.h/1.75).rotate(-self.rot2 - 180), vec(1, 0).rotate(-self.rot2 - 90), strela_img, strela_lifetime, False)
                    if hrac2.shotgun == True:
                        for uhel in uhly:
                            Strela(hrac2.pos + vec(0,hrac2.h/1.75).rotate(-self.rot2 - 180), vec(1.5, 0).rotate(-self.rot2 - uhel), strela_img, strela_lifetime - 2000, True)
                        hrac2.shotgun = False
                        
            if stisknuto[pygame.K_KP_ENTER]:
                now1 = pygame.time.get_ticks()
                if now1 - hrac1.last_shot > strela_delay and hrac1.povoleni == True:
                    hrac1.last_shot = now1
                    if hrac1.shotgun == False:
                        Strela(hrac1.pos + vec(0,hrac1.h/1.75).rotate(-self.rot1 - 180), vec(1, 0).rotate(-self.rot1 - 90), strela_img, strela_lifetime, False)
                    if hrac1.shotgun == True:
                        for uhel in uhly:
                            Strela(hrac1.pos + vec(0,hrac1.h/1.75).rotate(-self.rot1 - 180), vec(1.5, 0).rotate(-self.rot1 - uhel), strela_img, strela_lifetime - 2000, True)
                        hrac1.shotgun = False
                        
        if self.tanky_kolize == True and self.abilita_freeze_sebrana == False:
            self.povoleni = True
            
    def abilitky(self):
        global herni_casovac
        #freeze
        if self.abilita_freeze_sebrana == False:
            self.casovac_freeze = herni_casovac
        if self.abilita_freeze_sebrana == True:
            if herni_casovac - self.casovac_freeze > 7500:
                self.abilita_freeze_sebrana = False
       #speedup
        if self.abilita_speed_sebrana == False:
            self.casovac_speed = herni_casovac
        if self.abilita_speed_sebrana == True:
            self.zrychleni = 2
            if herni_casovac - self.casovac_speed > 6500:
                self.abilita_speed_sebrana = False
                self.zrychleni = 1
                
    def pohyb(self):
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
                
        #kolize
        self.kolize()
        
        if poloha == False:
            if hrac1.otaceni == False:
                self.rot_speed1 = 0
            if hrac2.otaceni == False:
                self.rot_speed2 = 0
        else:
            if hrac1.otaceni == False:
                self.rot_speed2 = 0
            if hrac2.otaceni == False:
                self.rot_speed1 = 0
        self.otaceni = True
        self.rot1 = (self.rot1 + self.rot_speed1 * self.dt) % 360
        self.rot2 = (self.rot2 + self.rot_speed2 * self.dt) % 360
        
        if pohyb_tanku:
            if poloha == False:
                hrac1.vel = vec(0, hrac1.rychlost1 * hrac1.zrychleni).rotate(-self.rot1)
                hrac1.image = pygame.transform.rotate(self.player_img, self.rot1)
                hrac2.vel = vec(0, hrac2.rychlost2 * hrac2.zrychleni).rotate(-self.rot2)
                hrac2.image = pygame.transform.rotate(self.player_img, self.rot2)
            else:
                hrac1.vel = vec(0, hrac1.rychlost2 * hrac1.zrychleni).rotate(-self.rot2)
                hrac1.image = pygame.transform.rotate(self.player_img, self.rot2)
                hrac2.vel = vec(0, hrac2.rychlost1 * hrac2.zrychleni).rotate(-self.rot1)
                hrac2.image = pygame.transform.rotate(self.player_img, self.rot1)
        else:
            pass
    
    def nova_hra(self):
        if zpatky_do_menu == True:
           if cl_close3[0][0] < pygame.mouse.get_pos()[0] < (cl_close3[0][0] + cl_close3[1][0]) and cl_close3[0][1] < pygame.mouse.get_pos()[1] < (cl_close3[0][1] + cl_close3[1][1]) and pygame.mouse.get_pressed()[0]:
               self.kill()
        if hrac1.tanky_kolize == False and herni_casovac - cekat_do_nove > znovu - 15:
            self.kill()
    def update(self):
        
        self.pohyb()
        self.rect = self.image.get_rect()
        hrac1.image.set_colorkey(cerna)
        hrac2.image.set_colorkey(cerna)
        self.pos += self.vel * self.dt
        self.rect.center = self.pos
        self.abilitky()
        self.palba()
        self.nova_hra()
        
 
class Strela(pygame.sprite.Sprite):
    def __init__(self, pos, direct, img, cas, zabit):
        #základy
        pygame.sprite.Sprite.__init__(self)
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, '../doc')
        pygame.sprite.Sprite.__init__(self)
        self.bullet_img = pygame.image.load(path.join(img_folder, img)).convert_alpha()
        self.image = self.bullet_img
        sprites.add(self)
        
        #pro hru
        self.odraz = 0
        self.sepuka = zabit
        self.strela_lifetime = cas
        self.dt = 150/100000
        self.rect = self.image.get_rect()
        self.image.set_colorkey(cerna)
        self.pos = vec(pos)
        self.rect.center = pos
        self.vel = direct * strela_speed
        self.spawn_time = pygame.time.get_ticks()
        
    def kolize_strely(self):
        for zed in zdi:
            if pygame.Rect.colliderect(self.rect, zed.rect) and self.sepuka == True and self.odraz == 1:
                self.kill()
            if pygame.Rect.colliderect(self.rect, zed.rect):
               #pro dolejšek zdi s hořejškem střely
                if zed.rect.x + zed.rect.w - zed.rect.w/25 > self.rect.x and zed.rect.x + zed.rect.w/25 < self.rect.x and zed.rect.y + zed.rect.h > self.rect.y and zed.rect.y + zed.rect.h - zed.rect.h/25 < self.rect.y or zed.rect.x + zed.rect.w - zed.rect.w/25 > self.rect.x + self.rect.w and zed.rect.x + zed.rect.w/25 < self.rect.x + self.rect.w  and zed.rect.y + zed.rect.h > self.rect.y and zed.rect.y + zed.rect.h - zed.rect.h/25 < self.rect.y:
                    self.pos.y = (zed.rect.bottom + self.rect.h / 2) + 1.8
                    self.vel.y *= -1
                    self.odraz += 1
                #pro hořejšek zdi s dolejškem střely
                if zed.rect.x + zed.rect.w - zed.rect.w/25 > self.rect.x + self.rect.w and zed.rect.x + zed.rect.w/25 < self.rect.x + self.rect.w and zed.rect.y + zed.rect.h/25 > self.rect.y + self.rect.h and zed.rect.y < self.rect.y + self.rect.h or zed.rect.x + zed.rect.w - zed.rect.w/25 > self.rect.x and zed.rect.x + zed.rect.w/25 < self.rect.x and zed.rect.y + zed.rect.h/25 > self.rect.y + self.rect.h and zed.rect.y < self.rect.y + self.rect.h:
                    self.pos.y = (zed.rect.top - self.rect.h/2) - 1.8
                    self.vel.y *= -1
                    self.odraz += 1
                #pro pravou stranu zdi a levou střely
                if zed.rect.x + zed.rect.w > self.rect.x and zed.rect.x + zed.rect.w - zed.rect.w/25 < self.rect.x and zed.rect.y + zed.rect.h - zed.rect.h/25 > self.rect.y + self.rect.h and zed.rect.y + zed.rect.h /25 < self.rect.y + self.rect.h or zed.rect.x + zed.rect.w > self.rect.x and zed.rect.x + zed.rect.w - zed.rect.w/25 < self.rect.x and zed.rect.y + zed.rect.h - zed.rect.h /25 > self.rect.y and zed.rect.y + zed.rect.h /25 < self.rect.y:
                    self.pos.x = (zed.rect.right + self.rect.width / 2) + 1.8
                    self.vel.x *= -1
                    self.odraz += 1
                #pro levou stranu zdi a pravou střely
                if zed.rect.x + zed.rect.w/25 > self.rect.x + self.rect.w and zed.rect.x < self.rect.x + self.rect.w and zed.rect.y + zed.rect.h - zed.rect.h/25 > self.rect.y and zed.rect.y + zed.rect.h/25 < self.rect.y or zed.rect.x + zed.rect.w/25 > self.rect.x + self.rect.w and zed.rect.x < self.rect.x + self.rect.w and zed.rect.y + zed.rect.h - zed.rect.h/25 > self.rect.y + self.rect.h and zed.rect.y + zed.rect.h/25 < self.rect.y + self.rect.h:
                    self.pos.x = (zed.rect.x - self.rect.width / 2) - 1.8
                    self.vel.x *= -1
                    self.odraz += 1
        
        #kolize s hráčema
        
        for hrac in hraci:
            if pygame.Rect.colliderect(self.rect, hrac.rect) and hrac.strela_kolize == True:
               if hrac.rect.centerx + hrac.rect.w/4  > self.rect.x and hrac.rect.centerx + hrac.rect.w/4 < self.rect.x + self.rect.w and hrac.rect.centery - hrac.rect.h/4 > self.rect.y and hrac.rect.centery - hrac.rect.h/4 < self.rect.y + self.rect.h or hrac.rect.centerx - hrac.rect.w/4  > self.rect.x and hrac.rect.centerx - hrac.rect.w/4 < self.rect.x + self.rect.w and hrac.rect.centery + hrac.rect.h/4 > self.rect.y and hrac.rect.centery + hrac.rect.h/4 < self.rect.y + self.rect.h or hrac.rect.centerx + hrac.rect.w/4  > self.rect.x and hrac.rect.centerx + hrac.rect.w/4 < self.rect.x + self.rect.w and hrac.rect.centery + hrac.rect.h/4 > self.rect.y and hrac.rect.centery + hrac.rect.h/4 < self.rect.y + self.rect.h or hrac.rect.centerx - hrac.rect.w/4  > self.rect.x and hrac.rect.centerx - hrac.rect.w/4 < self.rect.x + self.rect.w and hrac.rect.centery - hrac.rect.h/4 > self.rect.y and hrac.rect.centery - hrac.rect.h/4 < self.rect.y + self.rect.h or hrac.rect.centerx > self.rect.x and hrac.rect.centerx < self.rect.x + self.rect.w and hrac.rect.centery - hrac.rect.h/4 > self.rect.y and hrac.rect.centery - hrac.rect.h/4 < self.rect.y + self.rect.h or hrac.rect.centerx > self.rect.x and hrac.rect.centerx < self.rect.x + self.rect.w and hrac.rect.centery + hrac.rect.h/4 > self.rect.y and hrac.rect.centery + hrac.rect.h/4 < self.rect.y + self.rect.h or hrac.rect.centerx - hrac.rect.w/4 > self.rect.x and hrac.rect.centerx - hrac.rect.w/4 < self.rect.x + self.rect.w and hrac.rect.centery > self.rect.y and hrac.rect.centery < self.rect.y + self.rect.h or hrac.rect.centerx + hrac.rect.w/4 > self.rect.x and hrac.rect.centerx + hrac.rect.w/4 < self.rect.x + self.rect.w and hrac.rect.centery > self.rect.y and hrac.rect.centery < self.rect.y + self.rect.h or hrac.rect.centerx + hrac.rect.w/4 > self.rect.x and hrac.rect.centerx + hrac.rect.w/4 < self.rect.x + self.rect.w and hrac.rect.centery + hrac.rect.h/4 > self.rect.y and hrac.rect.centery + hrac.rect.h/4 < self.rect.y + self.rect.h or hrac.rect.centerx - hrac.rect.w/4 > self.rect.x and hrac.rect.centerx - hrac.rect.w/4 < self.rect.x + self.rect.w and hrac.rect.centery + hrac.rect.h/4 > self.rect.y and hrac.rect.centery + hrac.rect.h/4 < self.rect.y + self.rect.h or hrac.rect.centerx + hrac.rect.w/4 > self.rect.x and hrac.rect.centerx + hrac.rect.w/4 < self.rect.x + self.rect.w and hrac.rect.centery - hrac.rect.h/4 > self.rect.y and hrac.rect.centery - hrac.rect.h/4 < self.rect.y + self.rect.h or hrac.rect.centerx - hrac.rect.w/4 > self.rect.x and hrac.rect.centerx - hrac.rect.w/4 < self.rect.x + self.rect.w and hrac.rect.centery - hrac.rect.h/4 > self.rect.y and hrac.rect.centery - hrac.rect.h/4 < self.rect.y + self.rect.h:
                   #nastavení pro zmizení
                   hrac.kill()
                   self.kill()
                   hrac1.povoleni = False
                   hrac2.povoleni = False
                   hrac.strela_kolize = False
                   hrac1.tanky_kolize = False
                   hrac2.tanky_kolize = False
                   #skóre
                   global skorovani_jih, skorovani_sever
                   if skorovani_jih < 3 and skorovani_sever < 3:
                       if poloha == False:
                           if hrac == hrac1:
                               skorovani_sever += 1
                           if hrac == hrac2:
                               skorovani_jih += 1
                       else:
                           if hrac == hrac1:
                               skorovani_jih += 1
                           if hrac == hrac2:
                               skorovani_sever += 1
            
    def mazani(self):
        if zpatky_do_menu == True:
           if cl_close3[0][0] < pygame.mouse.get_pos()[0] < (cl_close3[0][0] + cl_close3[1][0]) and cl_close3[0][1] < pygame.mouse.get_pos()[1] < (cl_close3[0][1] + cl_close3[1][1]) and pygame.mouse.get_pressed()[0]:
               self.kill()
        if hrac1.tanky_kolize == False and herni_casovac - cekat_do_nove > znovu - 15:
            self.kill()
        if pygame.time.get_ticks() - self.spawn_time > self.strela_lifetime:
            self.kill()
            
    def update(self):
        self.kolize_strely()
        self.pos += self.vel * self.dt
        self.rect.center = self.pos
        self.mazani()

class Abilita(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #základy
        pygame.sprite.Sprite.__init__(self)
        #načítání obrázku
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, '../doc')
        pygame.sprite.Sprite.__init__(self)
        self.abilita_img = pygame.image.load(path.join(img_folder, "Ability.png")).convert_alpha()
        #definování abilitky
        self.image = self.abilita_img
        self.rect = self.image.get_rect()
        self.image.set_colorkey(cerna)
        
        #pro vykresleni
        sprites.add(self)
        
        #lokace
        self.rect.x = x
        self.rect.y = y
        self.kol_rect = pygame.Rect(x,y,self.rect.w - 5, self.rect.h - 5)
        
    def kolize_abilitek(self):
         for hrac in hraci:
            if pygame.Rect.colliderect(self.kol_rect, hrac.rect):
                global spawn_bool, herni_casovac
                spawn_bool = True
                self.kill()
                
                #abilitka
                rozhodnuti = random.choice(typy_abilitek)
                if rozhodnuti == "NIC":
                    print("prázdné")
                if rozhodnuti == "Shotgun":
                    print(hrac," má shotgun")
                    hrac.shotgun = True
                elif rozhodnuti == "Freeze":
                    print("freeze (7.5s)")
                    if hrac == hrac1:
                        hrac2.casovac_freeze  = herni_casovac
                        hrac2.povoleni = False
                        hrac2.abilita_freeze_sebrana = True
                    if hrac == hrac2:
                        hrac1.casovac_freeze = herni_casovac
                        hrac1.povoleni = False
                        hrac1.abilita_freeze_sebrana = True
                elif rozhodnuti == "Speed_UP":
                    print("Speed_UP (7.5s)")
                    hrac.casovac_speed = herni_casovac
                    hrac.abilita_speed_sebrana = True
                
        
    def reset(self):
        if zpatky_do_menu == True:
           if cl_close3[0][0] < pygame.mouse.get_pos()[0] < (cl_close3[0][0] + cl_close3[1][0]) and cl_close3[0][1] < pygame.mouse.get_pos()[1] < (cl_close3[0][1] + cl_close3[1][1]) and pygame.mouse.get_pressed()[0]:
               self.kill()
        if hrac1.tanky_kolize == False and herni_casovac - cekat_do_nove > znovu - 15:
            self.kill()
            
    def update(self):
         self.kolize_abilitek()
         self.reset()

class Zed(object): 
    
    def __init__(self, pos):
        zdi.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], mezery +1 , mezery_y +1 )

##################################################################################################

overovaci_pin_kod = []
pin_kod = []
zdi = []
abilitky = []
level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWW          H          WWWW",
"W            WW             W",
"W     W    WWWWWW   WW      W",
"W   WWW      A        WWW   W",
"W A WWW               WWW A W",
"W   WWW       A       WWW   W",
"W     W    WWWWWW   WW      W",
"W            WW             W",
"WWWW          N          WWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

level1 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWW     WW     WW       WWWW",
"W            N              W",
"W    W               W      W",
"W    W   WWWWWWWWW   WWW    W",
"W    W    A     A    WWW    W",
"W  A W               WWW A  W",
"W    W   WWWWWWWWW   WWW    W",
"W    W               W      W",
"W            H              W",
"WWWW     WW     WW       WWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

level2 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                          W",
"W     H                    W",
"W                          W",
"W    WWW     WW     WWW    W",
"W    WWW     WW     WWW    W",
"W    WWW            WWW    W",
"W A                        W",
"WWW          A           WWW",
"WWW                      WWW",
"W                        A W",
"W    WWWW    WW    WWWW    W",
"W    WWWW    WW    WWWW    W",
"W                          W",
"W                    N     W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

# pro responzivitu s velikostí okna
levely = [level, level1, level2]
vyber = level

pygame.init()

pygame.display.set_caption('Panzerschlachtfeld im Labyrinth')
okno = pygame.display.set_mode(ROZLISENI_OKNA)
sprites = pygame.sprite.Group()

while True:
    herni_casovac = pygame.time.get_ticks()
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
        herni_casovac = pygame.time.get_ticks()
        skorovani_jih = 0
        skorovani_sever = 0
        
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
                
                if vyber == levely[1]:
                    PLAYER_SPEED = speed + 100
                    obr = "TankN.png"
                else:
                    PLAYER_SPEED = speed
                    obr = "Tank.png"
                Done = True 
                MENU = False
                
            if cl_exit1[0][0] < pygame.mouse.get_pos()[0] < (cl_exit1[0][0] + cl_exit1[1][0]) and cl_exit1[0][1] < pygame.mouse.get_pos()[1] < (cl_exit1[0][1] + cl_exit1[1][1]) and pygame.mouse.get_pressed()[0] and aktivni_obrazovka == hlavni_menu:
                pygame.quit()
                sys.exit()
            
            if cl_hl3[0][0] < pygame.mouse.get_pos()[0] < (cl_hl3[0][0] + cl_hl3[1][0]) and cl_hl3[0][1] < pygame.mouse.get_pos()[1] < (cl_hl3[0][1] + cl_hl3[1][1]) and pygame.mouse.get_pressed()[0] and aktivni_obrazovka == hlavni_menu:
                aktivni_obrazovka = menu_CREDITS
            
            if napoveda[0][0] < pygame.mouse.get_pos()[0] < (napoveda[0][0] + napoveda[1][0]) and napoveda[0][1] < pygame.mouse.get_pos()[1] < (napoveda[0][1] + napoveda[1][1]) and pygame.mouse.get_pressed()[0]:
                aktivni_obrazovka = menu_napoveda
        
        if aktivni_obrazovka == menu_napoveda:
            if cl_close2[0][0] < pygame.mouse.get_pos()[0] < (cl_close2[0][0] + cl_close2[1][0]) and cl_close2[0][1] < pygame.mouse.get_pos()[1] < (cl_close2[0][1] + cl_close2[1][1]) and pygame.mouse.get_pressed()[0]:
                aktivni_obrazovka = hlavni_menu
             
        if aktivni_obrazovka == menu_vyberu:
            if cl_v1[0][0] < pygame.mouse.get_pos()[0] < (cl_v1[0][0] + cl_v1[1][0]) and cl_v1[0][1] < pygame.mouse.get_pos()[1] < (cl_v1[0][1] + cl_v1[1][1]) and pygame.mouse.get_pressed()[0]:
                vyber = levely[0]
                PLAYER_SPEED = speed
                obr = "Tank.png"
                Done = True 
                MENU = False
            if cl_v2[0][0] < pygame.mouse.get_pos()[0] < (cl_v2[0][0] + cl_v2[1][0]) and cl_v2[0][1] < pygame.mouse.get_pos()[1] < (cl_v2[0][1] + cl_v2[1][1]) and pygame.mouse.get_pressed()[0]:    
                vyber = levely[1]
                PLAYER_SPEED = speed + 100
                obr = "TankN.png"
                Done = True
                MENU = False
            if cl_v3[0][0] < pygame.mouse.get_pos()[0] < (cl_v3[0][0] + cl_v3[1][0]) and cl_v3[0][1] < pygame.mouse.get_pos()[1] < (cl_v3[0][1] + cl_v3[1][1]) and pygame.mouse.get_pressed()[0]:
                vyber = levely[2]
                PLAYER_SPEED = speed
                obr = "Tank.png"
                Done = True
                MENU = False
                
            if cl_close1[0][0] < pygame.mouse.get_pos()[0] < (cl_close1[0][0] + cl_close1[1][0]) and cl_close1[0][1] < pygame.mouse.get_pos()[1] < (cl_close1[0][1] + cl_close1[1][1]) and pygame.mouse.get_pressed()[0]:  
                aktivni_obrazovka = hlavni_menu
        
        if aktivni_obrazovka == menu_CREDITS:
            pipsiky_k_credits(okno, bila, cerna)
            if cl_close2[0][0] < pygame.mouse.get_pos()[0] < (cl_close2[0][0] + cl_close2[1][0]) and cl_close2[0][1] < pygame.mouse.get_pos()[1] < (cl_close2[0][1] + cl_close2[1][1]) and pygame.mouse.get_pressed()[0]:  
                aktivni_obrazovka = hlavni_menu                                
        
        if aktivni_obrazovka == hlavni_menu:
            hl_nadpis1 = typ_pisma_hlavni_menu.render('Panzerschlachtfeld im Labyrinth:', True, bila, cerna)
            hl_nadpis1Rect = hl_nadpis1.get_rect()
            hl_nadpis1Rect.center = (550, 128)
    
            nadpis_menu1 = typ_pisma_hlavni_menu.render('Vybrat mapu', True, bila, cerna)
            nadpis_menu1Rect = nadpis_menu1.get_rect()
            nadpis_menu1Rect.center = (560, 303)
            
            
            nadpis_menu2 = typ_pisma_hlavni_menu.render('Náhodná mapa', True, bila, cerna)
            nadpis_menu2Rect = nadpis_menu2.get_rect()
            nadpis_menu2Rect.center = (560, 483)
            

            nadpis_menu3 = typ_pisma_hlavni_menu.render('CREDITS', True, bila, cerna)
            nadpis_menu3Rect = nadpis_menu3.get_rect()
            nadpis_menu3Rect.center = (560, 663)
            
            nadpis_exit = typ_pisma_hlavni_menu.render('EXIT', True, bila, cerna)
            nadpis_exitRect = nadpis_exit.get_rect()
            nadpis_exitRect.center = (1000, 747)
            
            otaznik = typ_pisma_hlavni_menu.render('??', True, bila, (180, 0, 0))
            
        if aktivni_obrazovka == menu_napoveda:
            hl_nadpis1 = typ_pisma_hlavni_menu.render('Panzerschlachtfeld im Labyrinth:', True, bila, cerna)
            hl_nadpis1Rect = hl_nadpis1.get_rect()
            hl_nadpis1Rect.center = (550, 90)
            text_napoveda(okno, bila, cerna)
            
            nadpis_close1 = typ_pisma_hlavni_menu.render('CLOSE', True, bila, cerna)
            nadpis_close1Rect = nadpis_close1.get_rect()
            nadpis_close1Rect.center = (100, 750)
            
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
            okno.blit(otaznik, (26, 213))
            
        if aktivni_obrazovka == menu_napoveda:
            okno.blit(hl_nadpis1, hl_nadpis1Rect)
            okno.blit(nadpis_close1, nadpis_close1Rect)
        
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
            abilitky = []
            mezery = ROZLISENI_X/len(vyber[0])
            mezery_y = ROZLISENI_Y/len(vyber)
            x = y = 0
            for radek in vyber:
                for element in radek:
                    if element == "W":
                        Zed((x, y))
                    if element == "H":
                        hrac1 = Player(x + (mezery+5)/2, y + mezery_y/2 , obr)
                    if element == "N":
                        hrac2 = Player(x + (mezery+5)/2, y + mezery_y/2 , obr)
                    if element == "A":
                        abilitky.append([x, y + 7])
                    x += mezery
                y += mezery_y
                x = 0               
            if hrac1.rect.y < hrac2.rect.y: 
                poloha = True 
            else: 
                poloha = False
            
            #deklarace věcí
            abilitky_spawn = herni_casovac
            spawn_bool = True
            hraci = [hrac1,hrac2]
        pygame.display.update()

    #logika spawnu abiitek
    if hrac1.tanky_kolize == False and herni_casovac - abilitky_spawn > 0 or spawn_bool == False :
        abilitky_spawn = herni_casovac
    if hrac1.tanky_kolize == True and herni_casovac - abilitky_spawn > cas_na_spawn_abilitek and skorovani_jih != 3 and skorovani_sever != 3 and spawn_bool == True:
        if skorovani_jih < 3 and skorovani_sever < 3:
            ab = []
            a = random.choice(abilitky)
            ab.append(a)
            
            for pos in ab:
                Abilita(pos[0],pos[1])
            spawn_bool = False
        
    
    
    #logika respawnu, neboli nové hry
    if hrac1.tanky_kolize == True and herni_casovac - cekat_do_nove > 0:
        cekat_do_nove = herni_casovac
        
    if skorovani_jih == 3 or skorovani_sever == 3: 
        cekat_do_nove = herni_casovac - znovu
        
    if hrac1.tanky_kolize == False and herni_casovac - odpocet_odpoctu > 1000 and skorovani_jih != 3 and skorovani_sever != 3 :
        odpocet_odpoctu = herni_casovac
        odpocet -= 1
    
    if hrac1.tanky_kolize == False and herni_casovac - cekat_do_nove > znovu:
        mezery = ROZLISENI_X/len(vyber[0])
        mezery_y = ROZLISENI_Y/len(vyber)
        x = y = 0
        for radek in vyber:
            for element in radek:
                if element == "H":
                        hrac1 = Player(x + (mezery+5)/2, y + mezery_y/2 , obr)
                if element == "N":
                        hrac2 = Player(x + (mezery+5)/2, y + mezery_y/2 , obr) 
                x += mezery
            y += mezery_y
            x = 0               
        hraci = [hrac1,hrac2]
        odpocet = int(znovu/1000) + 1
        spawn_bool = True
        
########## herní logika ################################################################################################
        
    p_zmacknuto_ted = stisknuto[pygame.K_p]
    
    if p_zmacknuto_pred_tim !=  p_zmacknuto_ted:
        if p_zmacknuto_ted:
            in_game_menu = True  
    
    p_zmacknuto_pred_tim = p_zmacknuto_ted

######## vykreslovani ##############################################################################################
    okno.fill(RGB)
    sprites.update()
    for zed in zdi:
        pygame.draw.rect(okno, (0, 0, 0), zed.rect)   
    sprites.draw(okno)
    if hrac1.tanky_kolize == False and skorovani_jih != 3 and skorovani_sever != 3 :
        pygame.draw.rect(okno, (150,150,150), ((370,250), (300,300)))
        odpocet_text = typ_pisma_odpocet.render(str(odpocet), True, (20,100,35))
        okno.blit(odpocet_text, (435, 270))
        
    if vyber == level:
        skore_sever(bila, cerna, cervena)
        skore_jih(bila, cerna, cervena)
        
    if vyber == level1:
        skore_sever(bila, cerna, cervena)
        skore_jih(bila, cerna, cervena)
        
    if vyber == level2:
        skore_sever(bila, cerna, cervena)
        skore_jih(bila, cerna, cervena)
    
    kontrola_skore(okno)
# cudliky v pause menu ################################################################################################ 
    while in_game_menu == True:
        if time_p == False:
            cas = herni_casovac - abilitky_spawn
            for hrac in hraci:
                if hrac.abilita_freeze_sebrana == True:
                    hrac.cas = herni_casovac - hrac.casovac_freeze
                if hrac.abilita_speed_sebrana == True:
                    hrac.cas = herni_casovac - hrac.casovac_speed
            time_p = True
        herni_casovac = pygame.time.get_ticks()
        #abilitky spawn
        for hrac in hraci:
            if hrac.abilita_freeze_sebrana == True:
                hrac.casovac_freeze = herni_casovac- hrac.cas
            if hrac.abilita_speed_sebrana == True:
                hrac.casovac_speed = herni_casovac- hrac.cas
        abilitky_spawn = herni_casovac-cas
        
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
        p_zmacknuto_ted = stisknuto[pygame.K_p]
    
        if p_zmacknuto_pred_tim !=  p_zmacknuto_ted:
            if p_zmacknuto_ted:
                in_game_menu = False
                time_p = False
        
        p_zmacknuto_pred_tim = p_zmacknuto_ted
        if zpatky_do_menu == True:
            if cl_close3[0][0] < pygame.mouse.get_pos()[0] < (cl_close3[0][0] + cl_close3[1][0]) and cl_close3[0][1] < pygame.mouse.get_pos()[1] < (cl_close3[0][1] + cl_close3[1][1]) and pygame.mouse.get_pressed()[0]:
                aktivni_obrazovka = hlavni_menu
                in_game_menu = False
                Done = False
                MENU = True
                sprites.update()
               
        if odchod_ze_hry == True:
            if cl_exit2[0][0] < pygame.mouse.get_pos()[0] < (cl_exit2[0][0] + cl_exit2[1][0]) and cl_exit2[0][1] < pygame.mouse.get_pos()[1] < (cl_exit2[0][1] + cl_exit2[1][1]) and pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()
        
        okno.fill(RGB)
        for zed in zdi:
            pygame.draw.rect(okno, (0, 0, 0), zed.rect)   
        sprites.draw(okno)
        if in_game_menu == True:
            aktivni_obrazovka = pause_menu
            pygame.draw.rect(okno, (200, 0, 0), ((0,0), (520,520)))
            pygame.draw.rect(okno, (190, 190, 190), ((10,10), (500,500))) 
            
            for cudlik in pause_menu[2]:
                pygame.draw.rect(okno, cudlik[2], (cudlik[0], cudlik[1]))
                
            odchod_ze_hry = True
            zpatky_do_menu = True   
            
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
                odchod_ze_hry = False
                zpatky_do_menu = False
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
                odchod_ze_hry = False
                zpatky_do_menu = False
                pygame.draw.rect(okno, (200, 20, 20), ((0, 0), (1080, 800)))
                cekaci_obrazovka(okno)
                okno.blit(cekaci_menu_animation(animovany_tank,clock), (80, 80))
                vykreslovani_policek_v_cekacim_menu(okno)
                zapis_pro_overovaci_pin()
                popisky_k_cekacimu_menu(bila, cerna, okno)
            
            if cl_pin[0][0] < pygame.mouse.get_pos()[0] < (cl_pin[0][0] + cl_pin[1][0]) and cl_pin[0][1] < pygame.mouse.get_pos()[1] < (cl_pin[0][1] + cl_pin[1][1]) and pygame.mouse.get_pressed()[0]:
                if mys_zmacknuta_ted:
                    pin = True
                zadavani = True
        pygame.display.update()
    pygame.display.update() 