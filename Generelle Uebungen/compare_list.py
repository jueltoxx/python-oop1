list1 = [1,2,3,4,5,6,7,8]
list2 = [1,2,3,4,5,6,7]

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            print("True")