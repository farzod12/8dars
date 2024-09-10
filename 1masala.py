import os
os.system("cls")
file=open("salom.txt","r")
malumot=file.readlines()
#print(malumot)
suz=[]
for row in malumot:
    for word in row.split():
        suz.append(word)
print(suz[-1])        
file.close()
