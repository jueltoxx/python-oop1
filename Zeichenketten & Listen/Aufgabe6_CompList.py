liste1 = [1,2,5,5]
liste2 = [4,4,3,4]

for i in liste1:
    for j in liste2:
        if i == j:
            print("True")
            quit()
        else:
            print("False")