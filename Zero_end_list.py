# From a List of number 
# Move Zero to  the end of the List

list=[10,2,3,4,0,3,0,4,0,2,0,0,10]

for item in list:
    if item==0:
        list.remove(item)
        list.append(item)

print(list)