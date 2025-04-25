import pygame
import sys

# Inicialización
pygame.init()

# Colores
amarillo = (187, 173, 4)
amarilo_oscuro = (142, 130, 10 )
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (52, 237, 11)
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
# Variable de vidas
vidas = 3

# Variables del jugador
XX1 = 290
YY1 = 630

# Crear ventana
ventana = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Por qué la gallina cruzó la calle")

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Fuente para mostrar el texto de vidas
fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)

# Variables para los autos
autos1 = 0
autos2 = 600
autos3 = 0
autos4 = 600
autos5 = 700
autos6 = 700
derecha = 2
izquierda = -2
derecha2 = 4
izquierda2 = -4

# Bucle principal
while True:
    clock.tick(50)  # Limita los FPS a 50

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Llenar la ventana con color verde
    ventana.fill(verde)

    # Movimiento de los autos
    autos1 += derecha
    autos2 += izquierda
    autos3 += derecha2
    autos4 += izquierda2
    autos5 += izquierda2
    autos6 += izquierda

    # Comprobar si los autos salen de la pantalla y reiniciarlos
    if autos1 >= 600:
        autos1 = -50
    if autos2 <= -50:
        autos2 = 600
    if autos3 >= 600:
        autos3 = -50
    if autos4 <= -50:
        autos4 = 600
    if autos5 <= -50:
        autos5 = 600
    if autos6 <= -50:
        autos6 = 600

    # Movimiento de la gallina con teclas (se usa get_pressed() para un movimiento más fluido)
    keys = pygame.key.get_pressed()  # Obtiene todas las teclas presionadas
    if keys[pygame.K_w]:  # Tecla W (arriba)
        YY1 -= 3
    if keys[pygame.K_s]:  # Tecla S (abajo)
        YY1 += 3
    if keys[pygame.K_a]:  # Tecla A (izquierda)
        XX1 -= 3
    if keys[pygame.K_d]:  # Tecla D (derecha)
        XX1 += 3

    # Dibujar objetos
    pygame.draw.rect(ventana, gris_mas_oscuro, (0, 150, 600, 400))  # Suelo oscuro
    pygame.draw.rect(ventana, gris, (0, 200, 600, 300))  # Suelo claro
    pygame.draw.rect(ventana, gris_mas_oscuro, (0, 340, 600, 20))  # Línea divisoria
    pygame.draw.rect(ventana, amarillo, (XX1, YY1, 40, 40))  # Gallina
    pygame.draw.rect(ventana, rojo, (autos1, 450, 50, 30))  # Auto 1
    pygame.draw.rect(ventana, rojo, (autos2, 220, 50, 30))  # Auto 2
    pygame.draw.rect(ventana, rojo, (autos3, 380, 50, 30))  # Auto 3
    pygame.draw.rect(ventana, rojo, (autos4, 280, 50, 30))  # Auto 4
    pygame.draw.rect(ventana, rojo, (autos5, 280, 50, 30))  # Auto 5
    pygame.draw.rect(ventana, rojo, (autos6, 220, 50, 30))  # Auto 6

    # Detección de colisiones
    gallina_rect = pygame.Rect(XX1, YY1, 40, 40)
    auto_rects = [
        pygame.Rect(autos1, 450, 50, 30),
        pygame.Rect(autos2, 220, 50, 30),
        pygame.Rect(autos3, 380, 50, 30),
        pygame.Rect(autos4, 280, 50, 30),
        pygame.Rect(autos5, 280, 50, 30),
        pygame.Rect(autos6, 220, 50, 30)
    ]
    
    for auto_rect in auto_rects:
        if gallina_rect.colliderect(auto_rect):
            vidas -= 1  # Decrementar vidas al colisionar

    # Actualizar texto de vidas
    texto = fuente_arial.render("Vidas: " + str(vidas), True, negro)
    ventana.blit(texto, (10, 10))

    # Verificar si el juego termina
    if vidas <= 0:
        texto_gameover = fuente_arial.render("GAME OVER", True, rojo)
        ventana.blit(texto_gameover, (200, 300))

    # Actualizar la pantalla
    pygame.display.flip()