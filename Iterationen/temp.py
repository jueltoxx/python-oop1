word1 = "abxz"
word2 = "abx"
n = 1

for letter in word1:
    #print(letter)
    letterw1 = letter

    if letterw1 == word2[n]:
        print("Zeichen",n,"Matched")