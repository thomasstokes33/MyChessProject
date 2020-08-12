import pprint
def recursive1(board,colour,x,y,currentx,currenty):
    print(currentx+x,currenty+y) 

    

       
    if ((currentx+x>7)or(currentx+x<0))or((currenty+y<0)or(currenty+y>7)):#wrong position at first. this error must be checked for first
        return True
    elif isenemysquare(board,colour,currentx+x,currenty+y)==True:
        thepiece=getpiece(board,currentx+x,currenty+y)
        print(thepiece,"")
        try:
            if thepiece[1]=='q' or thepiece[1]=='b':
                print(thepiece)
                return False
            else:
                return True
        except:
            print(thepiece)
            return True
    elif isemptySquare(board,currentx+x,currenty+y)==False:
        return True


    else:
        value=recursive1(board,colour,x,y,currentx+x,currenty+y) 
        if value==True:
            return True
        else:#it wasn't true so it returned false, this was a big problem.
            return False

    
  


def diagonalsclear(board,colour,posx,posy) :#tick

    for y in range(-1,2):
        if (y==0):
            pass
        else:
            for x in range(-1,2):
                if (x==0):
                    pass
                
                else:
                    
                    returnvalue=recursive1(board,colour,x,y,posx,posy)
                    print(";")
                    if returnvalue==False:
                        return False
        
    return True            
                        
                        
                   

def straightsclear( board,colour,posx,posy):
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
                posx+=x
                
                while posx+x<=7 and posx+x>=0 and posy<=7 and posy>=0 and isemptySquare(board,posx,posy)==True and horizontalclear==True:
                    posx+=x
                    
                if isenemysquare(board,colour,posx,posy)==True:
                    thepiece=getpiece(board,posx,posy)
                    if thepiece[1]=='q' or thepiece[1]=='r':
                        horizontalclear=False
                else:
                    horizontalclear=True 
                
    print("horizontal done")
    
    for y in range(-1,2): 
        posx=originalx
        posy=originaly
        if x==0:
            pass
        else:
            if verticalclear==True:
                posy+=y
                while posy+y<=7 and posy+y>=0 and posx<=7 and posx>=0 and isemptySquare(board,posx,posy)==True and verticalclear==True:
                    posx+=x
                if isenemysquare(board,colour,posx,posy)==True:
                    thepiece=getpiece(board,posx,posy)
                    if thepiece[1]=='q' or thepiece[1]=='r':
                        horizontalclear=False
                else:
                    verticalclear=True
    print("vertical done")
    if horizontalclear==True and verticalclear==True:
        return True
    else:
        return False

    
def knightclear(board,colour,posx,posy): #tick

    long1=[2,-2]
    short=[1,-1]
    for x in long1:
        for y in short:
            if posx+x <8 and posx+x >-1 and posy+y<8 and posy+y>-1:
                if isenemysquare(board,colour,posx+x,posy+y )==True:
                    thepiece=getpiece(board,posx+x,posy+y)
                    print(thepiece)
                    if thepiece[1]=='k' and thepiece[2]=='n':

                        return False


    print("horizontal clear")
    for y in long1:
        for x in short:
            if posx+x <8 and posx+x >-1 and posy+y<8 and posy+y>-1:
                if isenemysquare(board,colour,posx+x,posy+y)==True:
                    thepiece=getpiece(board,posx+x,posy+y)
                    print(thepiece)
                    if thepiece[1]=='k' and thepiece[2]=='n':

                        return False


    print( "vertical is clear")
    return True
