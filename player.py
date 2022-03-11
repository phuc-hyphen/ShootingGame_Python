import pygame
from fireball import fireball
import animation
from tkinter import messagebox

class player(animation.animate): # définir objet comme un image objet
    def __init__(self,game):
        super().__init__('player') # appeler construiteur avance
        self.health =100
        self.maxhealth =100
        self.all_fire=pygame.sprite.Group()
        self.velocity =5
        self.attack =10
        self.rect = self.image.get_rect()# céer rectangle de capteur

        self.game=game  # récupérer la class game

        self.rect.y =500
    def damage(self,damage):

        self.health -= damage
        # s'il y a plus de vie
        if self.health == 0:
            messagebox.showinfo(" YOU LOSE ")

    def heath_bar(self,surface):
        pygame.draw.rect(surface,(200,200,200),(self.rect.x+50,self.rect.y+20,self.maxhealth,10))
        pygame.draw.rect(surface,(255,0,0),(self.rect.x+50,self.rect.y+20,self.health,10))


    def tire(self):
        self.all_fire.add(fireball(self))
        self.animer()


    def bouge_droit(self):
        colli=False
        # si il y a la collision
        for monster in self.game.all_mummy:
            if self.game.check_collision(self,monster):
                colli=True
                self.health -= 10
        if colli==False:
            self.rect.x += self.velocity

    def bouge_gauche(self):
        self.rect.x -= self.velocity

