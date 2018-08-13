import pygame, random

sky_blue = (100, 100, 255)
black = (0, 0, 0)
green = (50, 255, 50)
red = (255, 0, 0)

pixel = 4

def text(string):
    font = pygame.font.SysFont("arial", 20)
    label = font.render(string, True, black)
    return label

clock = pygame.time.Clock()

def attack(window, side, enemy_pos):
    if side == 'left':
        pygame.draw.rect(window, black, [123*pixel, 100*pixel, -10*pixel, 2*pixel])
        if enemy_pos > 107*pixel and enemy_pos < 118*pixel:
            return True

    if side == 'right':
        pygame.draw.rect(window, black, [128*pixel, 100*pixel, 10*pixel, 2*pixel])
        if enemy_pos > 128*pixel and enemy_pos < 138*pixel:
            return True

def enemy_spawn(width):
    if random.randint(1, 500) == 1:
        if random.randint(1, 2) == 1:
            return 0
        else:
            return width
    else:
        return None

def image(window, imageName, x, y):
    image = pygame.image.load(imageName).convert_alpha()
    window.blit(image, (x, y))

def loop(window):

    enemy_pos = [None, None, None, None, None, None, None, None, None, None]
    enemy_max = 10
    points = 0

    health = 100
    nuvem = 0

    while True:
        nuvem = (nuvem%1424)+pixel
        nuvem_pos = nuvem-100*pixel

        window.fill(sky_blue)
        image(window, 'ceu.jpg', 0, 0)
        image(window, 'gato.png', nuvem_pos, 5*pixel)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return 'quit'
                if event.key == pygame.K_LEFT:
                    for i in range(0, enemy_max):
                        if attack(window, 'left', enemy_pos[i]):
                            enemy_pos[i] = None
                            points += 1
                elif event.key == pygame.K_RIGHT:
                    for i in range(0, enemy_max):
                        if attack(window, 'right', enemy_pos[i]):
                            enemy_pos[i] = None
                            points += 1

        for i in range(0, enemy_max):
            if enemy_pos[i] == None:
                enemy_pos[i] = enemy_spawn(256*pixel)

        for i in range(0, enemy_max):
            if enemy_pos[i] is not None:
                if enemy_pos[i]<117*pixel:
                    enemy_pos[i]+=pixel
                elif enemy_pos[i]>129*pixel:
                    enemy_pos[i]-=pixel
                pygame.draw.rect(window, red, (enemy_pos[i], 100*pixel, 5*pixel, 10*pixel))

        for i in range(0, enemy_max):
            if (enemy_pos[i] == 117*pixel or enemy_pos[i] == 129*pixel):
                health -= 1

        if health <= 0:
            return 'gameover'

        pygame.draw.rect(window, black, (123*pixel, 100*pixel, 5*pixel, 10*pixel))
        pygame.draw.rect(window, green, (0, 110*pixel, 256*pixel, 100*pixel))

        window.blit(text('{}/100'.format(health)), (118*pixel, 110*pixel))
        window.blit(text('pontos: {}'.format(points)), (0, 0))

        pygame.display.update()

        clock.tick(400)