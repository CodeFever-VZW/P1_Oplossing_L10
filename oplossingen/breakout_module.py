import random
import pygame

###################### VENSTER ######################
def setup_venster(breedte, hoogte):
    pygame.init()
    nieuw_venster = pygame.display.set_mode((breedte, hoogte))
    pygame.display.set_caption('Breakout')
    return nieuw_venster


###################### BLOKKEN ######################
def initialiseer_blokken(rijen, kolommen, breedte, hoogte):
    # Maak een lijst van blokken (pygame rechthoeken)
    blokken = []
    for rij in range(rijen):
        for kolom in range(kolommen):
            blokken.append(
                pygame.Rect(5 + kolom * (breedte + 5), 5 + rij * (hoogte + 5), breedte, hoogte)
            )
    return blokken

###################### BAL ######################
def initialiseer_bal():
    # Kies een random richting en geef bijhorende snelheid terug
    richting = random.choice([-1, 1])
    nieuwe_bal_snelheid = [3 * richting, -3]
    return nieuwe_bal_snelheid


def update_bal():
    from main import bal_positie, bal_snelheid, bal_grootte, venster_breedte, venster_hoogte, peddel_positie, peddel_breedte, peddel_hoogte, blokken
    bal_positie[0] += bal_snelheid[0]
    bal_positie[1] += bal_snelheid[1]

    # Controleer of de bal de linker- of rechterrand van het venster raakt
    if bal_positie[0] <= 0 or bal_positie[0] >= venster_breedte - bal_grootte:
        bal_snelheid[0] = -bal_snelheid[0]  # Keer horizontaal om

    # Controleer of de bal de bovenrand van het venster raakt
    if bal_positie[1] <= 0:
        bal_snelheid[1] = -bal_snelheid[1]  # Keer verticaal om

    # Controleer of de bal de bovenkant van de peddel raakt
    if bal_positie[1] >= venster_hoogte - bal_grootte - peddel_hoogte and peddel_positie[0] - peddel_breedte // 2 <= \
            bal_positie[0] <= peddel_positie[0] + peddel_breedte // 2:
        bal_snelheid[1] = -bal_snelheid[1]

    # Controleer of de bal een blok raakt
    for blok in blokken:
        if blok.colliderect(
                pygame.Rect(bal_positie[0] - bal_grootte, bal_positie[1] - bal_grootte,
                            bal_grootte * 2, bal_grootte * 2)
        ):
            blokken.remove(blok)
            bal_snelheid[1] = -bal_snelheid[1]
            break
    return bal_positie, bal_snelheid


###################### BERICHT ######################
def toon_bericht(bericht, venster):
    breedte = venster.get_width()//2
    hoogte = venster.get_height()//2
    lettertype = pygame.font.Font(None, 36)
    tekst = lettertype.render(bericht, True, (255, 255, 255))
    tekst_rechthoek = tekst.get_rect(center=(breedte, hoogte))
    venster.blit(tekst, tekst_rechthoek)