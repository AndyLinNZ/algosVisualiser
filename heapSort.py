import time

def build_heap(array, drawArray, speed):
    n = len(array)
    for k in range(n//2 - 1, -1, -1):
        max_heapify(array, drawArray, speed, n, k)

def heap_sort(array, drawArray, speed):
    build_heap(array, drawArray, speed)
    size = len(array)-1
    for i in range(size, -1, -1):
        eject_heap(array, drawArray, speed, i)
    colourArray = ['turquoise' for _ in range(len(array))]
    drawArray(array, colourArray)
    

def max_heapify(array, drawArray, speed, n, i):
    # i is the parent node
    value = array[i]
    heap = False
    while not heap and 2*i + 1<= n-1:
        largerChild = 2*i + 1
        # Find the larger child
        if largerChild < n-1:
            if array[largerChild] < array[largerChild+1]:
                largerChild += 1

        colourArray = ['green' if x == i else ('red' if x == largerChild else 'turquoise') for x in range(len(array))]
        time.sleep(speed)
        drawArray(array, colourArray)

        if value >= array[largerChild]:
            heap = True
        else:
            # swap largest child with node
            array[i] = array[largerChild]
            i = largerChild
    array[i] = value
        
def eject_heap(array, drawArray, speed, k):
    array[0], array[k] = array[k], array[0]
    max_heapify(array, drawArray, speed, k, 0)
    
