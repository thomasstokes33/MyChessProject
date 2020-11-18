##The general game loop on line 1422 was from a part of series that taught me the basics of pygame. https://www.youtube.com/watch?v=ujOTNg17LjI&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO
#technical

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



chessDisplay=pygame.display.set_mode((displayWidth,displayHeight))#sets up display
pygame.display.set_caption('Chess')#sets caption of window
icon=pygame.image.load("whitepawn.png")
pygame.display.set_icon(icon)
widthOfSquare=75 #I use this(the width and height of a square on the board) to convert coordinates into more workable numbers. Effectively coding or mapping values to 
#new integers that are easier to work with and interpret.

bottom=widthOfSquare*7
bottom2=widthOfSquare*6
top=0
top2=widthOfSquare
clock=pygame.time.Clock()
def getpiece(board,mousex,mousey):
        return board[mousey][mousex]

def isemptySquare(board,x,y):

        if board[y][x] == '':
           
           return True
        else:
           
           return False

def isenemysquare(board,colour,x,y):
        
        try:
            character=board[y][x]
            if colour=="black":
                 
                if character[0]=='w':
                       return True  
            else:
                if character[0]=='b':
                    return True
        except IndexError:
           
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
        for items in self.board:
            for item in items:
                returnboard[count].append(item)
            count+=1
        return returnboard

    def getpiece(self,mousex,mousey):#this fetches the piece specified by paramters
        return self.board[mousey][mousex]
        
    def emptySquare(self,x,y):#this checks if the square specified is empty. 
   
        if self.board[y][x] == '':
 

           return True
        else:

           return False
    def friendlysquare(self,x,y,colour):#this checks if the square contains a piece belonging to the current players.
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
            return False
        
    def move(self,currentx,currenty,newx,newy):#this updates the array after a piece has moved. 
        record=self.board[currenty][currentx]
        self.board[currenty][currentx]=''
        self.board[newy][newx]=record
        self.display()
              
              
            
            
        




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
            pygame.event.get() ##In coding the pygame window brought up an error and this(https://stackoverflow.com/questions/20165492/pygame-window-not-responding-after-a-few-seconds) website told me
            #this line was needed. It just makes sure it is doing something and the os is receiving commands. 
            clicked1=pygame.mouse.get_pressed()
            mouse1=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()    
                    quit()
        
        if mouse1[1]>=262 and mouse1[1]<=337:
            if mouse1[0]>=150 and mouse1[0]<=225:#queen
                
                number=piece[5]
                upgradePawn1=(self.colour[0]+'queen'+number)
                upgradeType='queen'
                globals()[upgradePawn1]=Queen(upgradeType.lower(),self.posy,self.posx,self.colour)## I tried to eval the whole thing
                #which executes it as python code, but this didn't work. I had to do some research and learnt about how to create variables from 
                #strings:https://www.codespeedy.com/convert-string-into-variable-name-in-python/#:~:text=Declaring%20Variable%20Name%20Dynamically&text=Now%2C%20by%20using%20globals(),in%20the%20global%20%2F%20local%20namespace.
            if mouse1[0]>=225 and mouse1[0]<=300:#knight
                
                number=piece[5]
                upgradePawn1=(self.colour[0]+'knight'+number)
                upgradeType='knight'
                globals()[upgradePawn1]=Knight(upgradeType.lower(),self.posy,self.posx,self.colour)
            if mouse1[0]>=300 and mouse1[0]<=375:#rook
                
                number=piece[5]
                upgradePawn1=(self.colour[0]+'rook'+number)
                upgradeType='rook'
                globals()[upgradePawn1]=Rook(upgradeType.lower(),self.posy,self.posx,self.colour)
            if mouse1[0]>=375 and mouse1[0]<=450:#bishop
               
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
        for item in availableSquarey:
                  pygame.draw.rect(chessDisplay,blue,((availableSquarex[(counter)])*75,(item*75),75,75),1)
                  #draws rectangle on chessdisplay, blue outline, (left side x coordinate, top side y coordinate, width,height), thickness
                  counter+=1
                  pygame.display.update()
        
        
        clicked1=pygame.mouse.get_pressed() #This returns a list of left mouse button,middle mouse button and left mouse button in that order.
        
        while clicked1[0]==0: #This runs until the user clicks on one of the squares. 
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
        for item in availableSquarey:
            if (mouse1[0]>(availableSquarex[counter]*75) and mouse1[0]<((availableSquarex[counter]*75)+75))and(mouse1[1]>item*75 and mouse1[1]<(item*75)+75):
                SquareToMoveTo=availableSquarex[counter],item 
                xPerFrame,yPerFrame=self.distancePerFrame(SquareToMoveTo[0],SquareToMoveTo[1]) #This allows the function to return 
                #the distance the piece will move per frame as well as 
                
            counter+=1
        #If the user doesn't click in the blue boxes, None is returned for all fields.
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
            
            
        
        self.posx=squarex #sets posx and posy to move-to-coordinates.
        self.posy=squarey
        takenPiece=theboard.getpiece(self.posx,self.posy) #this records the piece that will be taken, if any.
        
        theboard.move(lastposx,lastposy,squarex,squarey)#this moves the piece in the board array(an attribute of the board class)
        self.movedyet=True 
        if takenPiece!='':
            allPieces.remove(takenPiece) #if a piece was taken it is removed from the update list.
        if self.ptype=='pawn': #if pawn has reached backrow it is upgraded.
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
        hor=abs(currentx-movetox)#calculates distance without sign. Abs function makes it positive.
        vert=abs(currenty-movetoy)
        print("hor: ",hor,"vert: ",vert)  #horizontal and vertical distance

        distance=math.sqrt((abs(hor))**2+(abs(vert))**2) #Uses pythagoras to find the distance between 2 squares.
        print("d:",distance)
        speed=210 #unitspersecond. This is a number I choose and tweaked till the pieces moved at a sensible speed.
        time=distance/speed
        print("t: "+str(time)) #time I want it to take to get the piece from one square to another

        framestaken=round((time/1)*30) #The 30 is frames per second, which I set in the pygame clock on line 31. This calculates the frames 
        # it will take to travel the given time. The round is here because each frame happens it; there aren't half frames. 
        print("framestaken",framestaken)
        xPerFrame=(hor/framestaken)#The distance is split up into x and y travelled per frame.
        yPerFrame=(vert/framestaken) 
        print("x move",xPerFrame,"y move",yPerFrame)
        if movetox<currentx:#if the x or y coordinates of the new square are less than the current then the corresponding distance per frame
            #for that component is switched to a negative. 
            xPerFrame=-xPerFrame

        if movetoy<currenty:
            yPerFrame=-yPerFrame
                    
        return xPerFrame,yPerFrame

    def endangersKing(self,colour,movetox,movetoy):
     
        board_temp= theboard.currentBoard()##This calls a method that creates a duplicate list. I learnt during the project and later
        #in school about immutable and mutable objects. Lists are mutable and can be changed after creation if referenced. 
        #This brought up problems when the temporary board was changed which changed the actual board. So this function creates a duplicate
        #that is different. This is like referencing a simple variable.
        record=board_temp[self.posy][self.posx] #records what is in the current square
        board_temp[self.posy][self.posx]=''
        board_temp[movetoy][movetox]=record#and moves it to a new square. 
        tempY=0
        
        for y in board_temp:#Each list within the board list represents a column on the board.
            try:
                if colour=='white':
                    thex=y.index("wking") #This loop finds the coordinates of the king. 
                    they=tempY
                   
                else:
                    thex=y.index("bking")
                    they=tempY
         
                tempY+=1
            except ValueError:
                
                tempY+=1
       
        if ( self.minicheck(board_temp,colour,thex,they) ==False):
            #mini check finds if
            #new move results in the king in danger. 
            print("no minicheck")
            
            return False
    

    def minicheck(self,board,colour,x,y):
        #diagonal
       
        diagonal=self.diagonalsclear(board,colour,x,y)


        if (diagonal==False):  
            print("diagonals are danger")
            return True
       
        #straights
        straights=self.straightsclear(board,colour,x,y)
        
        if straights==False:
            print("straights are danger")
            return True
       

        
        #adjacent for king and pawns
        adjacent=self.adjacentclear(board,colour,x,y)
        if (adjacent==False):
            print("adjacents aren't clear")
            return True          
       
        #knight
        knight=self.knightclear(board,colour,x,y)
        if (knight==False):
            print("knight are danger")
            return True
       
        return False
       
    def recursive2(self,board,colour,x,y,currentx,currenty,tempDiagonalDangerPieces):##This is recursive 2 because when this slightly different method was called the moving function was called
        #which had a different set of parameters.
       
        if ((currentx+x>7)or(currentx+x<0))or((currenty+y<0)or(currenty+y>7)):##I had a problem where the if loops here were the wrong way
            #around which was a problem because the function below has less error checking. Therefore when the values of current x and
            #y exceeded the size of the board there was an error.
            return True
        elif isenemysquare(board,colour,currentx+x,currenty+y)==True:
            thepiece=getpiece(board,currentx+x,currenty+y)
            try:
                if thepiece[1]=='q' or thepiece[1]=='b':#the queen and bishop can move diagonally and these pieces' 2nd character is either b or q.
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
#This function basically scans out from the king stopping if the next square is filled or the edge of the board is reached. If the piece is an enemy piece then there is a threat along the diagonals.

        else:
           
            tempDiagonalDangerPieces.append([currentx+x,currenty+y])
            value=self.recursive2(board,colour,x,y,currentx+x,currenty+y,tempDiagonalDangerPieces)#If none of the conditions are true the recursive algorithm continues. Otherwise it returns true or false and continues escaping
            #until all recursions have returned. 
            if value==True:
                return True
            else:##I had an error where this value was not true because it was assigned a string which caused a logical error
                #as the the wrong value was returned but the code kept running.
                return False     

        
    


    def diagonalsclear(self,board,colour,posx,posy) :
        originalx=posx
        originaly=posy
        for y in range(-1,2): #These for loops provide the increment in x and y for the scanning loop. 
            posx=originalx
            posy=originaly
            if (y==0): ##I had an error where this was x opposed to y. 
                pass
            else:
                for x in range(-1,2):
                    if (x==0):
                        pass
                    
                    else:
                        tempDiagonalDangerPieces=[]
                     
                        returnvalue=self.recursive2(board,colour,x,y,posx,posy,tempDiagonalDangerPieces)
                        if self.checkmateAlg==False: #This line ensures the loop runs all diagonals. This is used in checkmate, when 
                            #scanning for all threat along all diagonals.
                            if returnvalue==False:
                                return False
                        
            
        return True            
                            
                            
                    

    def straightsclear( self,board,colour,posx,posy):
        horizontalclear=True
        verticalclear= True
        originalx=posx
        originaly=posy
        for x in range(-1,2): #There are two separate loops for horizontal and vertical
            posx=originalx
            posy=originaly
            if x==0:
                pass
            else:

                if horizontalclear==True:#This variable is here to increase the speed of the loop by running less commands.
                    # It also ensures no new pieces are added to the danger pieces list.
                    tempDangerPieces=[]
                    while posx+x<=7 and posx+x>=0 and posy<=7 and posy>=0 and isemptySquare(board,posx+x,posy)==True and horizontalclear==True:
                        #I thought I'd try a different approach to a similar problem and used a while loop instead of a recursive algorithm(recursive2).
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
            if y==0:#was x ==0 which caused errors.
                
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
        #The knight can move two in a direction then one in the other plane(eg two vertically and one horizontally)
        long1=[2,-2]#Long is a type of integer with infinite length and so the variable name had to be changed.
        short=[1,-1]
        for x in long1:#This for loop checks two squares along the x axis usinf the list long1.
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
    def adjacentclear(self,board,colour,posx,posy):#This method was added because I originally tried using the diagonalsclear function, but 
        #that meant that if any king or pawn was on the diagonals the program claimed there was a diagonal threat to the king, which
        #there wasn't due to the movement constraints of the pieces involved.
        for x in range(-1,2):
                if posx+x <8 and posx+x >-1 and posy<8 and posy>-1:
                    if isenemysquare(board,colour,posx+x,posy )==True:
                        thepiece=getpiece(board,posx+x,posy)
                        
                        if thepiece[1]=='k' and thepiece[2]=='i':#I needed two characters because the knight also starts with a k.
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
                                     
                                    dangerPieces.append(thepiece)
                                    if self.checkmateAlg==False:
                                        return False                        
                        elif colour=='white':#This is because the pawns can only take diagonals infront of them based on which direction they normally move

                            
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





                if availableSquares== []:#If there are no available moves the square to move to is None,None
                  #and the show squares stage(where the available moves are highlighted) is skipped.
                  SquareToMoveTo=None,None
                  
                  return SquareToMoveTo,xPerFrame,yPerFrame
                
                else:
                    if self.checkmateMoves==True:#If it is the checkmate algorithm the show squares algorithm isn't needed because
                        #it will bring up the blue boxes.
                        SquareToMoveTo=availableSquares
                        return SquareToMoveTo,xPerFrame,yPerFrame
                    SquareToMoveTo,xPerFrame,yPerFrame=self.showSquares(availableSquares,availableSquarex,xPerFrame,yPerFrame) #The available moves are highlighted                   
                    #the square the piece will move to, if any, is returned along with xPerFrame and yPerFrame
                    #which will be passed to the moveit function.
                    return SquareToMoveTo,xPerFrame,yPerFrame
            
        else:
            
            SquareTo=None,None
            return SquareTo,xPerFrame,yPerFrame
    def checkmate(self,turn):
        #It first checks the available moves of the king. 
        
        dangerPiecesRecord=[]
        for items in dangerPieces: #creates a duplicate list 
            if type(items)=="""<class 'list'>""":
                minilist=[]
                for z in items:
                    minilist.append(z)
                dangerPiecesRecord.append(minilist)
            else:
                dangerPiecesRecord.append(items)      




        
        
        for u in range(len(dangerPieces)):
           
            dangerPieces.pop(0)
            
           
        self.checkmateMoves=True#This means that get_moves returns different things depending on whether it is empty.
       
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
        
        #danger piece record is a list of pieces currently threatening king and spaces that can be blocked
        for item in range(len(dangerPieces)):
            dangerPieces.pop(0)        
        for x in dangerPiecesRecord: 
            

            
            try:
                posx,posy=eval(x).coordinates() #This line and the exception/catch are used to get the coordinates of the pieces or squares that
                #can be used to block threats.
                #I got the name of the actual threat because it made the error checking easier.
            except TypeError:
                posx,posy=x[0],x[1]    
            
            if turn =='black':
                tempTurn='white'
            else:
                tempTurn='black'
                
            self.checkmateAlg=True#This ensures only the pieces are added that can save the king opposed to the empty squares.
            self.minicheck(board,tempTurn,posx,posy)#This adds to the now empty dangerPieces any pieces that can block or take pieces threatening the king.
            self.checkmateAlg=False
           

        
        dangerPiecesRecord=[]
        for items in dangerPieces:
            if type(items)=="""<class 'list'>""":
                minilist=[]
                for z in items:
                    minilist.append(z)
                dangerPiecesRecord.append(minilist)
            else:
                dangerPiecesRecord.append(items)      #this for loop creates a duplicate list          
        
        for item in dangerPiecesRecord: #The duplicate list is used so if any of the minicheck sub algorithms run it doesn't change the list.
            
            eval(item).checkmateMoves=True
            moves=eval(item).get_moves(self.posx,self.posy,turn)
            
            if  moves[0] !=(None,None):  #If none of the saviour pieces(pieces that might be able to save the king) can move
                #it means that there is another piece threatening king so it is checkmate if no pieces can save the king.
                
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
        #The queen can move along the straights and diagonals.
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
                            
                            for j in returnvaluex:
                                availableSquarex.append(j)
                            for k in returnvaluey:
                                 availableSquares.append(k)
            
            #straights
            for x in range(-1,2):
                posx=self.posx
                posy=self.posy
                if x==0:
                    pass
                else:

                    
                        
                        
                        while posx+x<=7 and posx+x>=0 and posy<=7 and posy>=0 and theboard.emptySquare(posx+x,posy)==True:#Checks next square and if empty it adds the new square to available moves.
                            posx+=x 
                            if self.endangersKing(turn,posx,posy)==False:#checks if the move endangers the king
                                availableSquarex.append(posx)
                                availableSquares.append(posy)
                            
                        if theboard.enemysquare(turn,posx+x,posy)==True and posy<=7 and posy>=0 and posx+x<=7 and posx+x>=0:#If the above while loop has stopped the next piece might be an enemy piece and providing the move doesn't endanger the king
                                #Then the square can be added to available squares(the list of squares the currently selected piece can move to).
                            posx+=x 
                            if self.endangersKing(turn,posx,posy)==False:
                                availableSquarex.append(posx)
                                availableSquares.append(posy)                             
                       
                        
         
        

            for y in range(-1,2): #This is the same as above but for the verticals
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
                            if self.endangersKing(turn,posx,posy)==False:
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
        
        if ((currentx+x>7)or(currentx+x<0))or((currenty+y<0)or(currenty+y>7)):
            
            return xvalues,yvalues
        elif theboard.friendlysquare(currentx+x,currenty+y,colour)==True:
           
            return xvalues,yvalues
        elif theboard.enemysquare(colour,currentx+x,currenty+y)==True:
            if self.endangersKing(colour,currentx+x,currenty+y)==False:#if it is an enemy then it is added to the list.
                xvalues.append(currentx+x)
                yvalues.append(currenty+y)
            return xvalues,yvalues            
        else:
            if self.endangersKing(colour,currentx+x,currenty+y)==False: #If the square is within the limits of the board and is empty then it is added to the list of available squares.
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
                short=[1,-1] #This works very similarly to the knights clear method.
              
                for x in long1:
                    for y in short:
                        squarex=self.posx+x
                        square=self.posy+y 
                
                        if (theboard.friendlysquare(squarex,square,self.colour))==False and square>-1 : 
                            if self.endangersKing(turn,squarex,square)==False:#checks if the move endangers the king
                                availableSquares.append(square)
                                availableSquarex.append(squarex)
             
                for y in long1:
                    for x in short:
                        squarex=self.posx+x
                        square=self.posy+y 
                
                        if (theboard.friendlysquare(squarex,square,self.colour))==False and square>-1: 
                            if self.endangersKing(turn,squarex,square)==False:
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

