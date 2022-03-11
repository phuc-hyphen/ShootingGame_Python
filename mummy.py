import pygame
import random
import animation

class mummy(animation.animate): # définir objet comme un image objet
    def __init__(self,game):
        super().__init__("mummy") # appeler construiteur avance
        self.health =100
        self.maxhealth =100
        self.velocity = 3
        self.rect = self.image.get_rect()# céer rectangle de capteur
        self.rect.x=800 + random.randint(0,300)
        self.rect.y =550
        self.attack =0.5

        self.game=game

    def damage(self,damage):

        self.health -= damage
        # si le mummy est mort
        if self.health <= 0:
        # remettre le monstre
            self.rect.x = 1000+ random.randint(0,300)
            self.health=100

    def heath_bar(self,surface):
        # couleur de bar de vie
        bar_color=(255,0,0)
        # la position et sa taille
        bar_position=[self.rect.x,self.rect.y,self.health,5]
        # dessin la barre
        pygame.draw.rect(surface,(200,200,200),(self.rect.x,self.rect.y,self.maxhealth,5))
        pygame.draw.rect(surface,bar_color,bar_position)



    def move(self):
        self.animer()
        # si il n'y a pas la collision
        if not self.game.check_collision(self,self.game.player):
            if (self.rect.x > 10):
                self.rect.x -= self.velocity
            else:
                self.rect.x = 1000
        else:
            self.game.player.damage(self.attack)
