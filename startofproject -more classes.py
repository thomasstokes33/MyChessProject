#1,1 = 0,0
x=75 
import pprint
import pygame
pygame.init()
displayWidth=600
displayHeight=600
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

chessDisplay=pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Chess')

bottom=x*7
bottom2=x*6
top=0
top2=x






class board1():
    def __init__(self):
        self.rowA={1:'br1',2:'bn1',3:'bb1',4:'bk1',5:'bq1',6:'bb2',7:'bn2',8:'br2'}
        self.rowB={1:'bp1',2:'bp2',3:'bp3',4:'bp4',5:'bp5',6:'bp6',7:'bp7',8:'bp8'}
        self.rowC={1:'   ',2:'   ',3:'   ',4:'   ',5:'   ',6:'   ',7:'   ',8:'   '}
        self.rowD={1:'   ',2:'   ',3:'   ',4:'   ',5:'   ',6:'   ',7:'   ',8:'   '}
        self.rowE={1:'   ',2:'   ',3:'   ',4:'   ',5:'   ',6:'   ',7:'   ',8:'   '}
        self.rowF={1:'   ',2:'   ',3:'   ',4:'   ',5:'   ',6:'   ',7:'   ',8:'   '}
        self.rowG={1:'wp1',2:'wp2',3:'wp3',4:'wp4',5:'wp5',6:'wp6',7:'wp7',8:'wp8'}
        self.rowH={1:'wr1',2:'wn1',3:'wb1',4:'wk1',5:'wq1',6:'wb2',7:'wn2',8:'wr2'}
    def display(self):
        pprint.pprint((self.rowA.values(),self.rowB.values(),self.rowC.values(),self.rowD.values(),self.rowE.values(),self.rowF.values(),self.rowG.values(),self.rowH.values()))

#self.rowA,self.rowB,self.rowC,self.rowD,self.rowE,self.rowF,self.rowG,self.rowH 




class piece():
    def __init__(self,ptype,posy,posx,colour):
        self.ptype=ptype
        self.posy=posy
        self.posx=posx
        self.moveforw=0
        self.moveLorR=0
        self.movedyet=False
        self.colour=colour
         

class King(piece):
    def __init__(self,ptype,posy,posx,colour):
        self.ptype=ptype
        self.posy=posy
        self.posx=posx
        self.moveforw=0
        self.moveLorR=0
        self.movedyet=False
        self.colour=colour
        if self.colour=='black':
            self.image=pygame.image.load("blackking.png")
            chessDisplay.blit(self.image,((self.posx-1)*75,top))
        else:
            self.image=pygame.image.load('whiteking.png')        
            chessDisplay.blit(self.image,((self.posx-1)*75,bottom))

class Queen(piece):
    def __init__(self,ptype,posy,posx,colour):
        self.ptype=ptype
        self.posy=posy
        self.posx=posx
        self.moveforw=0
        self.moveLorR=0
        self.movedyet=False
        self.colour=colour
        if self.colour=='black':
            self.image=pygame.image.load("blackqueen.png")
            chessDisplay.blit(self.image,((self.posx-1)*75,top))
        else:
            self.image=pygame.image.load('whitequeen.png')
            chessDisplay.blit(self.image,((self.posx-1)*75,bottom))
            
class Knight(piece):
    def __init__(self,ptype,posy,posx,colour):
        self.ptype=ptype
        self.posy=posy
        self.posx=posx
        self.moveforw=0
        self.moveLorR=0
        self.movedyet=False
        self.colour=colour
        if self.colour=='black':
            self.image=pygame.image.load("blackknight.png")
            chessDisplay.blit(self.image,((self.posx-1)*75,top))
        else:
            self.image=pygame.image.load('whiteknight.png')
            chessDisplay.blit(self.image,((self.posx-1)*75,bottom))

 
