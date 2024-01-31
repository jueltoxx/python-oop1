word1 = input("Geben Sie Sting 1 ein: ")
word2 = input("Geben Sie Sting 2 ein: ")
match = True

#zählen ob glecih lang
lenght1 = len(word1)
lenght2 = len(word2)

n = 0
anzunt=0

if lenght1 != lenght2:
    print("FALSE: Strings matchen nicht. Länge passt nicht")
else:
    for letter in word1:
        #print(letter)
        letterw1 = letter
        
        if letterw1 == word2[n]:
            #print("Zeichen",n,"Matched")
            n = n + 1
            if lenght2 == n:
                print("TRUE: Die Strings sind gleich")
                anzunt += 1
                print (anzunt)
                continue
        else:
            print("FALSE")
            match = False
           
            