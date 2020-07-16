# bubble sort
import time

def bubble_sort(array, drawArray, speed):
    isSorted = False
    lastUnsorted = len(array)-1
    while (not isSorted):
        isSorted = True
        for i in range(lastUnsorted):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = False

                # colour the array, green = being swapped, red = being checked against
                colourArray = ['red' if x == i else ('turquoise' if x <= lastUnsorted else 'green') for x in range(len(array))]
                drawArray(array, colourArray)
                # time.sleep(speed)
        
        lastUnsorted -= 1
    
    # finished sorting
    for i in range(len(array)):
        colourArray = ['blue' if x == i else ('turquoise' if x < i else 'green') for x in range(len(array))]
        drawArray(array, colourArray)
        # time.sleep(speed/2)
    # colour the array in turquoise
    drawArray(array, ['turquoise']*len(array))


