allPieces=['bpawn1', 'bpawn2', 'bpawn3', 'bpawn4', 'bpawn5', 'bpawn6', 'bpawn7', 'bpawn8', 'brook1',
                'bknight1', 'bbishop1', 'bqueen', 'bking', 'bbishop2', 'bknight2', 'brook2', 'wpawn1',
                'wpawn2', 'wpawn3', 'wpawn4', 'wpawn5', 'wpawn6', 'wpawn7', 'wpawn8', 'wrook1', 'wknight1',
                'wbishop1', 'wking', 'wqueen', 'wbishop2', 'wknight2', 'wrook2']
turn='black'
def function(item):
    if item not in ['white','black']:
        print(item)

    
if turn=='white':
    index=-1
    increment=-1
else:
    index=0
    increment=1
item=turn#initiates loop
while item[0]==turn[0]:
    function(item)
    item=allPieces[index]
    index=index+increment



