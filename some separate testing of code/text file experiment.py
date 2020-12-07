textfile=open("text.txt","a+")
textfile.seek(0)
x=1
while x!= '':
    j=x
    x=textfile.readline()
print(j)   
alphabet=list('abcdefghijklmnopqrstuvwxyz')
num=''
char=''
digit=1
while char not in alphabet:
    num=num+char
    textfile.seek(0)
    char=textfile.read(digit)
    char=char[digit-1]#string indexing starts at 0 opposed to 1 for text files.
    digit+=1

    
print("num",num)
textfile.seek(0)
print((textfile.readline()).strip())

print((textfile.readline()).strip())
last=((textfile.readline()).strip()).replace('g','')
print(last)

textfile.close()




#ctrl / comments code
# ctrl \ opens in new panel.
#ctrl ' opens ditto
#ctrl g is switch between windows
