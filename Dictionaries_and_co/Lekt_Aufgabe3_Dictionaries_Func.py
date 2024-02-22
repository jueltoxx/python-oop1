keys = ['Ten','Twenty','Thirdy','hehe']
values = [10,20,30,"oh no"]

peter = ['Pen','Twenty','Thirdy',]
gisela = [44,20,30]
    
def create_dictionary(keys,values):
    dict = {}
    i = 0
    for key in keys:
        dict[keys[i]] = values[i]
        i+=1

    return dict

result = create_dictionary(keys,values)
print(result)

result2 = create_dictionary(peter,gisela)
print(result2)