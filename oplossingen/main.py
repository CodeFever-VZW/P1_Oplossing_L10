from breakout_module import *
import pygame
import sys

venster_breedte = 590
venster_hoogte = 480
bal_positie = [venster_breedte // 2, venster_hoogte // 2]
bal_grootte = 10
blok_breedte = 60
blok_hoogte = 20
blok_rijen = 5
blok_kolommen = venster_breedte // (blok_breedte + 5)
peddel_positie = [venster_breedte // 2, venster_hoogte - 20]
peddel_breedte = 60
peddel_hoogte = 10
peddel_snelheid = 5
klok = pygame.time.Clock()
spel_voorbij = False


def beweeg_peddel():
    global peddel_breedte
    toetsen = pygame.key.get_pressed()

    if toetsen[pygame.K_LEFT]:
        peddel_positie[0] -= peddel_snelheid
    if toetsen[pygame.K_RIGHT]:
        peddel_positie[0] += peddel_snelheid
    if toetsen[pygame.K_UP]:
        peddel_breedte += 10
    elif toetsen[pygame.K_DOWN]:
        peddel_breedte -= 10


def teken_spel():
    venster.fill((10, 0, 30))

    pygame.draw.rect(venster, (170, 0, 255),
                     (peddel_positie[0] - peddel_breedte // 2, peddel_positie[1], peddel_breedte, peddel_hoogte))
    pygame.draw.circle(venster, (200, 50, 0), bal_positie, bal_grootte)

    index = 0
    for blok in blokken:
        pygame.draw.rect(venster, (150, 255-3*index, 255), blok)
        index += 1

    pygame.display.update()


def is_spel_voorbij():
    if bal_positie[1] >= venster_hoogte or len(blokken) == 0:
        return True
    return False

def toon_eindbericht():
    venster.fill((0, 0, 0))
    if len(blokken) <= 0:
        toon_bericht("GEWONNEN", venster)
    else:
        toon_bericht("GAME OVER", venster)
    pygame.display.update()


# Initialisatie van venster, snelheid en de blokken
venster = setup_venster(venster_breedte, venster_hoogte)
bal_snelheid = initialiseer_bal()
blokken = initialiseer_blokken(blok_rijen, blok_kolommen, blok_breedte, blok_hoogte)


# SPEEL BREAKOUT:
while not spel_voorbij:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                bal_snelheid[0] *= 1.2
                bal_snelheid[1] *= 1.4

    beweeg_peddel()
    bal_positie, bal_snelheid = update_bal()
    teken_spel()
    klok.tick(60)
    spel_voorbij = is_spel_voorbij()


# Hier is het spel voorbij: teken GAME OVER of GEWONNEN
toon_eindbericht()

# Wacht even en quit pygame
pygame.time.delay(3000)
pygame.quit()