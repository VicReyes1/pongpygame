import pygame

def main():
    pygame.init() #inicia pygame
    size = 800,600 #tamaño de la ventana
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Mi primer juego")

    width, height = 800,600
    speed = [2, 2]
    white = 255, 255, 255

    #se carga una imagen
    ball = pygame.image.load('/Users/victorserranoreyes/Desktop/balon.png')
    ballrect = ball.get_rect();
    

    #barra de rebote
    barra = pygame.image.load('/Users/victorserranoreyes/Desktop/barra.png')
    barrarect = barra.get_rect()
    barra2 = pygame.image.load('/Users/victorserranoreyes/Desktop/barra.png')
    barrarect2 = barra2.get_rect()


    #se ubica la barra a la mita de la ventana
    barrarect.move_ip(50,260)
    barrarect2.move_ip(750, 260)
    
    run = True
    while run:
        pygame.time.delay(5) #delay que contralará la velocidad            
        
        for event in pygame.event.get(): #se captura el evento que se produce
            if event.type == pygame.QUIT:
                run = False

        #se detecata si se ha pulsado alguna tecla
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            barrarect = barrarect.move(0, -1)
        if keys[pygame.K_s]:
            barrarect = barrarect.move(0, 1)
        if keys[pygame.K_UP]:
            barrarect2 = barrarect2.move(0, -1)
        if keys[pygame.K_DOWN]:
            barrarect2 = barrarect2.move(0, 1)
        

        #se detemina si hay colisiones 
        if barrarect.colliderect(ballrect):
            speed[0] = -speed[0]
        if barrarect2.colliderect(ballrect):
            speed[0] = -speed[0]

        ballrect = ballrect.move(speed) #se mueve el objeto
        #se determinan los límites del objeto
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        


        #se borra la pantalla anterior con el fondo blanco
        screen.fill(white)
        screen.blit(ball, ballrect)
        screen.blit(barra,barrarect)
        screen.blit(barra2,barrarect2)
        pygame.display.flip()
    pygame.quit() #se termina el juego

if __name__ == "__main__":
    main()