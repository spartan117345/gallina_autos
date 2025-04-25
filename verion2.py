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

# cargar las imagenes y cambiarles el tamaño
tanque = pygame.image.load("img/tanque.png")
tanque = pygame.transform.scale(tanque, (70, 50))  # Cambia el tamaño aquí


tanque2 = pygame.image.load("img/tanque2.png")
tanque2 = pygame.transform.scale(tanque2, (70,50))

auto4x4 = pygame.image.load("img/auto4x4.png")
auto4x4 = pygame.transform.scale(auto4x4, (70,50))
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

    if vidas <= 0:
        vidas = 0

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
    pygame.draw.rect(ventana, rojo, (autos2, 220, 50, 30))  # Auto 2
    pygame.draw.rect(ventana, cian, (autos3, 380, 50, 30))  # Auto 3
    pygame.draw.rect(ventana, rojo, (autos4, 280, 50, 30))  # Auto 4
    pygame.draw.rect(ventana, azul, (autos5, 280, 50, 30))  # Auto 5
    pygame.draw.rect(ventana, cian, (autos6, 220, 50, 30))  # Auto 6
    pygame.draw.rect(ventana, cafe, (150,50,100,80))# casa superior izquierda
    pygame.draw.lines(ventana, rojo,True, ((140, 50),(200,30),(200,30),(260,50)),3)# techo de la casa superior izquierda
    pygame.draw.rect(ventana, cafe, (350,50,100,80))# casa superior derecha
    pygame.draw.lines(ventana, rojo,True, ((340, 50),(400,30),(400,30),(460,50)),3)# techo de la casa superior derecha
    pygame.draw.rect(ventana, cafe, (50,610,100, 80 ))# casa a la izquierda de kfc
    pygame.draw.lines(ventana,rojo,True,((40,610),(100,590),(100,590),(160,610)),3)# techo de la casa a la izquierda de kfc
    pygame.draw.rect(ventana, cafe, (250, 610,100,80)) # KFC
    pygame.draw.lines(ventana, rojo,True,((240,610),(300,590),(300,590),(360,610)),3) # techo de KFC
    pygame.draw.rect(ventana, cafe, (450,610,100,80)) # casa a la derecha de kfc
    pygame.draw.lines(ventana, rojo, True,((450,610),(500,590),(500,590),(550,610)),3)# techo de la casa al lado derecho de kfc
    ventana.blit(tanque, (autos1, 440))
    ventana.blit(tanque2, (autos2, 210))
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
        texto_gameover = fuente_arial.render("GAME OVER", True, naranja)
        ventana.blit(texto_gameover, (200, 300))

    if YY1 <= 100 and vidas >= 1 :
        texto_gameover = fuente_arial.render("you win", True, rojo)
        ventana.blit(texto_gameover, (200, 300))

    
    texto_gameover = fuente_arial.render("KFC", True, blanco)
    ventana.blit(texto_gameover, (260, 630))

    # Actualizar la pantalla
    pygame.display.flip()