import pprint
pp = pprint.PrettyPrinter(indent=4,width=100)
boardState=open("boardstate.txt","a+")
boardState.seek(0)
array=[]
checkdig='1'
while checkdig != '':
    lastvalue=checkdig
    if checkdig!='1':
        array.append(lastvalue)
    checkdig=boardState.readline()
    pp.pprint(checkdig)
pp = pprint.PrettyPrinter(indent=4,width=100)
pp.pprint(array)
print()
print()
print()
print(lastvalue)
counter=0
while lastvalue in array:
    counter+=1
    array.remove(lastvalue)
print(counter)