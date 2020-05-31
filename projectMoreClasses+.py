#1,1 = 0,0
import pprint
import pygame
import time
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
x=75 

bottom=x*7
bottom2=x*6
top=0
top2=x






class board1():
    '''keeps track of board'''
    def __init__(self):
             self.board=[['brook1', 'bknight1', 'bbishop1', 'bqueen', 'bking', 'bbishop2', 'bknight2', 'brook2'],
                         ['bpawn1', 'bpawn2', 'bpawn3', 'bpawn4', 'bpawn5', 'bpawn6', 'bpawn7', 'bpawn8'],
                         ['', '', '', '', '', '', '', ''],['', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', ''],['', '', '', '', '', '', '', ''],
                         ['wpawn1', 'wpawn2', 'wpawn3', 'wpawn4', 'wpawn5', 'wpawn6', 'wpawn7', 'wpawn8'],
                         ['wrook1', 'wknight1', 'wbishop1', 'wqueen', 'wking', 'wbishop2', 'wknight2', 'wrook2']]
    def display(self):#displays board
        for x in range(8):
            pprint.pprint(self.board[x],compact=False,width=100)

    def getpiece(self,mousex,mousey):
        return self.board[mousey][mousex]
        
    def emptySquare(self,x,y):
       
        if self.board[y][x] == '':
           
           return True
        else:
           
           return False
    def enemysquare(self,colour,x,y):
        pass
##        if colour=="black":
##            if self.board[y][x]
##        else:
##            
            
        
        
##[['brook1', 'bknight1', 'bbishop1', 'bqueen', 'bking', 'bbishop2', 'bknight2', 'broo:k2'],
##['bpawn1', 'bpawn2', 'bpawn3', 'bpawn4', 'bpawn5', 'bpawn6', 'bpawn7', 'bpawn8'],
##['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
##['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
##['wpawn1', 'wpawn2', 'wpawn3', 'wpawn4', 'wpawn5', 'wpawn6', 'wpawn7', 'wpawn8'],
##['wrook1', 'wknight1', 'wbishop1', 'wqueen', 'wking', 'wbishop2', 'wknight2', 'wrook2']]       
        

#self.rowA,self.rowB,self.rowC,self.rowD,self.rowE,self.rowF,self.rowG,self.rowH




class piece():
    '''Basic piece class'''
    def __init__(self,ptype,posy,posx,colour):
        self.ptype=ptype
        self.posy=posy
        self.posx=posx
        self.moveforw=0
        self.moveLorR=0
        self.movedyet=False
        self.colour=colour
    def update(self):
        chessDisplay.blit(self.image,((self.posx)*75,self.posy*75))

    def showSquares(self,availableSquarey,availableSquarex):
        counter=0
        for x in availableSquarey:
                
                  
                  pygame.draw.rect(chessDisplay,blue,[(availableSquarex[(counter)])*75,(x*75),75,75],1)
                  counter+=1
                  pygame.display.update()
        
        
        clicked1=pygame.mouse.get_pressed()
        while clicked1[0]==0: 
            pygame.event.get()
            clicked1=pygame.mouse.get_pressed()
            mouse1=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()    
                    quit()
        while clicked1[0]==1:
            pygame.event.get()
            clicked1=pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()    
                    quit()
        counter=0
        SquareToMoveTo=None,None
        for x in availableSquarey:
            if (mouse1[0]>(availableSquarex[counter]*75) and mouse1[0]<((availableSquarex[counter]*75)+75))and(mouse1[1]>x*75 and mouse1[1]<(x*75)+75):
                
                SquareToMoveTo=availableSquarex[counter],x
                
            counter+=1
        print("yippee")
        return SquareToMoveTo 

    def moveit(self,thesquare):
        squarex=thesquare[0]
        squarey=thesquare[1]
        print("x",squarex,"y",squarey)
        if squarex!=None and sqaurey!=None:
             if self.posx==squarex and self.posy==sqaurey:
                 pass
                 
                 
     
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
            chessDisplay.blit(self.image,((self.posx)*75,top))
        else:
            self.image=pygame.image.load('whiteking.png')        
            chessDisplay.blit(self.image,((self.posx)*75,bottom))
    def get_moves():
        pass
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
            chessDisplay.blit(self.image,((self.posx)*75,top))
        else:
            self.image=pygame.image.load('whitequeen.png')
            chessDisplay.blit(self.image,((self.posx)*75,bottom))

    def get_moves(self):
        pass
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
            chessDisplay.blit(self.image,((self.posx)*75,top))
        else:
            self.image=pygame.image.load('whiteknight.png')
            chessDisplay.blit(self.image,((self.posx)*75,bottom))

    def get_moves(self):
        pass
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
            chessDisplay.blit(self.image,((self.posx)*75,top))
        else:
            self.image=pygame.image.load('whiterook.png')
            chessDisplay.blit(self.image,((self.posx)*75,bottom))
    def get_moves(self):
        pass
        
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
            chessDisplay.blit(self.image,((self.posx)*75,top))
        else:
            self.image=pygame.image.load('whitebishop.png')
            chessDisplay.blit(self.image,((self.posx)*75,bottom))
    def get_moves(self):
        pass

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
            chessDisplay.blit(self.image,((self.posx)*75,top2))
        else:
            self.image=pygame.image.load('whitepawn.png')
            chessDisplay.blit(self.image,((self.posx)*75,bottom2))


    def get_moves(self):#calculates available moves
        
        if self.colour==turn:
                
##            if self.movedyet==False:#
          
                availableSquares=[]
                availableSquarex=[]
                for x in range(1,3):
                    
                    if self.colour=='white':
                        if self.movedyet==False:
                            
                            square=self.posy-x
                        else:
                            square=self.posy-1
                         
                    else:
                        if self.movedyet==False:
                            
                            square=self.posy+x
                        else:
                            square=self.posy+1
                    if (theboard.emptySquare(self.posx,square))==True:
       
                        availableSquares.append(square)
                        availableSquarex.append(self.posx)
                        
                    print(availableSquares)
                    

              
                    
                for x in range(-1,2):
                    if x==0:
                        pass
                    else:
                        if self.colour=='white':
                            
                            squarey=self.posy-1
                            squarex=self.posx+x
                            if (theboard.enemysquare("white",squarex,squarey))==True:
                            
                                availableSquares.append(squarey)
                                availableSquarex.append(squarex)
                            
                        else:
                            squarey=self.posy+1
                            squarex=self.posx+x

                            if (theboard.enemysquare("black",squarex,squarey))==True:
                            
                                availableSquares.append(squarey)
                                availableSquarex.append(squarex)                        
                    
                SquareToMoveTo =self.showSquares(availableSquares, availableSquarex)                    
                return SquareToMoveTo
        
##            else:#the pawn moves 1 most of the time
##                      
##                availableSquares=[]
##                availableSquarex=[]
##                for x in range(1,2):
##                    if self.colour=='white':
##                        
##                        square=self.posy-x
##                         
##                    else:
##                        square=self.posy+x
##                    if (theboard.emptySquare(self.posx,square))==True:
##       
##                        availableSquares.append(square)
##                        availableSquarex.append(self.posx)
##                        
##                    print(availableSquares)
##
##
##              
##                    
##                for x in range(-1,2):
##                    if x==0:
##                        pass
##                    else:
##                        if self.colour=='white':
##                            
##                            squarey=self.posy-1
##                            squarex=self.posx+x
##                            if (theboard.enemysquare(squarex,squarey))==True:
##                            
##                                availableSquares.append(squarey)
##                                availableSquarex.append(squarex)
##                        else:
##                            squarey=self.posy+1
##                            squarex=self.posx+x
##
##                            if (theboard.enemysquare(squarex,squarey))==True:
##                            
##                                availableSquares.append(squarey)
##                                availableSquarex.append(squarex)                        
                    
##            availableSquaresx=[]
##            availableSquaresy
##            for x in range(1,2):
##                if self.colour=='white':
##                    
##                    square=self.posy-x
##                    
##                    
##                         
##                         
##                         
##                else:
##                    square=self.posy+x
##                if theboard.emptySquare(self.posx,square)==True:
##                    availableSquares.append(square)
##                    
##                print(availableSquares)
            
         
 








clock=pygame.time.Clock()
def getmouse():
    mouse=pygame.mouse.get_pos()
    clicked=pygame.mouse.get_pressed()
    
    mousex,mousey=None,None
    currentPiece=''
    if clicked[0]==1:
        
        while clicked[0] == 1:
            random=pygame.event.get()
            clicked=pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()    
                    quit()
            
        
        mousex=mouse[0]//75
        mousey=mouse[1]//75
        print("x",mousex,"y",mousey)
        currentPiece=pieceInPos(mousex,mousey)
        
        
        
    return (mousex,mousey,currentPiece) 

def pieceInPos(mousex,mousey):
    piece=theboard.getpiece(mousex,mousey)
    return piece

def move():

    global currentPiece
    mousex,mousey,currentPiece=getmouse()
    if mousex!=None and mousey!=None:
         
        
        
        print("thisbit")
        try:
            
            print(mousex,mousey,currentPiece,)
            SquareTo=eval(currentPiece).get_moves()
            
            eval(currentPiece).moveit(SquareTo)
            
            
            
            print()
        except SyntaxError:
            print(mousex,mousey,"Square empty")
            print()

   
     
def update():
    chessDisplay.blit(chessBoard,(0,0))
    bpawn1.update()
    bpawn2.update()
    bpawn3.update()
    bpawn4.update()
    bpawn5.update()
    bpawn6.update()
    bpawn7.update()
    bpawn8.update()
    brook1.update()
    bknight1.update()
    bbishop1.update()
    bqueen.update()
    bking.update()
    bbishop2.update()
    bknight2.update()
    brook2.update()
    
    wpawn1.update()
    wpawn2.update()
    wpawn3.update()
    wpawn4.update()
    wpawn5.update()
    wpawn6.update()
    wpawn7.update()
    wpawn8.update()
    wrook1.update()
    wknight1.update()
    wbishop1.update()
    wking.update()
    wqueen.update()
    wbishop2.update()
    wknight2.update()
    wrook2.update()  

def start():
    
    gameExit=False 
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()    
                quit()
            

            move()
            update()
            pygame.display.update()
            clock.tick(10)
            
        
        
        
if __name__=="__main__":
    theboard=board1()
    chessBoard=pygame.image.load('board4.png')
    chessDisplay.blit(chessBoard,(0,0))
    theboard.display()
    print()
    print()
    list1=[]
    # Pygame pixel coordinates start in top left
    bpawn1=Pawn("pawn",1,0,"black")#y coordinate first.
    
    bpawn2=Pawn("pawn",1,1,"black")
    bpawn3=Pawn("pawn",1,2,"black")
    bpawn4=Pawn("pawn",1,3,"black")
    bpawn5=Pawn("pawn",1,4,"black")
    bpawn6=Pawn("pawn",1,5,"black")
    bpawn7=Pawn("pawn",1,6,"black")
    bpawn8=Pawn("pawn",1,7,"black")
    brook1=Rook("rook",0,0,"black")
    bknight1=Knight("knight",0,1,"black")
    bbishop1=Bishop("bishop",0,2,"black")
    bqueen=Queen("queen",0,3,"black")
    bking=King("king",0,4,"black")
    bbishop2=Bishop("bishop",0,5,"black")
    bknight2=Knight("knight",0,6,"black")
    brook2=Rook("rook",0,7,"black")
    
    wpawn1=Pawn("pawn",6,0,"white")
    wpawn2=Pawn("pawn",6,1,"white")
    wpawn3=Pawn("pawn",6,2,"white")
    wpawn4=Pawn("pawn",6,3,"white")
    wpawn5=Pawn("pawn",6,4,"white")
    wpawn6=Pawn("pawn",6,5,"white")
    wpawn7=Pawn("pawn",6,6,"white")
    wpawn8=Pawn("pawn",6,7,"white")
    wrook1=Rook("rook",7,0,"white")
    wknight1=Knight("knight",7,1,"white")
    wbishop1=Bishop("bishop",7,2,"white")
    wking=King("king",7,3,"white")
    wqueen=Queen("queen",7,4,"white")
    wbishop2=Bishop("bishop",7,5,"white")
    wknight2=Knight("knight",7,6,"white")
    wrook2=Rook("rook",7,7,"white")
    turn='white'
    
    start()



##              bpawn1
##            bpawn2
##            bpawn3
##            bpawn4
##            bpawn5
##            bpawn6
##            bpawn7
##            bpawn8
##            brook1
##            bknight1
##            bbishop1
##            bqueen
##            bking
##            bbishop2
##            bknight2
##            brook2
##            
##            wpawn1
##            wpawn2
##            wpawn3
##            wpawn4
##            wpawn5
##            wpawn6
##            wpawn7
##            wpawn8
##            wrook1
##            wknight1
##            wbishop1
##            wking
##            wqueen
##            wbishop
##            wknight2
##            wrook2  
#use breadth first to check for sqaures that can be taken.
