def binary_search(list,target):
    first=0
    last=len(list)-1

    while first<=last:
        midpoint=(first+last)//2

        if list[midpoint]==target:
            return midpoint
        elif list[midpoint]<target:
            first=midpoint+1
        else:
            last=midpoint-1
    return None

def verify(index):
    if index is not None:
        print("Target is found in list",index)
    else:
        print("Target is not found in list")

lst=[]
n=int(input("Enter a number of element :"))
for i in range (0,n):
   num=int(input())
   lst.append(num)

lst.sort()
print("sorted list: ",lst)

s=int(input("Enter a searcing element:"))


result=binary_search(lst,s)
verify(result)