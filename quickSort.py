# quicksort algorithm
import random
import time

def quick_sort(array, drawArray, speed):
    left = 0
    right = len(array)-1
    quickSort(array, left, right, drawArray, speed)

    # finished sorting
    for i in range(len(array)):
        colourArray = ['blue' if x == i else 'turquoise' for x in range(len(array))]
        drawArray(array, colourArray)
        time.sleep(speed/2)

    # final array to be turquoise
    drawArray(array, ['turquoise']*len(array))
    return array

def quickSort(array, left, right, drawArray, speed):
    if left < right:
        index = partition(array, left, right, drawArray, speed)
        quickSort(array, left, index-1, drawArray, speed)
        quickSort(array, index+1, right, drawArray, speed)


def partition(array, left, right, drawArray, speed):
    pivot = array[right]
    pIndex = left
    for i in range(left, right):
        drawArray(array, getColourArray(array, pIndex, i, pivot))
        time.sleep(speed)
        if array[i] <= pivot:
            array[pIndex], array[i] = array[i], array[pIndex]
            pIndex += 1

    array[right], array[pIndex] = array[pIndex], array[right]

    return pIndex

def getColourArray(array, pIndex, left, pivot):
    colourArray = ['red' if pIndex == x or x == left else ('green' if array[x] == pivot else 'turquoise') for x in range(len(array))]
    
    return colourArray

    
