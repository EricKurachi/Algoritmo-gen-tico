import pygame

black = (0, 0, 0)
gray = (168, 168, 168)
pixel = 4

clock = pygame.time.Clock()

def text(string):
    font = pygame.font.SysFont("arial", 20)
    label = font.render(string, True, black)
    return label

def image(window, imageName, x, y):
    image = pygame.image.load(imageName).convert_alpha()
    window.blit(image, (x, y))

def loop(window):
    option = 0
    while True:
        image(window, 'title.png', 0, 0)

        if option == 0:
            image(window, 'raio.png', 82*pixel, 73*pixel)
        if option == 1:
            image(window, 'raio.png', 75*pixel, 94*pixel)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 'arena'
                if event.key == pygame.K_DOWN:
                    option += 1
                if event.key == pygame.K_UP:
                    option -= 1

        option = option%2

        pygame.display.update()
        clock.tick(30)