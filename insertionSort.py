# insertion sort function
import time

def insertion_sort(array, drawArray, speed):
    for i in range(1, len(array)):
        j = i-1
        while (j >=0 and array[j] > array[j+1]):
            array[j], array[j+1] = array[j+1], array[j]
            j -= 1

            # colour the array, green = being swapped, red = being checked against
            colourArray = ['red' if x == j else ('green' if x == i else 'turquoise') for x in range(len(array))]
            drawArray(array, colourArray)
            time.sleep(speed)

    # insertion sort finished, so do a final pink array animation        
    for i in range(len(array)):
        colourArray = ['blue' if x == i else 'turquoise' for x in range(len(array))]
        drawArray(array, colourArray)
        time.sleep(speed/2)

    # back to being turqoise
    colourArray = ['turquoise' for x in range(len(array))]
    drawArray(array, colourArray)