
def recursive1(board,colour,x,y,currentx,currenty):
    if isenemysquare(board,colour,currentx+x,currenty+y)==True:
        return False
    
    elif isemptySquare(board,currentx+x,currenty+y):
        return True
        
    elif ((currentx+x>7)or(currenty+x<0))or((currenty+y>0)or(currenty+y>7)):
        return True
    else:
        value=recursive1(board,colour,x,y,currentx+x,currenty+y) 
        if value==True:
            return True
        else:
            return False


  


def diagonalsclear(board,colour,posx,posy) :

    for y in range(-1,2):
        if (y==0):
            pass
        else:
            for x in range(-1,2):
                if (x==0):
                    pass
                
                else:
                    returnvalue=recursive1(board,colour,x,y,posx,posy)
                    if returnvalue==False:
                        return False
    return True            
                        
                        
                   



def minicheck(board,colour,x,y):
    ##diagonal
    diagonal=diagonalsclear(board,colour,x,y)


    if (diagonal==False):  
        return True
    
    ##straights
    straights=straightsclear(board,colour,x,y)
    if straights==False:
        return True

    ##adjacent
    adjacent=adjacentclear(board,colour,x,y)
    if (adjacent==False):
        return True
    

   
    ##knight
    knight=knightclear(board,colour)
    if (knight==False):
        return True
       
    


       


##then the check algorithm

##then the checkmate algorithm

## for en passant check if current piece is pawn, if last moved piece was pawn and that pawn is adjacent now.
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
              

self.posx=1
self.posy=2
movedtox=4
movedtoy=5
self.boardtemp= [['brook1', 'bknight1', 'bbishop1', 'bqueen', 'bking', 'bbishop2', 'bknight2', 'brook2'],
            ['bpawn1', 'bpawn2', 'bpawn3', 'bpawn4', 'bpawn5', 'bpawn6', 'bpawn7', 'bpawn8'],
            ['', '', '', '', '', '', '', ''],['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],['', '', '', '', '', '', '', ''],
            ['wpawn1', 'wpawn2', 'wpawn3', 'wpawn4', 'wpawn5', 'wpawn6', 'wpawn7', 'wpawn8'],
            ['wrook1', 'wknight1', 'wbishop1', 'wking', 'wqueen', 'wbishop2', 'wknight2', 'wrook2']]
record=self.board[self.posy][self.posx]
self.board[self.posy][self.posx]=''
self.board[movedtoy][movedtoy]=record
if ( minicheck(self.boardtemp,colour,movedtox,movedtoy) ==False) :
    availableSquares.append(square)
    availableSquarex.append(self.posx)
