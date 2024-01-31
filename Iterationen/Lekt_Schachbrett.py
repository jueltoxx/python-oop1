#Schachbrett => schwarz = #, Weiss = "" 8*8

n = 9

for i in range (1,n):
    for j in range(1,n):
        if (i+j) % 2 == 0:
            print("  ", end="")
        else:
            print("#", end="")
    print("")