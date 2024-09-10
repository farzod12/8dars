from os import system
system("cls")
fayl=open("natijaa.txt","r")
qatorlar=fayl.readlines()
suzlar=[]
for row in qatorlar:
    for word in row.split():
        suzlar.append(word)
suzlar.sort(key=len)

print(suzlar[-1])
fayl.close()