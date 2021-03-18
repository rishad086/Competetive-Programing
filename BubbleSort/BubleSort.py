def QuickSort(list):
    for i in range (len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp

list=[2,1,3,4,2,3,26,7,3,25,9,0,7]
QuickSort(list)
print(list)

