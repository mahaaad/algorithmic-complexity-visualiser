#This module takes the randomly generated lists, sorts them, and counts the iterations
def bubbleSort(items):
    count = 0
    for j in range(0,len(items) - 1,1):
        count += 1
        for i in range(0,len(items) - 1,1):
            count += 1
            if items[i] < items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp

    return count

def insertionSort(items):
    count = 0
    for i in range(1, len(items)):
        count += 1
        key = items[i]
        j = i - 1
        while j >= 0 and key < items[j]:
            count += 1
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key

    return count

def optimizedBubble(items):
    n = len(items)
    count = 0
    for i in range(n):
        count += 1
        swapped = False
        for j in range(0, n - i - 1):
            count += 1
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        #if no elements were swapped it breaks the loop to avoid unnecessary iterations
        if swapped == False:
            break

    return count

def selectionSort(items):
    count = 0
    for i in range(0,len(items)-1,1):
        min = i
        count += 1
        for j in range(i + 1, len(items)):
            count += 1
            if items[min] > items[j]:
                min = j
        items[i], items[min] = items[min], items[i]

    return count

if __name__ == "__main__":
    print(bubbleSort([9,8,7,6,5,4,3,2,1]))
    # returns count for one of the algorithms