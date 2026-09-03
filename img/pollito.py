import pygame

pygame.init()

pantalla = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Cruzar la avenida")

amarillo = (255, 255, 0)
gris = (80, 80, 80)
rojo = (255, 0, 0)
azul = (0, 100, 255)
verde = (0, 200, 0)
blanco = (255, 255, 255)

x = 300
y = 450

carros = [
    [50, 150],
    [400, 250],
    [150, 350]
]

jugando = True

while jugando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        x -= 5
    if teclas[pygame.K_RIGHT]:
        x += 5
    if teclas[pygame.K_UP]:
        y -= 5
    if teclas[pygame.K_DOWN]:
        y += 5

    pantalla.fill(verde)

    # Avenida
    pygame.draw.rect(pantalla, gris, (0, 100, 600, 300))

    # Meta
    pygame.draw.rect(pantalla, verde, (0, 0, 600, 70))
    texto = pygame.font.Font(None, 40).render("META", True, blanco)
    pantalla.blit(texto, (260, 20))

    # Carros
    for carro in carros:
        pygame.draw.rect(pantalla, rojo, (carro[0], carro[1], 80, 40))
        carro[0] += 3

        if carro[0] > 600:
            carro[0] = -80

    # Jugador
    pygame.draw.circle(pantalla, amarillo, (x, y), 15)

    pygame.display.update()

pygame.quit()
