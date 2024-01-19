originalword = "Hans"
letters = 0

for c in originalword:
 letters = letters + 1

print("Anzahl Buchstaben:", letters)

count = letters - 1
while (count != -1):
 print(originalword[count])
 count = count - 1
    