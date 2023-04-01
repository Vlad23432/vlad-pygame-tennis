import pygame


class Platform:
    def __init__(self, bounds):
        self.bounds = bounds
        self.size = (70, 20)
        self.speedX = 10
        self.speedY = 10

    def draw(self):
        self.image = pygame.image.load('platform.png')
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()

    def move(self, bounds):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 10
        if key[pygame.K_RIGHT] and self.rect.right < bounds[0]:
            self.rect.x += 10

    def coll(self):
        self.rect.colliderect(self.rect)
        self.move()
