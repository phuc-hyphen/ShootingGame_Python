import pygame
from player import player
from mummy import mummy
from game import game

# start game
pygame.init()
#créer la fenêtre
screen=pygame.display.set_mode((1080,720))#déclarer un fenetre
pygame.display.set_caption(" shooting game ")#changer le nom
# charger image
back=pygame.image.load('assets/bg.jpg')
# charger le jeu
game=game()

running=True
start=False
# boucle
while running:
    # appliquer le background
    screen.blit(back, (0, -200))  # les valeurs peuvent négatives

    if start==False:

        # l'écran d'accueil
        image_banner=pygame.image.load('assets/banner.png')
        image_banner=pygame.transform.scale(image_banner,(200,200))
        screen.blit(image_banner,(400,200))
        image_bout=pygame.image.load('assets/button.png')
        image_bout=pygame.transform.scale(image_bout,(200,100))
        screen.blit(image_bout, (400, 350))

        # detect mouse click
        ev=pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:  # bouton X pour sortir
                running = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if (pos[0]>415 and pos[0]<512 and pos[1]>370 and pos[1]< 420):
                    start=True
                    print(pos)


    else:
    #--------------------- Appliquer player-------------
        screen.blit(game.player.image,game.player.rect)
        game.player.heath_bar(screen)

        #----- player move---------------------
        if game.touche.get(pygame.K_RIGHT) and game.player.rect.x < 950 : # get () : access the items of a dictionary by referring to its key name
            game.player.bouge_droit()
        if game.touche.get(pygame.K_LEFT) and game.player.rect.x > 0:
            game.player.bouge_gauche()


        pygame.time.delay(10)

        # ----------- detection du presse ----------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # bouton X pour sortir
                running = False
            if event.type==pygame.KEYDOWN:
                game.touche[event.key]=True # écrire en la dic la touche
                # détecter si la touche est la boule
                if event.key == pygame.K_SPACE:
                    game.player.tire()
            if event.type==pygame.KEYUP:
                game.touche[event.key]=False


    #---------------- Aplliquer boule de feu -------------

        # recuperer le fireball
        for fire in game.player.all_fire:
            fire.move()
        game.player.all_fire.draw(screen)

    # -------------- Appliquer Mummies ---------------
        for mummy in game.all_mummy:
            mummy.move()
            mummy.heath_bar(screen)

        game.all_mummy.draw(screen)

    pygame.display.flip()


