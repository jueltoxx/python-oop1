#find the first 10 odd numbers

zahl = 1
resultate = 0

while resultate < 10:
    
    if zahl % 2 == 0:
       zahl += 1
       continue

    print("uneven:",zahl)
    zahl += 1
    resultate += 1


    
