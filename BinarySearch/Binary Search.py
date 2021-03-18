def BinarySearch(list,x):
    b=len(list)
    u=len(list)
    l=0
    while l<=u:
        avg = (l + u) // 2


        if avg > (b - 1):
            print("not found")
            break
        elif x==list[avg]:
            print("found ")
            break
        elif x>list[avg]:
            l=avg+1
        elif x<list[avg]:
            u=avg-1
        else:
            None

list=[]
x=int(input("enter the number of values u want"))
print("enter the values")
i=0
while i<x:
    y=int(input())
    list.append(y)
    i=i+1
list.sort()

print("enter the value u want")
u=int(input())
BinarySearch(list,u)
