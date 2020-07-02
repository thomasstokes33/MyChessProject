import math
import pygame
pygame.init()

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
chessDisplay=pygame.display.set_mode((600,600))
clock=pygame.time.Clock()
chessBoard=pygame.image.load('board4.2.png')
chessDisplay.blit(chessBoard,(0,0))
image=pygame.image.load("blackpawn.png")
chessDisplay.blit(image,((0)*75,1*75))
currentx=0*75
currenty=0*75
movetox=0*75
movetoy=1*75
x=currentx
y=currenty


eggs=True
while eggs:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        print(event)
    pygame.display.update()
    clock.tick(30)
