import re 
string="""bpawn1.update()
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
"""
k=re.compile("((b|w)([a-z]|[1-9])*)")
g=k.findall(string)
print(g)
list1=[]
for x in g:
    list1.append(x[0])
print(list1)
