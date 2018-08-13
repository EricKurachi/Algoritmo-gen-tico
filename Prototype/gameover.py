import pygame

gray = (168, 168, 168)
black = (0, 0, 0)

clock = pygame.time.Clock()

def text(string):
    font = pygame.font.SysFont("arial", 20)
    label = font.render(string, True, black)
    return label

def loop(window):
    while True:
        window.fill(gray)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return 'arena'
                if event.key == pygame.K_q:
                    return 'quit'

        window.blit(text('Vc bateu as botas ( e perdeu O JOGO)'), (500, 300))
        window.blit(text("aperte 'r' para jogar novamente"), (500, 400))
        window.blit(text("aperte 'q' para sair"), (500, 350))

        pygame.display.update()
        clock.tick(30)
