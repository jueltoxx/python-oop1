originalword = input("Geben Sie ein Wort ein: ")
letters = 0

for c in originalword:
 letters = letters + 1

print("Anzahl Buchstaben:", letters)

newword = ""
count = letters - 1
while (count != -1):
 newword = newword + originalword[count]
 #sys.stdout.write(originalword[count])
 #print(originalword[count], end="", sep="")
 count = count - 1

print(newword)
    