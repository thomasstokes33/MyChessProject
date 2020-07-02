import pygame
import math
import time as time1
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
currentx=1*75
currenty=2*75
movetox=3*75
movetoy=1*75
x=currentx
y=currenty

hor=abs(currentx-movetox)
vert=abs(currenty-movetoy)

print("hor: ",hor,"vert: ",vert)  #horizontal and vertical distance

distance=math.sqrt((abs(hor))**2+(abs(vert))**2)
print("d:",distance)
speed=210 #unitspersecond
time=distance/speed
print("t: "+str(time)) #time

framestaken=round((time/1)*30)
print("framestaken",framestaken)
xPerFrame=(hor/framestaken)
yPerFrame=(vert/framestaken)
print("x move",xPerFrame,"y move",yPerFrame)
thetick=0
hor=hor
vert=vert
if movetox<currentx:
    xPerFrame=-xPerFrame
    

if movetoy<currenty:
    yPerFrame=-yPerFrame
    
eggs=True
while eggs:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    
    pygame.display.update()
    clock.tick(30)
    thetick+=1
    print(x,y)
  
    if x==(movetox) and y==movetoy:
        eggs=False
    else:
        x=x+xPerFrame
        y=y+yPerFrame
        chessDisplay.blit(chessBoard,(0,0))
        chessDisplay.blit(image,(x,y))
        if round(x)==movetox and round(y)==movetoy:
            chessDisplay.blit(chessBoard,(0,0))
            chessDisplay.blit(image,(movetox,movetoy))
            eggs=False
            pygame.draw.rect(chessDisplay,blue,[movetox,(movetoy),75,75],1)
            pygame.display.update()
            print("finished",x,y)
            print(thetick)

#Note: I realised that I have to round frames, because there can only be a whole number of frames. 
