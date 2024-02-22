data_list = [1,102012,4,46553,33,22,-2548,-2548,-2548]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    print("m8 I'm fcking wasted")
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

print (new_list)