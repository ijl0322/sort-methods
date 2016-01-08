def bubbleSort(lists):
    for item in lists:
        for num in range(len(lists)-1):
            print lists
            if lists[num] > lists[num + 1]:
                temp = lists[num]
                lists[num] = lists[num + 1]
                lists[num + 1] = temp
    return lists

#print bubbleSort([5,3,2,1])

def selectionSort(lists):
    sortedList = []
    while len(lists) > 0:
        smallest = None
        for elt in lists:
            if smallest == None:
                smallest = elt
            elif smallest > elt:
                smallest = elt
        sortedList.append(smallest)
        lists.remove(smallest)
    return sortedList
    
print selectionSort([5,2,1,3])
                
                         