class Rook(piece):
    def __init__(self,ptype,posy,posx,colour):
        self.ptype=ptype
        self.posy=posy
        self.posx=posx
        self.moveforw=0
        self.moveLorR=0
        self.movedyet=False
        self.colour=colour
        if self.colour=='black':
            self.image=pygame.image.load("blackrook.png")
            chessDisplay.blit(self.image,((self.posx-1)*75,top))
        else:
            self.image=pygame.image.load('whiterook.png')
            chessDisplay.blit(self.image,((self.posx-1)*75,bottom))
        
class Bishop(piece):
    def __init__(self,ptype,posy,posx,colour):
        self.ptype=ptype
        self.posy=posy
        self.posx=posx
        self.moveforw=0
        self.moveLorR=0
        self.movedyet=False
        self.colour=colour
        if self.colour=='black':
            self.image=pygame.image.load("blackbishop.png")
            chessDisplay.blit(self.image,((self.posx-1)*75,top))
        else:
            self.image=pygame.image.load('whitebishop.png')
            chessDisplay.blit(self.image,((self.posx-1)*75,bottom))
class Pawn(piece):
    def __init__(self,ptype,posy,posx,colour):
        self.ptype=ptype
        self.posy=posy
        self.posx=posx
        self.moveforw=0
        self.moveLorR=0
        self.movedyet=False
        self.colour=colour
        if self.colour=='black':
            self.image=pygame.image.load("blackpawn.png")
            chessDisplay.blit(self.image,((self.posx-1)*75,top2))
        else:
            self.image=pygame.image.load('whitepawn.png')
            chessDisplay.blit(self.image,((self.posx-1)*75,bottom2))






 















clock=pygame.time.Clock()
def getmouse():
    mouse=pygame.mouse.get_pos()
    print(mouse)



def move():
    getmouse()
    

def board():
    theboard=board1()
    chessBoard=pygame.image.load('board2.png')
    chessDisplay.blit(chessBoard,(0,0))
    theboard.display()
    bpawn1=Pawn("pawn",2,1,"black")
    bpawn2=Pawn("pawn",2,2,"black")
    bpawn3=Pawn("pawn",2,3,"black")
    bpawn4=Pawn("pawn",2,4,"black")
    bpawn5=Pawn("pawn",2,5,"black")
    bpawn6=Pawn("pawn",2,6,"black")
    bpawn7=Pawn("pawn",2,7,"black")
    bpawn8=Pawn("pawn",2,8,"black")
    brook1=Rook("rook",1,1,"black")
    bknight1=Knight("knight",1,2,"black")
    bbishop1=Bishop("bishop",1,3,"black")
    bqueen=Queen("queen",1,5,"black")
    bking=King("king",1,4,"black")
    bbishop2=Bishop("bishop",1,6,"black")
    bknight2=Knight("knight",1,7,"black")
    brook2=Rook("rook",1,8,"black")
    
    wpawn1=Pawn("pawn",7,1,"white")
    wpawn2=Pawn("pawn",7,2,"white")
    wpawn3=Pawn("pawn",7,3,"white")
    wpawn4=Pawn("pawn",7,4,"white")
    wpawn5=Pawn("pawn",7,5,"white")
    wpawn6=Pawn("pawn",7,6,"white")
    wpawn7=Pawn("pawn",7,7,"white")
    wpawn8=Pawn("pawn",7,8,"white")
    wrook1=Rook("rook",8,1,"white")
    wknight1=Knight("knight",8,2,"white")
    wbishop1=Bishop("bishop",8,3,"white")
    wking=King("king",8,4,"white")
    wqueen=Queen("queen",8,5,"white")
    wbishop2=Bishop("bishop",8,6,"white")
    wknight2=Knight("knight",8,7,"white")
    wrook2=Rook("rook",8,8,"white")



def start():
    
    gameExit=False
    newboard=board()
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()    
                quit()
         
            move()
            pygame.display.update()
            clock.tick(60)
            
        
        
        
if __name__=="__main__":
    
    start()
    
