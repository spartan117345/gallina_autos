import pygame
import sys
import random

# inicializacion
pygame.init()

# Colores
amarillo = (187, 173, 4)
amarilo_oscuro = (142, 130, 10 )
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (50, 222, 12)
rosado = (255, 195, 203)
negro = (0,0,0)
naranja = (194, 88, 0)
blanco = (255, 255, 255)
cian = (0, 255, 255)
gris = (118, 120, 119)
gris_oscuro = (80, 81, 81)
gris_mas_oscuro = (58,59,58)
gris_claro = (198, 200, 199)
boca = (197, 71, 56)
morado = (145, 74, 201 )
cafe = (91, 10, 10 )

# variables del jugador
XX = 300
YY = 550

# Crear ventana
ventana = pygame.display.set_mode((600, 700))
pygame.display.set_caption("El cuadrado que rebota")

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Variables para el cuadrado que se mueve
autos1 = 0
autos2 = 600
autos3 = 0
autos4 = 600
derecha = 2
izquierda = -2
derecha2 = 4
izquierda2 = -4
vidas = 3
# Bucle principal
while True:
    clock.tick(50)  # Limita los FPS a 50

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Llenar la ventana con color azul
    ventana.fill(verde)

    # Actualizar la posición del cuadrado que rebota
    autos1 = autos1 + derecha
    autos2 = autos2 + izquierda
    autos3 = autos3 + derecha2
    autos4 = autos4 + izquierda2
    # Comprobar si el cuadrado rebota
    if autos1 >= 600:
        autos1 = 0

    if autos2 <= 0:
        autos2 = 600

    if autos3 >= 600:
        autos3 = 0

    if autos4 <= 0:
        autos4 = 600



    # Dibujar el cuadrado principal (rojo) que se mueve
    pygame.draw.rect(ventana, gris_mas_oscuro,(0,150,600, 400))
    pygame.draw.rect(ventana, gris, (0,200,600,300))
    pygame.draw.rect(ventana, gris_mas_oscuro, (0,340, 600, 20))
    pygame.draw.rect(ventana, blanco, (0, 260, 600, 10))
    pygame.draw.rect(ventana, blanco, (0, 425, 600, 10))
    
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("vidas"+ str(vidas,1, negro))
    ventana.blit(texto,(10,10))

    for i in range(2):
        pygame.draw.rect(ventana, rojo, (autos1, 450, 50,30))
        pygame.draw.rect(ventana, rojo, (autos1, 380, 50,30))
        pygame.draw.rect(ventana, rojo, (autos2, 220, 50,30))
        pygame.draw.rect(ventana, rojo, (autos2, 280, 50,30))
        pygame.draw.rect(ventana, rojo, (autos3, 450, 50,30))
        pygame.draw.rect(ventana, rojo, (autos3, 380, 50,30))
        pygame.draw.rect(ventana, rojo, (autos4, 220, 50,30))
        pygame.draw.rect(ventana, rojo, (autos4, 280, 50,30))

    # Actualizar la pantalla
    pygame.display.flip()