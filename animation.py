import pygame


class animate(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{name}.png')
        self.current_image = 0  # commencer par image n°0
        self.images = animations.get(name)  # liste d'image

    # pour animer image
    def animer(self):
        self.current_image += 1  # changer image
        # vérifier la fin del'animation
        if (self.current_image >= len(self.images)):
            self.current_image = 0
        # charger l'image
        self.image = self.images[self.current_image]

    # charger image 24 fois/s


def load_image(name):
    # créer un dossier d'image
    images = []
    # récupérer la chemin
    chemin = f"assets/{name}/{name}"
    # boucle de chaque image
    for i in range(1, 24):
        image_chemin = chemin + str(i) + '.png'
        images.append(pygame.image.load(image_chemin))

    # renvoyer le contenu
    return images


# une dictionnaire
animations = {
    'mummy': load_image('mummy'),
    'player': load_image('player')
}