class Rook(piece):#Works like the straights part of the queen.
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
           
            for x in range(-1,2):
                posx=self.posx
                posy=self.posy
                if x==0:
                    pass
                else:

                    
                        
                        
                        while posx+x<=7 and posx+x>=0 and posy<=7 and posy>=0 and theboard.emptySquare(posx+x,posy)==True:
                            posx+=x
                            if self.endangersKing(turn,posx,posy)==False: 
                                availableSquarex.append(posx)
                                availableSquares.append(posy)
                            
                        if theboard.enemysquare(turn,posx+x,posy)==True and posy<=7 and posy>=0 and posx+x<=7 and posx+x>=0:
                            posx+=x 
                            if self.endangersKing(turn,posx,posy)==False:
                                availableSquarex.append(posx)
                                availableSquares.append(posy)                            
                       
                        
           

            for y in range(-1,2): 
                posx=self.posx
                posy=self.posy
                if y==0:
                    pass
                else:
                        
                        while posy+y<=7 and posy+y>=0 and posx<=7 and posx>=0 and theboard.emptySquare(posx,posy+y)==True :
                            posy+=y
                            if self.endangersKing(turn,posx,posy)==False:
                                availableSquarex.append(posx)
                                availableSquares.append(posy)
                        if theboard.enemysquare(turn,posx,posy+y)==True and posy+y<=7 and posy+y>=0 and posx<=7 and posx>=0 :
                            posy+=y
                            if self.endangersKing(turn,posx,posy)==False:
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

