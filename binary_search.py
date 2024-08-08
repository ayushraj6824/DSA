def binary_search(list,target):
    first=0
    last=len(list)-1

    while first<=last:
        midpoint=(first+last)//2

        if midpoint==target:
            return midpoint
        elif midpoint<target:
            first=midpoint+1
        else:
            last=midpoint-1
    return None

def verify(index):
    if index is not None:
        print("Target is found in list",index)
    else:
        print("Target is not found in list")

number=[1,2,3,4,5,6,7,8,9,10]
result=binary_search(number,6)
verify(result)
