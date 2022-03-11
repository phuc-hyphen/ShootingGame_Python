import pygame

# start game
pygame.init()
#créer la fenêtre
screen=pygame.display.set_mode((100,200))#déclarer un fenetre
pygame.display.set_caption(" shooting game ")#changer le nom
# charger le jeu

running=True
# boucle
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # bouton X pour sortir
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            print("down")
            if event.key==pygame.K_RIGHT:
                print("tested")
    pygame.display.flip()