def bubbleSort(lists):
    for item in lists:
        for num in range(len(lists)-1):
            print lists
            if lists[num] > lists[num + 1]:
                temp = lists[num]
                lists[num] = lists[num + 1]
                lists[num + 1] = temp
    return lists

print bubbleSort([5,3,2,1])
                