class Bishop(piece):#Works like the diagonals part of the queen.
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
                          
                            for j in returnvaluex:
                                availableSquarex.append(j)
                            for k in returnvaluey:
                                 availableSquares.append(k)
         
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
        
        if ((currentx+x>7)or(currentx+x<0))or((currenty+y<0)or(currenty+y>7)):
         
            return xvalues,yvalues
        elif theboard.friendlysquare(currentx+x,currenty+y,colour)==True:
          
            return xvalues,yvalues
        elif theboard.enemysquare(colour,currentx+x,currenty+y)==True:
            if self.endangersKing(colour,currentx+x,currenty+y)==False:
                xvalues.append(currentx+x)
                yvalues.append(currenty+y)
            return xvalues,yvalues            
        else:
            if self.endangersKing(colour,currentx+x,currenty+y)==False:
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


    def get_moves(self,xPerFrame,yPerFrame,turn):#pawn can move forward two on first turn and then one. It can take pieces diagonally
        #in front of it
         if str(self.colour)==turn: #This checks that the clicked piece belongs to the player whose turn it is.
          
                availableSquares=[]
                availableSquarex=[]
                temporaryy=[]
                temporaryx=[]
                closestEmpty=True #If the square closest to the pawn is filled then the pawn can't move. 
               
                for x in range(1,3):
                    
                    if self.colour=='white': #If the pieces are white they move towards the x axis(remember that (0,0) is in top left corner)

                        if self.movedyet==False:
                            
                            square=self.posy-x
                        else:
                            square=self.posy-1
                         
                    else:#If they are black they move away from the x axis(hence add 1).
                        if self.movedyet==False:
                            
                            square=self.posy+x
                        else:
                            square=self.posy+1
                    if  square>-1 and square<8: #If within boundaries
                        if (theboard.emptySquare(self.posx,square))==True: #If square is empty 
                            if (theboard.friendlysquare( self.posx,square,self.colour))==False:
                                if self.endangersKing(turn,self.posx,square)==False:#checks if the move endangers the king
                                    temporaryy.append(square) 
                                    temporaryx.append(self.posx)
                            else:
                                if x==1:
                                    closestEmpty=False
                                    
                        else:
                            if x==1:
                                closestEmpty=False
                    else:
                           
                            closestEmpty=False
                
                if closestEmpty==True: ##There was an error where the pawn could move 2 if blocked so this variable was added which 
                    #only adds the moves if the closest square is empty.
                    for y in temporaryy:
                        availableSquares.append(y)
                    for x in temporaryx:
                        availableSquarex.append(x)

                            
                            
            
                    

              
                   
                for x in range(-1,2):#This checks if the piece can take diagonals. 
                    if x!=0:
                        if self.colour=='white':
                            
                            squarey=self.posy-1 #it's only 1 "up"
                            squarex=self.posx+x   
                            if (theboard.enemysquare("white",squarex,squarey))==True and squarex>-1 and square>-1:
                                    if self.endangersKing(turn,squarex,squarey)==False:
                                        availableSquares.append(squarey)
                                        availableSquarex.append(squarex)
                            
                            
                        else:
                            squarey=self.posy+1
                            squarex=self.posx+x

                            if (theboard.enemysquare("black",squarex,squarey))==True and squarex>-1 and square>-1:
                                if self.endangersKing(turn,squarex,squarey)==False:
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