def adjacentclear(board,colour,posx,posy):
    for x in range(-1,2):
            if posx+x <8 and posx+x >-1 and posy<8 and posy>-1:
                if isenemysquare(board,colour,posx+x,posy )==True:
                    thepiece=getpiece(board,posx+x,posy)
                    
                    if thepiece[1]=='k' and thepiece[2]=='i':

                        return False
    for y in range(-1,2):
            if posx <8 and posx >-1 and posy+y<8 and posy+y>-1:
                if isenemysquare(board,colour,posx,posy+y)==True:
                    thepiece=getpiece(board,posx,posy+y)
                    
                    if thepiece[1]=='k' and thepiece[2]=='i':

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
                        if posx +x<8 and posx+x>-1 and posy+y<8 and posy+y>-1 and isenemysquare(board,colour,posx+x,posy+y)==True:
                            thepiece=getpiece(board,posx,posy+y)
                            if (thepiece[1]=='p'and posy+y>posy) or (thepiece[1]=='k' and thepiece[1]=='i'):
                                return False                        
                    elif colour=='white':
                        if posx +x<8 and posx+x>-1 and posy+y<8 and posy+y>-1 and isenemysquare(board,colour,posx+x,posy+y)==True:
                            thepiece=getpiece(board,posx,posy+y)
                            if (thepiece[1]=='p'and posy+y<posy) or (thepiece[1]=='k' and thepiece[1]=='i'):
                                return False

                
    
            
                    

     
    
def minicheck(board,colour,x,y):
    #diagonal
    diagonal=diagonalsclear(board,colour,x,y)


    if (diagonal==False):  
        print("diagonal not clear")
        
        return True
    print("diagonals are clear")

    
    straights=straightsclear(board,colour,x,y)
    if straights==False:
        print("straights not clear")
        return True
    
    print("straights are clear")

    #adjacent for king and pawns
    adjacent=adjacentclear(board,colour,x,y)
    if (adjacent==False):
        print("adjacents aren't clear")
        return True
    
    
    print("adjacents are clear")
    #knight
    knight=knightclear(board,colour,x,y)  # it is better this is done last as chances are less 
    if (knight==False):
        print("knights are not clear")
        return True
    print("knights are clear")
    print(x,y)
    return False
       
    


       
def hello():
    print("hello")
    return "yo"
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
            print("empty")
            return False
              
colour='black'
positionx=1
positiony=2
movedtox=0
movedtoy=5
boardtemp= [['', 'bknight1', 'bbishop1', 'bqueen', '', 'bbishop2', 'bknight2', 'brook2'],
            ['bpawn1', 'bpawn2', 'bpawn3', 'bpawn4', 'bpawn5', 'bpawn6', 'bpawn7', 'bpawn8'],
            ['', '', '', '', '', '', '', ''],['brook1', '', 'bking', 'wrook2', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],['', '', '', '', '', '', '', ''],
            ['wpawn1', 'wpawn2', 'wpawn3', 'wpawn4', 'wpawn5', 'wpawn6', 'wpawn7', 'wpawn8'],
            ['wrook1', 'wknight1', 'wbishop1', 'wking', 'wqueen', 'wbishop2', 'wknight2', '']]
pp=pprint.PrettyPrinter(indent=1,width=100)
record=boardtemp[positiony][positionx]
print(record)
boardtemp[positiony][positionx]=''
boardtemp[movedtoy][movedtox]=record  
pp.pprint(boardtemp)
# pprint.pprint(boardtemp)
tempY=0
# he=hello()
# print(he)

for y in boardtemp:
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
        print("value error")
        tempY+=1

print(boardtemp[they][thex])
print("coordinates start",thex,they)

     

if (minicheck(boardtemp,colour,thex,they) ==False): #mini check finds if new move results in king in danger. 
    print("add")
else: 
    print("don't")
ycount=0
xcount=0
for y in boardtemp:
    xcount=0
    for x in y:
        if x=='':
            # print("x",xcount,"y",ycount)
            boardtemp[ycount][xcount]='      '

        xcount+=1
    ycount+=1        
pp.pprint(boardtemp)
##then the check algorithm which is basically the same as above

##then the checkmate algorithm


## for en passant check if current piece is pawn, if last moved piece was pawn and that pawn is adjacent now.
##for taking pieces I suggest a list where update pieces are removed and removed from board array. 
##for upgrading pawns, create new piece. 


#Note: The king can't move through check. The only time this is a problem is castling and we'll worry about that 

#when we get there. 