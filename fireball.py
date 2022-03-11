import pygame


class fireball(pygame.sprite.Sprite): # définir objet comme un image objet
    def __init__(self,player):
        super().__init__() # appeler construiteur avance
        self.damage = 20
        self.velocity=5
        self.image = pygame.image.load('assets/projectile.png')
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()# céer rectangle de capteur
        self.rect.y = player.rect.y + 90
        self.rect.x = player.rect.x + 100
        self.origin_image=self.image
        self.angle=0

        self.player=player

    def rotate(self): # le fireball se tourne
        self.angle += 90
        self.image=pygame.transform.rotozoom(self.origin_image,self.angle,1)

    def move(self):

        # si le ball touche le mummy
        colli = False
        # si il n'y a pas la collision
        for monster in self.player.game.check_collision2(self,self.player.game.all_mummy):
            # supprimer la ball
            self.player.all_fire.remove(self)
            monster.damage(self.damage)


        self.rect.x += self.velocity
        self.rotate()






