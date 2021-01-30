import pygame
import time
import random

#Definiciones globales
pygame.init()

pancho = 800
papitas = 600

areajuego = pygame.display.set_mode((pancho,papitas))
pygame.display.set_caption('Arkanoid del 3er mundo!')

black = (0,0,0)
white = (255,255,255)
rojo  = (255,0,0)

jancho = 100
jalto = 20

bloquey = 100
bloque2y = 200
bloquex = [0,100,200,300,400,500,600,700]
bloque2x = [0,100,200,300,400,500,600,700]

florderelos = pygame.time.Clock()

def text_objects(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text,x,y):
    largetext = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largetext)
    TextRect.center = (x,y)
    areajuego.blit(TextSurf, TextRect)


def game_loop():
    px = 395
    py = 295

    pelopancho = 15
    pelopalto = 15

    movpx = 5
    movpy = 5

    jposx = 350
    jposy = 560

    jmovx = 0

#PINTAR FONDO
    areajuego.fill(black)
#PINTAR Marco


    termino = False

    while not termino:
        pygame.draw.rect(areajuego, black, [jposx, jposy, jancho, jalto])
        pygame.draw.rect(areajuego, black, [px, py, pelopancho, pelopalto])
        pygame.draw.rect(areajuego, black, [0, bloquey, 800, 30])
        pygame.draw.rect(areajuego, black, [0, bloque2y, 800, 30])

        for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_0:
                            termino = True
                        if event.key == pygame.K_LEFT:
                            jmovx = -8
                            #print("A la izquierda")
                        elif event.key == pygame.K_RIGHT:
                            jmovx = 8
                            #print("A la derecha")
        
        
        if (jmovx < 0):
            if (jposx + jmovx) > 1:
                jposx = jposx + jmovx
        else:
            if (jposx + jmovx) < 699:
                jposx = jposx + jmovx

        for b in bloquex:
            pygame.draw.rect(areajuego, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), [b, bloquey, 100, 30])
        for b2 in bloque2x:
            pygame.draw.rect(areajuego, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), [b2, bloque2y, 100, 30])

        #print(px)
        #print(py)
        #print(movpy)
        #print(" - ")
        if (movpx < 0):
            if (px + movpx) > 1:
                px = px + movpx
            else:
                movpx = 5
                px = px + movpx
        else:
            if (px + movpx) < 799:
                px = px + movpx
            else:
                movpx = -5
                px = px + movpx

        if (movpy > 0):
            if (py <= bloquey+30) and ((py+pelopalto) >= bloquey):
                for l in bloquex:
                    if ((px+pelopancho) >= l) and (px <= (l+100)):
                        bloquex.remove(l)
            if (py <= bloque2y+30) and ((py+pelopalto) >= bloque2y):
                for l2 in bloque2x:
                    if ((px+pelopancho) >= l2) and (px <= (l2+100)):
                        bloque2x.remove(l2)
            
            if ((py+pelopalto) >= jposy) and ((px+pelopancho) >= jposx) and (px <= (jposx+jancho)):
                movpy = -5
                py = py + movpy
                if (jmovx > 0):
                    movpx = 5
                else:
                    movpx = -5
            if (py > jposy+jalto):
                termino = True
            else:
                py = py + movpy

        else:
            if (py <= bloquey+30) and ((py+pelopalto) >= bloquey):
                for l in bloquex:
                    if ((px+pelopancho) >= l) and (px <= (l+100)):
                        bloquex.remove(l)
            if (py <= bloque2y+30) and ((py+pelopalto) >= bloque2y):
                for l2 in bloque2x:
                    if ((px+pelopancho) >= l2) and (px <= (l2+100)):
                        bloque2x.remove(l2)
            if ((py + movpy) > 0):
                py = py + movpy
            else:
                movpy = 5 
                py = py + movpy

        pygame.draw.rect(areajuego, (0,random.randrange(0,255),0), [px, py, pelopancho, pelopalto])
        pygame.draw.rect(areajuego, (random.randrange(0,255),0,0), [jposx, jposy, jancho, jalto])
        
        pygame.display.update()
        florderelos.tick(60)
        if (len(bloquex) == 0) and (len(bloque2x) == 0):
            termino = True
    return len(bloquex)+len(bloque2x)


def main():

    #Cuerpo del programa que llama al juego
    areajuego.fill(black)
    restantes = game_loop()
    time.sleep(2)
    if (restantes > 0):
        mensaje = "Cantidad de ladrillos faltantes: " + str(restantes)
    else:
        mensaje = "GANASTE!!!"
    print(mensaje)
    #areajuego.fill(black)
    message_display(mensaje,400,300)
    pygame.display.update()
    time.sleep(4)
    pygame.quit()
    quit()



if __name__ == "__main__":
    main()
