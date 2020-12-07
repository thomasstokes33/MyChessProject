import pprint
pp = pprint.PrettyPrinter(indent=4,width=100)
boardState=open(r"some separate testing of code/boardstate.txt","a+")#YOU can remove the folder name if an error appears!
boardState.seek(0)
array=[]
checkdig='1'
while checkdig != '':
    lastvalue=checkdig.strip("\n")
    if checkdig!='1':
        array.append(lastvalue)
    checkdig=boardState.readline()
    
pp = pprint.PrettyPrinter(indent=4,width=500)
pp.pprint(array)
counter=0
while (lastvalue) in array:
    counter+=1
    array.remove(lastvalue)
print(counter)