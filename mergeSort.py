# mergeSort algorithm
import time


#Other working solution copied code

def merge_sort(array, drawArray, speed):
    mergeSortHelper(array, 0, len(array)-1, drawArray, speed)
    drawArray(array, ['turquoise']*len(array))
    return array

def mergeSortHelper(array, startIdx, endIdx, drawArray, speed):
    if startIdx < endIdx:
        mid = startIdx + (endIdx - startIdx) // 2
        mergeSortHelper(array, startIdx, mid, drawArray, speed)
        mergeSortHelper(array, mid + 1, endIdx, drawArray, speed)
        merge(array, startIdx, mid, endIdx, drawArray, speed)

def merge(array, startIdx, mid, endIdx, drawArray, speed):

    i = 0
    j = 0
    leftArray = array[startIdx:mid+1]
    rightArray = array[mid+1:endIdx+1]

    for k in range(startIdx, endIdx+1):
        if i < len(leftArray) and j < len(rightArray):
            if leftArray[i] <= rightArray[j]:
                array[k] = leftArray[i]
                i += 1
            else:
                array[k] = rightArray[j]
                j += 1
        
        elif i < len(leftArray):
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
            j += 1 
        drawArray(array, compareColour(array, k))
        time.sleep(speed)
        
            
    drawArray(array, ['green' if x>= startIdx and x <= endIdx else 'turquoise' for x in range(len(array))])
    time.sleep(speed)


def compareColour(array, k):
    colour = []
    for i in range(len(array)):
        if k == i:
            colour.append("red")
        else:
            colour.append("turquoise")
    return colour

"""
# my version of mergesort           

def merge_sort(array, drawArray):
    array_cpy = list(array)
    mergeSortHelper(array, 0, len(array)-1, array_cpy, drawArray)
    return array

def mergeSortHelper(array, startIdx, endIdx, array_cpy, drawArray):
    if startIdx < endIdx:
        mid = startIdx + (endIdx - startIdx) // 2
        mergeSortHelper(array_cpy, startIdx, mid, array, drawArray)
        mergeSortHelper(array_cpy, mid + 1, endIdx, array, drawArray)
        merge(array, startIdx, mid, endIdx, array_cpy, drawArray)

def merge(array, startIdx, mid, endIdx, array_cpy, drawArray):

    i = startIdx
    j = mid+1
    k = startIdx

    while i <= mid and j <= endIdx:
        colourArray(array, i, j, drawArray, 'red')
        time.sleep(0.5)
        if array_cpy[i] <= array_cpy[j]:
            colourArray(array, i, j, drawArray, 'green')
            array[k] = array_cpy[i]
            i += 1
        else:
            colourArray(array, i, j, drawArray, 'green')
            array[k] = array_cpy[j]
            j += 1
        k += 1
    
    while i <= mid:
        colourArray(array, i, j, drawArray, 'green')
        array[k] = array_cpy[i]
        i += 1
        k += 1
    while j <= endIdx:
        colourArray(array, i, j, drawArray, 'green')
        array[k] = array_cpy[j]
        j += 1
        k += 1
    
    colourArray(array, startIdx, endIdx, drawArray, 'turquoise')
    
def colourArray(array, i, j, drawArray, colour):
    colouredArray = [colour if x == i or x == j else 'turquoise' for x in range(len(array))]
    drawArray(array, colouredArray)
    time.sleep(0.2)
"""

    
    