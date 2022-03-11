import pygame
from player import player
from mummy import mummy


class game():
    def __init__(self):
        # groupe de joueur
        self.all_player = pygame.sprite.Group()
        self.player = player(self)
        self.all_player.add(self.player)

        # groupe de mummy
        self.all_mummy = pygame.sprite.Group()
        self.spwam_mummy()
        self.spwam_mummy()

        self.touche = {}  # créer un dictionnaire vide

    def check_collision(self, sprite, group):
        return pygame.sprite.collide_mask(sprite, group)

    def check_collision2(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spwam_mummy(self):
        self.all_mummy.add(mummy(self))
