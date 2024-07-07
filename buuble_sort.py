def buuble_sort(list1)->list:
    for i in range(len(list1)-1,0,-1):
        for j in range(i):
            if list1[j] > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1                   


print(buuble_sort([2,4,6,5,1,3]))