def gameover():
    restart=pygame.image.load('reloadimg.png')
    chessDisplay.blit(restart,(260,260))
    pygame.display.update()  
    clicked=pygame.mouse.get_pressed() 
    while clicked[0]==0:
        clicked=pygame.mouse.get_pressed()
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()    
                    quit()
    gameExit=True
    return gameExit
     
         

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
    gameExit=False#Once in this loop the game isn't exiting. This is also used to stop and error, where this value
    #isn't defined
    
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
                if SquareTo != (None,None):#If there are available moves then:
                    
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
                    gameExit=check(turn)

        except SyntaxError:
                print(mousex,mousey,"Square empty")
                print()
    try:

        return moving1,currentmovingpiece,SquareTo,xPerFrame,yPerFrame,turn,gameExit
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
            

def check(turn):
    print("Check algorithm")
    print(dangerPieces)
    tempY=0
    board=theboard.currentBoard()
    
    for y in board:  #This finds the location of the king
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
    gameExit=False
    if turn=='white':
        if wking.minicheck(board,turn,thex,they)==True:
            print("check white")
            print(dangerPieces)
            if wking.checkmate(turn)==True:
                print("CHECKMATE")
                gameExit=gameover()
    else:
        if bking.minicheck(board,turn,thex,they)==True:
            print("check black")
            if bking.checkmate(turn)==True:
                print("CHECKMATE")
                gameExit=gameover()
               
    
    print("chk alg comp")
    return gameExit
    
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
                
            

            returned,current,squ,xPerFrame,yPerFrame,turn,gameExit=move(returned,current,squ,xPerFrame,yPerFrame,turn)
            
            update(turn)#this effectively paints all the pieces onto a staging board so any changes can display at once. 
            pygame.display.update()#This displays all change to the actual display
            clock.tick(30)
            
        
        
         
if __name__=="__main__":
    while True: 
        #this creates the game and classes. 
        movedList=open("movedList.txt","w")
        movedList.write("movedlist")
        movedList.close()
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


