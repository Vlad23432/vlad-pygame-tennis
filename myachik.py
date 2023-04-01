import pygame
import random


class Ball:
    def __init__(self, bounds):
        self.bounds = bounds
        self.size = (50, 50)
        self.image = pygame.image.load('img.png')
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.speedX = 10
        self.speedY = 10

    def respawn(self):
        self.rect.x = random.randint(100, self.bounds[1] - 100)
        self.rect.y = 50

    def move(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY

    def update(self, screen):
        if self.rect.top < 0:
            self.speedY = -self.speedY
        if self.rect.left < 0:
            self.speedX = -self.speedX
        if self.rect.right > self.bounds[0]:
            self.speedX = -self.speedX
        self.move()
        screen.blit(self.image, self.rect)