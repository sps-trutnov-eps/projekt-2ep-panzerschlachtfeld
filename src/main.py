# Začátek Panzerschlachtfeld im Labyrinth ##################################################

import pygame, sys
import math


# proměnné ##################################################################################

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 800,800
RGB = R, G, B, = 255, 0, 255


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
        
        
# vykreslovani ##############################################################################
    
    okno.fill(RGB)
    pygame.display.update()
        