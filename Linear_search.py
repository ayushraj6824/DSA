def linear_search(list,target):
   for i in range(0,len(list)):
      if list[i]==target:
         return i
   return None

def verify(index):
   if index is not None:
      print("Target found at index :",index)
   else:
      print("Target not found in list")



lst=[]
n=int(input("Enter a number of element :"))
for i in range (0,n):
   num=int(input())
   lst.append(num)
print("list: ",lst)

s=int(input("Enter a searcing element:"))


result=linear_search(lst,s)
verify(result)