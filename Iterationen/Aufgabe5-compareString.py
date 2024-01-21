string1 = input("Gebe String 1 ein: ")
string2 = input("Gebe String 2 ein: ")

match = True
n = 0 

while match == True:
    for letter in string1:
        letterstring1 = letter

        for letter in string2:
            letterstring2 = letter
        
            if letterstring1 != letterstring2:
                match = False
                print("Strings nicht gleich!")
            elif letterstring1 == letterstring2:

                print("Match")
                n += 1
                
        

    