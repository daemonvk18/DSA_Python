def merge(list1,list2):
    i,j=0,0
    new_list = []
    while i<len(list1) and j<len(list2):
        if list1[i]<=list2[j]:
            new_list.append(list1[i])
            i+=1
        else:
            new_list.append(list2[j])
            j+=1
    while j<len(list2):
        new_list.append(list2[j])
        j+=1
    while i<len(list1):
        new_list.append(list1[i])
        i+=1

    return new_list


def merge_sort(my_list):
    if len(my_list)==1:return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    return merge(left,right)

print(merge_sort([3,1,4,2]))        
