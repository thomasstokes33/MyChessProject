#1,1 = 0,0,
import pprint
import pygame
import time
import math  #imports modules
pygame.init()
displayWidth=600
displayHeight=600
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
movedList=open("movedList.txt","w")
movedList.write("movedlist")

movedList.close()
chessDisplay=pygame.display.set_mode((displayWidth,displayHeight))#sets up display
pygame.display.set_caption('Chess')#sets caption of window
icon=pygame.image.load("whitepawn.png")
pygame.display.set_icon(icon)
x=75 

bottom=x*7
bottom2=x*6
top=0
top2=x
clock=pygame.time.Clock()
def getpiece(board,mousex,mousey):
        return board[mousey][mousex]

def isemptySquare(board,x,y):

        if board[y][x] == '':
           
           return True
        else:
           
           return False

def isenemysquare(board,colour,x,y):
        #pass
        try:
            character=board[y][x]
            if colour=="black":
                 
                if character[0]=='w':
                       return True  
            else:
                if character[0]=='b':
                    return True
        except IndexError:
            # print("empty")
            return False




class board1():
    '''keeps track of board'''
    def __init__(self):
             self.board=[['brook1', 'bknight1', 'bbishop1', 'bqueen', 'bking', 'bbishop2', 'bknight2', 'brook2'],
                         ['bpawn1', 'bpawn2', 'bpawn3', 'bpawn4', 'bpawn5', 'bpawn6', 'bpawn7', 'bpawn8'],
                         ['', '', '', '', '', '', '', ''],['', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', ''],['', '', '', '', '', '', '', ''],
                         ['wpawn1', 'wpawn2', 'wpawn3', 'wpawn4', 'wpawn5', 'wpawn6', 'wpawn7', 'wpawn8'],
                         ['wrook1', 'wknight1', 'wbishop1', 'wqueen', 'wking', 'wbishop2', 'wknight2', 'wrook2']]
                         #the array above tracks the position of every piece. 
    def newpiece(self,newpiecex,newpiecey,pieceName):
        self.board[newpiecey][newpiecex]=pieceName
    def display(self):# method which displays board
        for x in range(8):
            pprint.pprint(self.board[x],compact=False,width=100)
    def currentBoard(self):
        returnboard=[]
        for x in range(8):
            returnboard.append([])
        count=0
        for y in self.board:
            for x in y:
                returnboard[count].append(x)
            count+=1
        return returnboard

    def getpiece(self,mousex,mousey):#this fetches the piece specified by paramters
        return self.board[mousey][mousex]
        
    def emptySquare(self,x,y):#this checks if the square specified is empty. 
        # print(x,y,"is empty square")
        if self.board[y][x] == '':
 

           return True
        else:

           return False
    def friendlysquare(self,x,y,colour):#this checks if the square contains a piece of the current players.
        try:  
            squareInQuestion=str(self.board[y][x])

            
            if squareInQuestion=='':
                return False
            else:
                team=squareInQuestion[0]
                if team=='b' and colour=='black':
                    return True
                elif team=='w' and colour=='white':
                    return True
                else:
                    return False
        except IndexError:
            # print("empty or no enemy or off board frien")
            pass
             


        
    def enemysquare(self,colour,x,y):#checks if it is an enemy square

        try:
            character=self.board[y][x]
            if colour=="black":
                 
                if character[0]=='w':
                       return True  
            else:
                if character[0]=='b':
                    return True
        except IndexError:
            # print("empty or no enemy  or off board enem")
            return False
        
    def move(self,currentx,currenty,newx,newy):#this updates the array after a piece has moved. 
        record=self.board[currenty][currentx]
        self.board[currenty][currentx]=''
        self.board[newy][newx]=record
        self.display()
              
              
            
            
        
        
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
        self.checkmateAlg=False
        self.checkmateMoves=False
    def update(self):
        chessDisplay.blit(self.image,((self.posx)*75,self.posy*75))
    def coordinates(self):
        return self.posx,self.posy
    def upgradePawn(self,piece,colour_of_piece):
        update(colour_of_piece)
        if colour_of_piece=='black':
            pygame.draw.rect(chessDisplay,white,(150,262,300,75))
            pygame.draw.rect(chessDisplay,black,(150,262,300,75),1)
            blackqueen=pygame.image.load("blackqueen.png")
            blackknight=pygame.image.load("blackknight.png")
            blackrook=pygame.image.load("blackrook.png")
            blackbishop=pygame.image.load("blackbishop.png")
            chessDisplay.blit(blackqueen,(150,262))
            chessDisplay.blit(blackknight,(225,262))
            chessDisplay.blit(blackrook,(300,262))
            chessDisplay.blit(blackbishop,(375,262))
        else:
            pygame.draw.rect(chessDisplay,white,(150,262,300,75))
            pygame.draw.rect(chessDisplay,black,(150,262,300,75),1)
            whitequeen=pygame.image.load("whitequeen.png")
            whiteknight=pygame.image.load("whiteknight.png")
            whiterook=pygame.image.load("whiterook.png")
            whitebishop=pygame.image.load("whitebishop.png")
            chessDisplay.blit(whitequeen,(150,262))
            chessDisplay.blit(whiteknight,(225,262))
            chessDisplay.blit(whiterook,(300,262))
            chessDisplay.blit(whitebishop,(375,262))
            
        
        pygame.display.update()
        clicked1=pygame.mouse.get_pressed()
        mouse1=pygame.mouse.get_pos()
        while clicked1[0]==0 or (mouse1[0]>450 or mouse1[0]<150 or mouse1[1]>337 or  mouse1[1]<262): 
            pygame.event.get()
            clicked1=pygame.mouse.get_pressed()
            mouse1=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()    
                    quit()
        
        if mouse1[1]>=262 and mouse1[1]<=337:
            if mouse1[0]>=150 and mouse1[0]<=225:#queen
                print("queen")
                number=piece[5]
                upgradePawn1=(self.colour[0]+'queen'+number)
                upgradeType='queen'
                globals()[upgradePawn1]=Queen(upgradeType.lower(),self.posy,self.posx,self.colour)#don't eval whole thing
            if mouse1[0]>=225 and mouse1[0]<=300:#knight
                print("knight")
                number=piece[5]
                upgradePawn1=(self.colour[0]+'knight'+number)
                upgradeType='knight'
                globals()[upgradePawn1]=Knight(upgradeType.lower(),self.posy,self.posx,self.colour)
            if mouse1[0]>=300 and mouse1[0]<=375:#rook
                print("rook")
                number=piece[5]
                upgradePawn1=(self.colour[0]+'rook'+number)
                upgradeType='rook'
                globals()[upgradePawn1]=Rook(upgradeType.lower(),self.posy,self.posx,self.colour)
            if mouse1[0]>=375 and mouse1[0]<=450:#bishop
                print("bishop")
                number=piece[5]
                upgradePawn1=(self.colour[0]+'bishop'+number)
                upgradeType='bishop'
                globals()[upgradePawn1]=Bishop(upgradeType.lower(),self.posy,self.posx,self.colour)

        allPieces.remove(piece)    
        theboard.newpiece(self.posx,self.posy,upgradePawn1)
        if self.colour=='black':
            allPieces.insert(0,upgradePawn1)
        else:
            allPieces.insert(-1,upgradePawn1)

        
            
    def showSquares(self,availableSquarey,availableSquarex,xPerFrame,yPerFrame):
        counter=0
        for x in availableSquarey:
                
                  
                  pygame.draw.rect(chessDisplay,blue,((availableSquarex[(counter)])*75,(x*75),75,75),1)
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
        xPerFrame,yPerFrame=None,None
        for x in availableSquarey:
            if (mouse1[0]>(availableSquarex[counter]*75) and mouse1[0]<((availableSquarex[counter]*75)+75))and(mouse1[1]>x*75 and mouse1[1]<(x*75)+75):
                
                SquareToMoveTo=availableSquarex[counter],x
                print("moving")
                xPerFrame,yPerFrame=self.distancePerFrame(SquareToMoveTo[0],SquareToMoveTo[1])
 

                
            counter+=1
        print("yippee")
        return SquareToMoveTo,xPerFrame,yPerFrame

    def moveit(self,thesquare,xPerFrame,yPerFrame,turn,current_piece):
        lastposx=self.posx
        lastposy=self.posy
        #maybe add a a attribute called last square or even attributes for the moving created in the algorithm above
        squarex=thesquare[0]
        squarey=thesquare[1]
        print("moveit","x",squarex,"y",squarey,xPerFrame)
        
        while round(self.posx,1)!=squarex or round(self.posy,1)!=squarey:
            clicked1=pygame.mouse.get_pressed()
            self.posx=self.posx+(xPerFrame/75)
            self.posy=self.posy+(yPerFrame/75)
            update(turn)
            self.update()
            pygame.display.update()
            clock.tick(30)
            
            
        
        self.posx=squarex
        self.posy=squarey
        takenPiece=theboard.getpiece(self.posx,self.posy)
        print(takenPiece)
        theboard.move(lastposx,lastposy,squarex,squarey)
        self.movedyet=True
        if takenPiece!='':
            allPieces.remove(takenPiece)
        if self.ptype=='pawn':
            if self.colour=='black' and self.posy==7:
                print("upgrade")
                self.upgradePawn(current_piece,self.colour)
            elif self.colour=='white' and self.posy==0:
                print("upgrade")
                self.upgradePawn(current_piece,self.colour)
        movedList=open("movedlist.txt","a+")
        movedList.write("\n"+current_piece)
        movedList.close()



 
        return False
    
    def distancePerFrame(self,movetox,movetoy):
        movetox=movetox*75
        movetoy=movetoy*75
        currentx=self.posx*75
        currenty=self.posy*75
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
        if movetox<currentx:
            xPerFrame=-xPerFrame
            

        if movetoy<currenty:
            yPerFrame=-yPerFrame
                    
        return xPerFrame,yPerFrame

    def endangersKing(self,colour,movetox,movetoy):
        print("KEY",movetox,movetoy)
        board_temp= theboard.currentBoard()
        record=board_temp[self.posy][self.posx]
        board_temp[self.posy][self.posx]=''
        
       
        board_temp[movetoy][movetox]=record
        
        # pp=pprint.PrettyPrinter(indent=1,width=100)
        # pp.pprint(board_temp)
        tempY=0
        print(colour)
        for y in board_temp:
            try:
                if colour=='white':
                    thex=y.index("wking")
                    they=tempY
                    print(thex)
                else:
                    thex=y.index("bking")
                    they=tempY
                    print(thex)
                tempY+=1
            except ValueError:
                
                tempY+=1
        print(theboard.getpiece(thex,they))
        if ( self.minicheck(board_temp,colour,thex,they) ==False) :#mini check finds if
                                                                          # new move results in king in danger. 
            # # availableSquares.append(square)
            # availableSquarex.append(self.posx)  
            print("no minicheck")
            
            return False
    

    def minicheck(self,board,colour,x,y):
        #diagonal
        print(x,y)
        diagonal=self.diagonalsclear(board,colour,x,y)


        if (diagonal==False):  
            print("diagonals are danger")
            return True
       
        ##straights
        straights=self.straightsclear(board,colour,x,y)
        
        if straights==False:
            print("straights are danger")
            return True
       

        
        ##adjacent for king and pawns
        adjacent=self.adjacentclear(board,colour,x,y)
        if (adjacent==False):
            print("adjacents aren't clear")
            return True          
       
        ##knight
        knight=self.knightclear(board,colour,x,y)
        if (knight==False):
            print("knight are danger")
            return True
       
        return False
       
    def recursive2(self,board,colour,x,y,currentx,currenty,tempDiagonalDangerPieces):#the other recursive algorithm was being called
       
        if ((currentx+x>7)or(currentx+x<0))or((currenty+y<0)or(currenty+y>7)):#wrong position at first. this error must be checked for first
            return True
        elif isenemysquare(board,colour,currentx+x,currenty+y)==True:
            thepiece=getpiece(board,currentx+x,currenty+y)
            
            try:
                if thepiece[1]=='q' or thepiece[1]=='b':
                    
                    if self.checkmateAlg==False:
                        for o in tempDiagonalDangerPieces:

                            dangerPieces.append(o)
                    dangerPieces.append(thepiece) 
                    
                    return False
                else:
                    return True
            except:
            
                return True
        elif isemptySquare(board,currentx+x,currenty+y)==False:
            return True


        else:
            print("currentx+x,currenty+y",currentx+x,currenty+y)
            tempDiagonalDangerPieces.append([currentx+x,currenty+y])
            value=self.recursive2(board,colour,x,y,currentx+x,currenty+y,tempDiagonalDangerPieces) 
            if value==True:
                return True
            else:#it wasn't true so it returned false, this was a big problem.
                return False     

        
    


    def diagonalsclear(self,board,colour,posx,posy) :
        originalx=posx
        originaly=posy
        for y in range(-1,2):
            posx=originalx
            posy=originaly
            if (y==0):
                pass
            else:
                for x in range(-1,2):
                    if (x==0):
                        pass
                    
                    else:
                        tempDiagonalDangerPieces=[]
                        print("x and y",x,y)
                        returnvalue=self.recursive2(board,colour,x,y,posx,posy,tempDiagonalDangerPieces)
                        if self.checkmateAlg==False:
                            if returnvalue==False:
                                return False
                        
            
        return True            
                            
                            
                    

    def straightsclear( self,board,colour,posx,posy):
        horizontalclear=True
        verticalclear= True
        originalx=posx
        originaly=posy
        for x in range(-1,2):
            posx=originalx
            posy=originaly
            if x==0:
                pass
            else:

                if horizontalclear==True:
                    tempDangerPieces=[]
                    while posx+x<=7 and posx+x>=0 and posy<=7 and posy>=0 and isemptySquare(board,posx+x,posy)==True and horizontalclear==True:
                        posx+=x
                        tempDangerPieces.append([posx,posy])
                    if isenemysquare(board,colour,posx+x,posy)==True and posx+x>-1 and posx+x<8:
                        thepiece=getpiece(board,posx+x,posy)
                        if thepiece[1]=='q' or thepiece[1]=='r':
                            if self.checkmateAlg ==False:
                                for o in tempDangerPieces:
                                    dangerPieces.append(o)
                            dangerPieces.append(thepiece)
                            if self.checkmateAlg ==False:
                                horizontalclear=False        
                    else:
                        horizontalclear=True 
                    
       
        
        for y in range(-1,2): 
            
            posx=originalx
            posy=originaly
            if y==0:#was x ==0
                
                pass
            else:
                if verticalclear==True:
                    tempDangerPieces=[]
                    while posy+y<=7 and posy+y>=0 and posx<=7 and posx>=0 and isemptySquare(board,posx,posy+y)==True and verticalclear==True:
                        posy+=y 
                        tempDangerPieces.append([posx,posy])

                    if isenemysquare(board,colour,posx,posy+y)==True and posy+y>-1 and posy+y<8 :
                        thepiece=getpiece(board,posx,posy+y)
                      
                        if thepiece[1]=='q' or thepiece[1]=='r':
                            if self.checkmateAlg==False:
                                for o in tempDangerPieces:
                                    dangerPieces.append(o)
                            dangerPieces.append(thepiece) 
                            if self.checkmateAlg ==False:
                                verticalclear=False  
                    else:
                        verticalclear=True
      
        if horizontalclear==True and verticalclear==True:
            return True
        else:
            return False

        
    def knightclear(self,board,colour,posx,posy): 

        long1=[2,-2]
        short=[1,-1]
        for x in long1:
            for y in short:
                if posx+x <8 and posx+x >-1 and posy+y<8 and posy+y>-1:
                    if isenemysquare(board,colour,posx+x,posy+y )==True:
                        thepiece=getpiece(board,posx+x,posy+y)
               
                        if thepiece[1]=='k' and thepiece[2]=='n':
                            dangerPieces.append(thepiece)
                            if self.checkmateAlg==False:
                                return False


        
        for y in long1:
            for x in short:
                if posx+x <8 and posx+x >-1 and posy+y<8 and posy+y>-1:
                    if isenemysquare(board,colour,posx+x,posy+y)==True:
                        thepiece=getpiece(board,posx+x,posy+y)
                      
                        if thepiece[1]=='k' and thepiece[2]=='n':
                            dangerPieces.append(thepiece)
                            if self.checkmateAlg==False:
                                return False


        
        return True
    def adjacentclear(self,board,colour,posx,posy):
        for x in range(-1,2):
                if posx+x <8 and posx+x >-1 and posy<8 and posy>-1:
                    if isenemysquare(board,colour,posx+x,posy )==True:
                        thepiece=getpiece(board,posx+x,posy)
                        
                        if thepiece[1]=='k' and thepiece[2]=='i':
                            dangerPieces.append(thepiece)
                            if self.checkmateAlg==False:
                                return False
        for y in range(-1,2):
                if posx <8 and posx >-1 and posy+y<8 and posy+y>-1:
                    if isenemysquare(board,colour,posx,posy+y)==True:
                        thepiece=getpiece(board,posx,posy+y)
                        
                        if thepiece[1]=='k' and thepiece[2]=='i':
                            dangerPieces.append(thepiece)
                            if self.checkmateAlg==False:
                                return False      
        for y in range(-1,2):
            if (y==0):
                pass
            else:
                for x in range(-1,2):
                    if (x==0):
                        pass
                    else:
                     
                        
                        if colour=='black':
                            if posx+x<8 and posx+x>-1 and posy+y<8 and posy+y>-1 and isenemysquare(board,colour,posx+x,posy+y)==True:
                                thepiece=getpiece(board,posx+x,posy+y)
                                
                                if (thepiece[1]=='p'and posy+y>posy) or (thepiece[1]=='k' and  thepiece[2]=='i'):
                                    #may need to solve pawn problem 
                                    dangerPieces.append(thepiece)
                                    if self.checkmateAlg==False:
                                        return False                        
                        elif colour=='white':
                            
                            if posx+x<8 and posx+x>-1 and posy+y<8 and posy+y>-1 and isenemysquare(board,colour,posx+x,posy+y)==True:
                                thepiece=getpiece(board,posx+x,posy+y)
                                
                                if (thepiece[1]=='p'and posy+y<posy) or (thepiece[1]=='k' and thepiece[2]=='i'):
                                    
                                    dangerPieces.append(thepiece)
                                    if self.checkmateAlg==False:
                                        return False 
        return True
                
     
     
class King(piece):
    def __init__(self,ptype,posy,posx,colour):
        self.ptype=ptype
        self.posy=posy
        self.posx=posx
        self.moveforw=0
        self.moveLorR=0
        self.movedyet=False
        self.colour=colour
        self.checkmateAlg=False
        self.checkmateMoves=False
        if self.colour=='black':
            self.image=pygame.image.load("blackking.png")
            chessDisplay.blit(self.image,((self.posx)*75,top))
        else:
            self.image=pygame.image.load('whiteking.png')        
            chessDisplay.blit(self.image,((self.posx)*75,bottom))
    def get_moves(self,xPerFrame,yPerFrame,turn):
        if str(self.colour)==turn:
                availableSquarex=[]
                availableSquares=[]
                posx=self.posx
                posy=self.posy
                for x in range(-1,2): 
                    for y in range(-1,2):
                        if posx+x>=0 and posx+x<=7 and posy+y>=0 and posy+y<=7:
                            if theboard.friendlysquare(posx+x,posy+y,turn)==False:
                                if self.endangersKing(turn,posx+x,posy+y)==False:#checks if the move endangers the king
                                    availableSquares.append(posy+y)
                                    availableSquarex.append(posx+x)                                





                if availableSquares== []:
                  SquareToMoveTo=None,None
                  
                  return SquareToMoveTo,xPerFrame,yPerFrame
                
                else:
                    if self.checkmateMoves==True:
                        SquareToMoveTo=availableSquares
                        return SquareToMoveTo,xPerFrame,yPerFrame
                    SquareToMoveTo,xPerFrame,yPerFrame=self.showSquares(availableSquares,availableSquarex,xPerFrame,yPerFrame)                    
                    return SquareToMoveTo,xPerFrame,yPerFrame
            
        else:
            
            SquareTo=None,None
            return SquareTo,xPerFrame,yPerFrame
    def checkmate(self,turn):
        #check moves of king
        
        dangerPiecesRecord=[]
        for items in dangerPieces:
            if type(items)=="""<class 'list'>""":
                minilist=[]
                for z in items:
                    minilist.append(z)
                dangerPiecesRecord.append(minilist)
            else:
                dangerPiecesRecord.append(items)      #creates a duplicate list 




        
        
        for u in range(len(dangerPieces)):
           
            dangerPieces.pop(0)
            
            #dangerPieces.remove(x)
        self.checkmateMoves=True
       
        temporary_board=theboard.currentBoard()
        moves=self.get_moves(self.posx,self.posy,turn)
        moves=moves[0]
        self.checkmateMoves=False
        if moves!=(None, None):
            print("King can move")
            return False
        
        theThreats=self.threats(turn,temporary_board,dangerPiecesRecord)
        if theThreats==False:
            return False
        return True
    def threats(self,turn,board,dangerPiecesRecord):
        
        for u in range(len(dangerPieces)):
            dangerPieces.pop(0)        
        for x in dangerPiecesRecord:
            

            print("dangerPieces record threats",dangerPiecesRecord)
            try:
                posx,posy=eval(x).coordinates()
            except TypeError:
                posx,posy=x[0],x[1]    
            print(posx,posy)
            if turn =='black':
                tempTurn='white'
            else:
                tempTurn='black'
                
            self.checkmateAlg=True
            print("x run",x)
            self.minicheck(board,tempTurn,posx,posy)
            self.checkmateAlg=False
            print(dangerPieces)
            # if self.minicheck(board,tempTurn,posx,posy)==True:
            #     #Only one piece can be endangering King. The others
            #     #just block the escape of the King, this is because if the King is ever in check it would have to move out of it.
            #     print(dangerPieces)
            #     for x in  dangerPieces:
            #         posx,posy=eval(x).coordinates()
                    
                    
            #     return False
            # print(dangerPieces)
       
        dangerPiecesRecord=[]
        for items in dangerPieces:
            if type(items)=="""<class 'list'>""":
                minilist=[]
                for z in items:
                    minilist.append(z)
                dangerPiecesRecord.append(minilist)
            else:
                dangerPiecesRecord.append(items)      #creates a duplicate list         
        
        for item in dangerPiecesRecord:
            print(item)
            eval(item).checkmateMoves=True
            moves=eval(item).get_moves(self.posx,self.posy,turn)
            print(moves)
            if  moves[0] !=(None,None):
                print("good")
                eval(item).checkmateMoves=False

                return False
            eval(item).checkmateMoves=False
        return True     

        
        
class Queen(piece):
    def __init__(self,ptype,posy,posx,colour):
        self.ptype=ptype
        self.posy=posy
        self.posx=posx
        self.moveforw=0
        self.moveLorR=0
        self.movedyet=False
        self.colour=colour
        self.checkmateAlg=False
        self.checkmateMoves=False
        if self.colour=='black':
            self.image=pygame.image.load("blackqueen.png")
            chessDisplay.blit(self.image,((self.posx)*75,top))
        else:
            self.image=pygame.image.load('whitequeen.png')
            chessDisplay.blit(self.image,((self.posx)*75,bottom))

    def get_moves(self,xPerFrame,yPerFrame,turn):

        if str(self.colour)==turn:
            availableSquarex=[]
            availableSquares=[]
            #diagonals
            for y in range(-1,2):
                if (y==0):
                    pass
                else:
                    for x in range(-1,2):
                        if (x==0):
                            pass
                        
                        else:
                            returnvaluex=[]
                            returnvaluey=[]
                            returnvaluex,returnvaluey=self.recursive1(turn,x,y,self.posx,self.posy,returnvaluex,returnvaluey)
                            print("x",returnvaluex,"y",returnvaluey)
                            for j in returnvaluex:
                                availableSquarex.append(j)
                            for k in returnvaluey:
                                 availableSquares.append(k)
            print(availableSquarex,availableSquares)
            #straights
            for x in range(-1,2):
                posx=self.posx
                posy=self.posy
                if x==0:
                    pass
                else:

                    
                        
                        
                        while posx+x<=7 and posx+x>=0 and posy<=7 and posy>=0 and theboard.emptySquare(posx+x,posy)==True:
                            posx+=x 
                            if self.endangersKing(turn,posx,posy)==False:#checks if the move endangers the king
                                availableSquarex.append(posx)
                                availableSquares.append(posy)
                            
                        if theboard.enemysquare(turn,posx+x,posy)==True and posy<=7 and posy>=0 and posx+x<=7 and posx+x>=0:
                            posx+=x 
                            if self.endangersKing(turn,posx,posy)==False:#checks if the move endangers the king
                                availableSquarex.append(posx)
                                availableSquares.append(posy)                             
                       
                        
            print("horizontal done")
            print(availableSquarex,availableSquares)

            for y in range(-1,2): 
                posx=self.posx
                posy=self.posy
                if y==0:
                    pass
                else:
                        
                        while posy+y<=7 and posy+y>=0 and posx<=7 and posx>=0 and theboard.emptySquare(posx,posy+y)==True :
                            posy+=y
                            if self.endangersKing(turn,posx,posy)==False:#checks if the move endangers the king
                                availableSquarex.append(posx)
                                availableSquares.append(posy)
                        if theboard.enemysquare(turn,posx,posy+y)==True and posy+y<=7 and posy+y>=0 and posx<=7 and posx>=0 :
                            posy+=y
                            if self.endangersKing(turn,posx,posy)==False:#checks if the move endangers the king
                                availableSquarex.append(posx)
                                availableSquares.append(posy)   









            if availableSquares== []:
                SquareToMoveTo=None,None
                return SquareToMoveTo,xPerFrame,yPerFrame

            else:
                if self.checkmateMoves==True:
                    SquareToMoveTo=availableSquares
                    return SquareToMoveTo,xPerFrame,yPerFrame
                SquareToMoveTo,xPerFrame,yPerFrame=self.showSquares(availableSquares,availableSquarex,xPerFrame,yPerFrame)                    
                return SquareToMoveTo,xPerFrame,yPerFrame



        else:
            
            SquareTo=None,None
            return SquareTo,xPerFrame,yPerFrame               
            
    def recursive1(self,colour,x,y,currentx,currenty,xvalues,yvalues):
        
        if ((currentx+x>7)or(currentx+x<0))or((currenty+y<0)or(currenty+y>7)):#wrong position at first. this error must be checked for first
            print("too wide")
            return xvalues,yvalues
        elif theboard.friendlysquare(currentx+x,currenty+y,colour)==True:
            print("friendly")
            return xvalues,yvalues
        elif theboard.enemysquare(colour,currentx+x,currenty+y)==True:
            if self.endangersKing(colour,currentx+x,currenty+y)==False:#checks if the move endangers the king
                xvalues.append(currentx+x)
                yvalues.append(currenty+y)
            return xvalues,yvalues            
        else:
            if self.endangersKing(colour,currentx+x,currenty+y)==False:#checks if the move endangers the king
                xvalues.append(currentx+x)
                yvalues.append(currenty+y)
            xvalues,yvalues=self.recursive1(colour,x,y,currentx+x,currenty+y,xvalues,yvalues) 
            return xvalues,yvalues

class Knight(piece):
    def __init__(self,ptype,posy,posx,colour):
        self.ptype=ptype
        self.posy=posy
        self.posx=posx
        self.moveforw=0
        self.moveLorR=0
        self.movedyet=False
        self.colour=colour
        self.checkmateAlg=False
        self.checkmateMoves=False
        if self.colour=='black':
            self.image=pygame.image.load("blackknight.png")
            chessDisplay.blit(self.image,((self.posx)*75,top))
        else:
            self.image=pygame.image.load('whiteknight.png')
            chessDisplay.blit(self.image,((self.posx)*75,bottom))

    def get_moves(self,xPerFrame,yPerFrame,turn):
        if str(self.colour)==turn:
                availableSquarex=[]
                availableSquares=[]
       
                long1=[2,-2]
                short=[1,-1]
                print("horizontal")
                for x in long1:
                    for y in short:
                        squarex=self.posx+x
                        square=self.posy+y 
                
                        if (theboard.friendlysquare(squarex,square,self.colour))==False and square>-1 : 
                            if self.endangersKing(turn,squarex,square)==False:#checks if the move endangers the king
                                availableSquares.append(square)
                                availableSquarex.append(squarex)
                print("vertical")
                for y in long1:
                    for x in short:
                        squarex=self.posx+x
                        square=self.posy+y 
                
                        if (theboard.friendlysquare(squarex,square,self.colour))==False and square>-1: 
                            if self.endangersKing(turn,squarex,square)==False:#checks if the move endangers the king
                                availableSquares.append(square)
                                availableSquarex.append(squarex)                       





                if availableSquares== []:
                  SquareToMoveTo=None,None
                  return SquareToMoveTo,xPerFrame,yPerFrame

                else:
                    if self.checkmateMoves==True:
                        SquareToMoveTo=availableSquares
                        return SquareToMoveTo,xPerFrame,yPerFrame
                    SquareToMoveTo,xPerFrame,yPerFrame=self.showSquares(availableSquares,availableSquarex,xPerFrame,yPerFrame)                    
                    return SquareToMoveTo,xPerFrame,yPerFrame
            
        else:
            
            SquareTo=None,None
            return SquareTo,xPerFrame,yPerFrame

class Rook(piece):
    def __init__(self,ptype,posy,posx,colour):
        self.ptype=ptype
        self.posy=posy
        self.posx=posx
        self.moveforw=0
        self.moveLorR=0
        self.movedyet=False
        self.colour=colour
        self.checkmateAlg=False
        self.checkmateMoves=False
        if self.colour=='black':
            self.image=pygame.image.load("blackrook.png")
            chessDisplay.blit(self.image,((self.posx)*75,top))
        else:
            self.image=pygame.image.load('whiterook.png')
            chessDisplay.blit(self.image,((self.posx)*75,bottom))
    def get_moves(self,xPerFrame,yPerFrame,turn):
        if str(self.colour)==turn:
            availableSquarex=[]
            availableSquares=[]        
            # originalx=self.posx
            # originaly=self.posy
            for x in range(-1,2):
                posx=self.posx
                posy=self.posy
                if x==0:
                    pass
                else:

                    
                        
                        
                        while posx+x<=7 and posx+x>=0 and posy<=7 and posy>=0 and theboard.emptySquare(posx+x,posy)==True:
                            posx+=x
                            if self.endangersKing(turn,posx,posy)==False:#checks if the move endangers the king 
                                availableSquarex.append(posx)
                                availableSquares.append(posy)
                            
                        if theboard.enemysquare(turn,posx+x,posy)==True and posy<=7 and posy>=0 and posx+x<=7 and posx+x>=0:
                            posx+=x 
                            if self.endangersKing(turn,posx,posy)==False:#checks if the move endangers the king
                                availableSquarex.append(posx)
                                availableSquares.append(posy)                            
                       
                        
            print("horizontal done")
            print(availableSquarex,availableSquares)

            for y in range(-1,2): 
                posx=self.posx
                posy=self.posy
                if y==0:
                    pass
                else:
                        
                        while posy+y<=7 and posy+y>=0 and posx<=7 and posx>=0 and theboard.emptySquare(posx,posy+y)==True :
                            posy+=y
                            if self.endangersKing(turn,posx,posy)==False:#checks if the move endangers the king
                                availableSquarex.append(posx)
                                availableSquares.append(posy)
                        if theboard.enemysquare(turn,posx,posy+y)==True and posy+y<=7 and posy+y>=0 and posx<=7 and posx>=0 :
                            posy+=y
                            if self.endangersKing(turn,posx,posy)==False:#checks if the move endangers the king
                                availableSquarex.append(posx)
                                availableSquares.append(posy)                             
                      
            print("vertical done")
            print(availableSquarex,availableSquares)
            if availableSquares== []:
                SquareToMoveTo=None,None
                return SquareToMoveTo,xPerFrame,yPerFrame

            else:
                if self.checkmateMoves==True:
                    SquareToMoveTo=availableSquares
                    return SquareToMoveTo,xPerFrame,yPerFrame                
                SquareToMoveTo,xPerFrame,yPerFrame=self.showSquares(availableSquares,availableSquarex,xPerFrame,yPerFrame)                    
                return SquareToMoveTo,xPerFrame,yPerFrame

        else:
            SquareTo=None,None
            return SquareTo,xPerFrame,yPerFrame

class Bishop(piece):
    def __init__(self,ptype,posy,posx,colour):
        self.ptype=ptype
        self.posy=posy
        self.posx=posx
        self.moveforw=0
        self.moveLorR=0
        self.movedyet=False
        self.colour=colour
        self.checkmateAlg=False
        self.checkmateMoves=False
        if self.colour=='black':
            self.image=pygame.image.load("blackbishop.png")
            chessDisplay.blit(self.image,((self.posx)*75,top))
        else:
            self.image=pygame.image.load('whitebishop.png')
            chessDisplay.blit(self.image,((self.posx)*75,bottom))
    def get_moves(self,xPerFrame,yPerFrame,turn):
        if str(self.colour)==turn:
            availableSquarex=[]
            availableSquares=[]
            for y in range(-1,2):
                if (y==0):
                    pass
                else:
                    for x in range(-1,2):
                        if (x==0):
                            pass
                        
                        else:
                            returnvaluex=[]
                            returnvaluey=[]
                            returnvaluex,returnvaluey=self.recursive1(turn,x,y,self.posx,self.posy,returnvaluex,returnvaluey)
                            print("x",returnvaluex,"y",returnvaluey)
                            for j in returnvaluex:
                                availableSquarex.append(j)
                            for k in returnvaluey:
                                 availableSquares.append(k)
            print(availableSquarex,availableSquares)
            if availableSquares== []:
                SquareToMoveTo=None,None
                return SquareToMoveTo,xPerFrame,yPerFrame

            else:
                if self.checkmateMoves==True:
                    SquareToMoveTo=availableSquares
                    return SquareToMoveTo,xPerFrame,yPerFrame
                SquareToMoveTo,xPerFrame,yPerFrame=self.showSquares(availableSquares,availableSquarex,xPerFrame,yPerFrame)                    
                return SquareToMoveTo,xPerFrame,yPerFrame



        else:
            SquareTo=None,None
            return SquareTo,xPerFrame,yPerFrame               
            
    def recursive1(self,colour,x,y,currentx,currenty,xvalues,yvalues):
        
        if ((currentx+x>7)or(currentx+x<0))or((currenty+y<0)or(currenty+y>7)):#wrong position at first. this error must be checked for first
            print("too wide")
            return xvalues,yvalues
        elif theboard.friendlysquare(currentx+x,currenty+y,colour)==True:
            print("friendly")
            return xvalues,yvalues
        elif theboard.enemysquare(colour,currentx+x,currenty+y)==True:
            if self.endangersKing(colour,currentx+x,currenty+y)==False:#checks if the move endangers the king
                xvalues.append(currentx+x)
                yvalues.append(currenty+y)
            return xvalues,yvalues            
        else:
            if self.endangersKing(colour,currentx+x,currenty+y)==False:#checks if the move endangers the king
                xvalues.append(currentx+x)
                yvalues.append(currenty+y)
            xvalues,yvalues=self.recursive1(colour,x,y,currentx+x,currenty+y,xvalues,yvalues) 
            return xvalues,yvalues

class Pawn(piece):
    def __init__(self,ptype,posy,posx,colour):
        self.ptype=ptype
        self.posy=posy
        self.posx=posx
        self.moveforw=0
        self.moveLorR=0
        self.movedyet=False
        self.colour=colour
        self.checkmateAlg=False
        self.checkmateMoves=False
        if self.colour=='black':
            self.image=pygame.image.load("blackpawn.png")
            chessDisplay.blit(self.image,((self.posx)*75,top2))
        else:
            self.image=pygame.image.load('whitepawn.png')
            chessDisplay.blit(self.image,((self.posx)*75,bottom2))


    def get_moves(self,xPerFrame,yPerFrame,turn):#calculates available moves
         print(turn)
         print(self.colour)
         if str(self.colour)==turn:
                

          
                availableSquares=[]
                availableSquarex=[]
                temporaryy=[]
                temporaryx=[]
                closestEmpty=True
                both_empty=True
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
                    if  square>-1 and square<8:
                        if (theboard.emptySquare(self.posx,square))==True:
                            if (theboard.friendlysquare( self.posx,square,self.colour))==False:
                                if self.endangersKing(turn,self.posx,square)==False:#checks if the move endangers the king
                                    temporaryy.append(square)
                                    temporaryx.append(self.posx)
                            else:
                                if x==1:
                                    closestEmpty=False
                                    # both_empty=False
                        else:
                            if x==1:
                                closestEmpty=False
                    else:
                            print("not empty")
                            # both_empty=False
                            closestEmpty=False
                print(temporaryx,temporaryy)
                if closestEmpty==True:
                    for y in temporaryy:
                        availableSquares.append(y)
                    for x in temporaryx:
                        availableSquarex.append(x)

                # # if both_empty==True:
                # #     print("both empty")
                # #     for y in temporaryy:
                # #         availableSquares.append(y)
                # #     for x in temporaryx:
                # #         availableSquarex.append(x)
                            
                            
                print("pawn available",availableSquares)
                    

              
                   
                for x in range(-1,2):
                    if x==0:
                        pass
                    else:
                        if self.colour=='white':
                            
                            squarey=self.posy-1
                            squarex=self.posx+x    
                            if (theboard.enemysquare("white",squarex,squarey))==True and squarex>-1 and square>-1:
                                    if self.endangersKing(turn,squarex,squarey)==False:#checks if the move endangers the king
                                        availableSquares.append(squarey)
                                        availableSquarex.append(squarex)
                            
                            
                        else:
                            squarey=self.posy+1
                            squarex=self.posx+x

                            if (theboard.enemysquare("black",squarex,squarey))==True and squarex>-1 and square>-1:
                                if self.endangersKing(turn,squarex,squarey)==False:#checks if the move endangers the king
                                    availableSquares.append(squarey)
                                    availableSquarex.append(squarex)
                
                if availableSquares== []:
                    SquareToMoveTo=None,None
                    return SquareToMoveTo,xPerFrame,yPerFrame

                else:
                    if self.checkmateMoves==True:
                        SquareToMoveTo=availableSquares
                        return SquareToMoveTo,xPerFrame,yPerFrame
                    SquareToMoveTo,xPerFrame,yPerFrame=self.showSquares(availableSquares,availableSquarex,xPerFrame,yPerFrame)                    
                    return SquareToMoveTo,xPerFrame,yPerFrame
         else:
            SquareToMoveTo=None,None
            return SquareToMoveTo,xPerFrame,yPerFrame 

def oldcode():      
    
    ##            else:#the pawn moves 1 most of the time
    ##                      
    ##                availableSquares=[]
    ##                availableSquarex=[]
    ##                for x in range(1,2):
    ##                    if self.colour=='white':
    ##                        
    ##                        square=self.posy-x
    
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
    pass
         
 









def getmouse():
    mouse=pygame.mouse.get_pos()
    clicked=pygame.mouse.get_pressed()
    
    mousex,mousey=None,None
    currentPiece=''
    if clicked[0]==1:#This gets the mouse position
        
        while clicked[0] == 1:
            random=pygame.event.get()
            clicked=pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                  
                    pygame.quit()    
                    quit()
            
        
        mousex=mouse[0]//75 #These 2 statements sort of act as a hashing algorithm reducing the board to 8*8 as opposed to 600*600
        mousey=mouse[1]//75

        currentPiece=pieceInPos(mousex,mousey)
        
        
        
    return (mousex,mousey,currentPiece) 

def pieceInPos(mousex,mousey):#This just gets the name of piece in the position the user clicked from the board array.
    piece=theboard.getpiece(mousex,mousey)
    return piece

def move(moving1,currentmovingpiece,SquareTo,xPerFrame,yPerFrame,turn):
 
    
    mousex,mousey,currentPiece=getmouse()


    
    

    if mousex!=None and mousey!=None:
        try:
                print()
                print()
                print()
                print("NEW PIECE")
                print(mousex,mousey,currentPiece)
                #The eval statement below was to ensure it ran as python code opposed to as a string.
                SquareTo,xPerFrame,yPerFrame=eval(currentPiece).get_moves(xPerFrame,yPerFrame,turn)#There is a different method 
                #for each piece that runs here to calculate available moves.
                print(SquareTo,xPerFrame,yPerFrame)
                if SquareTo != (None,None):#If there are available moves then
                    
                    currentmovingpiece=currentPiece
                    
                    moving1=eval(currentmovingpiece).moveit(SquareTo,xPerFrame,yPerFrame,turn,currentmovingpiece)#This moves the piece to
                    #the square the user clicked on. 
                    if turn =='black':
                        turn='white'
                    else:
                        turn='black'
                    boardState=open("boardstate.txt","a+")
                    boardState.write("\n"+str(theboard.currentBoard())+turn)
                    boardState.close()
                    check(turn)

                
                
                
                
        except SyntaxError:
                print(mousex,mousey,"Square empty")
                print()





    try:

        return moving1,currentmovingpiece,SquareTo,xPerFrame,yPerFrame,turn
    except:
        print("not returning")
        return None
     
def update(turn):

    chessDisplay.blit(chessBoard,(0,0))
    #It reads from different ends of the allPieces list 
    #so when the pieces of the player whose turn it is take other pieces they glide
    #over them opposed to under them. 
    if turn=='black':
        g=0
        for x in range(len(allPieces)):
            g=g-1
            thepiece=allPieces[g]
            eval(thepiece).update()
    else:

        for x in allPieces: 
            eval(x).update()
            
##    bpawn1.update()
##    bpawn2.update()
##    bpawn3.update()
##    bpawn4.update()
##    bpawn5.update()
##    bpawn6.update()
##    bpawn7.update()
##    bpawn8.update()
##    brook1.update()
##    bknight1.update()
##    bbishop1.update()
##    bqueen.update()
##    bking.update()
##    bbishop2.update()
##    bknight2.update()
##    brook2.update()
##
##    wpawn1.update()
##    wpawn2.update()
##    wpawn3.update()
##    wpawn4.update()
##    wpawn5.update()
##    wpawn6.update()
##    wpawn7.update()
##    wpawn8.update()
##    wrook1.update()
##    wknight1.update()
##    wbishop1.update()
##    wking.update()
##    wqueen.update()
##    wbishop2.update()
##    wknight2.update()
##    wrook2.update()  
def check(turn):
    print("Check algorithm")
    print(dangerPieces)
    tempY=0
    board=theboard.currentBoard()
    
    for y in board:
        try:
            if turn=='white':
                thex=y.index("wking")
                they=tempY
                print(thex)
            else:
                thex=y.index("bking")
                they=tempY
                print(thex)
            tempY+=1
        except ValueError:
            tempY+=1
    king_in_check=theboard.getpiece(thex,they)
    print(king_in_check)

    if turn=='white':
        if wking.minicheck(board,turn,thex,they)==True:
            print("check white")
            print(dangerPieces)
            if wking.checkmate(turn)==True:
                print("CHECKMATE")
                # pygame.quit()    
                # quit()   
    else:
        if bking.minicheck(board,turn,thex,they)==True:
            print("check black")
            if bking.checkmate(turn)==True:
                print("CHECKMATE")
                # pygame.quit()    
                # quit()
    
    print("chk alg comp")
    
def start(turn): #this function is the main game loop and repeats over and over again.
    gameExit=False 
    returned,current,squ,xPerFrame,yPerFrame=None,None,None,None,None
    boardState=open("boardstate.txt","w")
    boardState.write("boardstate")
    boardState.write("\n"+str(theboard.currentBoard())+turn)
    boardState.close()
    while not gameExit:
        for x in range(len(dangerPieces)):
            dangerPieces.pop(0)

        for event in pygame.event.get():
            if event.type==pygame.QUIT: #this allows the player to quit the game
                pygame.quit()    
                quit()
                
            

            returned,current,squ,xPerFrame,yPerFrame,turn=move(returned,current,squ,xPerFrame,yPerFrame,turn)
            
            update(turn)#this effectively paints all the pieces onto a staging board so any changes can display at once. 
            pygame.display.update()#This displays all change to the actual display
            clock.tick(30)
            
        
        
        
if __name__=="__main__":
    #this creates the game and classes. 
    allPieces=['bpawn1', 'bpawn2', 'bpawn3', 'bpawn4', 'bpawn5', 'bpawn6', 'bpawn7', 'bpawn8', 'brook1',
               'bknight1', 'bbishop1', 'bqueen', 'bking', 'bbishop2', 'bknight2', 'brook2', 'wpawn1',
               'wpawn2', 'wpawn3', 'wpawn4', 'wpawn5', 'wpawn6', 'wpawn7', 'wpawn8', 'wrook1', 'wknight1',
               'wbishop1', 'wking', 'wqueen', 'wbishop2', 'wknight2', 'wrook2']
    theboard=board1()
    chessBoard=pygame.image.load('board4.png')
    chessDisplay.blit(chessBoard,(0,0))
    theboard.display()
    print()
    print()
    dangerPieces=[]
    # Pygame pixel coordinates start in top left
    bpawn1=Pawn("pawn",1,0,"black")
    
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
    wking=King("king",7,4,"white")
    wqueen=Queen("queen",7,3,"white")
    wbishop2=Bishop("bishop",7,5,"white")
    wknight2=Knight("knight",7,6,"white")
    wrook2=Rook("rook",7,7,"white")
    turn='white'
    
    
    start(turn)
##    pygame.quit() 



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
