import pygame # Импорт модуля пайгейм
import myachik
pygame.init()

ping = pygame.mixer.Sound('otskok.mp3')
loose = pygame.mixer.Sound('loose.mp3')

pygame.mixer.music.load('fonovaya_music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

score = 0
rounds = 3

def draw_text(screen, text,size, x, y, color):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_image, text_rect)
width = 1366
height = 768
fps = 60
gameName = 'First Project'

screen = pygame.display.set_mode((width, height)) # Создание экрана с заданными размера

BLACK = '#000000'
WHITE = '#FFFFFF'
RED = '#FF0000'
GREEN = '#008000'
BLUE = '#0000FF'
CYAN = '#00FFFF'

ball = myachik.Ball((width, height))

platform = pygame.image.load('platform.png')
platform_rect = platform.get_rect()

platform_rect.x = width / 2 - platform.get_width() / 2
platform_rect.y = height - 60

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()

    screen.fill(CYAN)
    ball.update(screen)
    screen.blit(platform, platform_rect)
    draw_text(screen, 'score: ' + str(score), 40, width / 2, 50, RED)
    draw_text(screen, 'rounds: ' + str(rounds), 40, width - 100, 50, RED)

    if key[pygame.K_LEFT] and platform_rect.left > 0:
        platform_rect.x -= 10
    if key[pygame.K_RIGHT] and platform_rect.right < width:
        platform_rect.x += 10

    if ball.rect.colliderect(platform_rect):
        ping.play()
        score += 1

        ball.speedY = -ball.speedY

    if ball.rect.bottom > height:
        rounds -= 1
        loose.play()
        if rounds <= 0:
            run = False
        ball.respawn()

    pygame.display.update()
pygame.quit()