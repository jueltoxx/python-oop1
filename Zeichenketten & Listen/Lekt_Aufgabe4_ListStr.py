import itertools


liste1 = ["hxllo","hallo","keiner","reiner","hallo"]

for a,b in itertools.combinations(liste1,2):

    laengeA = len(a)
    laengeB = len(b)

    if a == b:
        print("variant1",a)
    elif laengeB - 2 <= laengeA <= laengeB + 2:
        print(a)