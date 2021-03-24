import pygame
pygame.init()
x = 400
y = 400
velocidade = 10
fundo = pygame.image.load('Game Background.png')
carro = pygame.image.load('Jogo_do_carro/carro1.png')

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Criando um jogo com Python")

janelaAberta = True

while janelaAberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janelaAberta = False

    comandos = pygame.key.get_pressed()
    if comandos [pygame.K_UP]:
        y -= velocidade
    if comandos [pygame.K_DOWN]:
        y += velocidade
    if comandos [pygame.K_RIGHT]:
        x += velocidade
    if comandos [pygame.K_LEFT]:
        x -= velocidade

    janela.blit(fundo, (0, 0))
    janela.blit(carro, (x, y))
    pygame.display.update()

pygame.quit()
