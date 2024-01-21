word1 = "abxz"
word2 = "abx"
n = 0


for letter in word1:
    #print(letter)
    letterw1 = letter

    if letter == word2[n]:
        print("Zeichen",n,"Matched")
        n += 1