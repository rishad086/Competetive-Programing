def LinearSearch(list,u):
    j = 0
    while j < len(list):
        if u == list[j]:
            return True,j
        j=j+1
    return False,None




list=[]
x=int(input("enter the number of values u want"))
print("enter the values")
i=0
while i<x:
    y=int(input())
    list.append(y)
    i=i+1

print("enter the value u want")
u=int(input())
t,r=LinearSearch(list,u)

if t==True:
    print("Found","index value=",r)
else:
    print("Not Found")

