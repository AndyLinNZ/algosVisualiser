# Sorting Algorithms Visualiser
# Andy Lin 28/03/2020

from tkinter import *
from tkinter import ttk
from insertionSort import insertion_sort
from mergeSort import merge_sort
from bubbleSort import bubble_sort
from quickSort import quick_sort
import random

# variables
algorithms = ['Mergesort', 'Quicksort', 'Bubblesort', 'Insertionsort']
MAXWIDTH = 900
MAXHEIGHT = 700
MAXNUM = 400
MINNUM = 1
array = []


# starting window
window = Tk()
window.maxsize(MAXWIDTH, MAXHEIGHT)
window.title("Algorithms Visualiser")
window.config(bg="black")

selected_alg = StringVar()
# functions
def drawArray(data, colourArray):
    canvas.delete("all")
    c_height = 480
    c_width = MAXWIDTH
    x_width = c_width / len(data)

    normalisedData = [i/max(data) for i in data]
    for i, height in enumerate(normalisedData):
        # top left hand corner of bar
        x0= i*x_width
        y0= c_height - height*(c_height-100)
        # bottom right hand corner of bar
        x1 = (i+1)*x_width
        y1 = c_height

        # draw the rectangles
        canvas.create_rectangle(x0, y0, x1, y1, fill = colourArray[i])

    window.update_idletasks()

def generate():
    """ Generates a new array based on user inputs """
    global array
    print("You've selected: " + selected_alg.get())
    sizeNum = sizeEntry.get()

    # create array
    array = []
    for _ in range(sizeNum):
        x = random.randint(MINNUM, MAXNUM)
        array.append(x)
    colourArray = ['turquoise' for i in range(len(array))]
    drawArray(array, colourArray)

def startAlgorithm():
    global array
    if not array:
        return
    
    # get the speed of the algorithm visualiser
    sizeNum = sizeEntry.get()
    speed = 10/(sizeNum*pow(sizeNum, 0.5))

    # visualise an algorithm
    if algoMenu.get() == "Insertionsort":
        insertion_sort(array, drawArray, speed)
    if algoMenu.get() == "Mergesort":
        merge_sort(array, drawArray, speed)
    if algoMenu.get() == "Bubblesort":
        bubble_sort(array, drawArray, speed)
    if algoMenu.get() == "Quicksort":
        quick_sort(array, drawArray, speed)

# Frame/ Where our functionalies are
UI_frame = Frame(window, width = MAXWIDTH, height = 200, bg = "blue")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# Canvas/Where our algorithm is displayed
canvas = Canvas(window, width = MAXWIDTH, height = 480, bg = "white")
canvas.grid(row=1, column=0, pady=5)

# User Interface Area
# first row of functions
label = Label(UI_frame, text = "Algorithms", bg = "grey")
label.grid(row=0, column=0, padx=5, pady=5)

algoMenu = ttk.Combobox(UI_frame, textvariable = selected_alg, values = algorithms)
algoMenu.current(0)
algoMenu.grid(row=0, column=1, padx=5, pady=5)

generateButton = Button(UI_frame, text = 'Generate', command = generate, bg = "grey", font = ("Helvetica", 9, "bold italic"))
generateButton.grid(row=0, column=2, padx=5, pady=5)

startButton = Button(UI_frame, text = 'Start', command = startAlgorithm, bg = "grey", font = ("Helvetica", 9, "bold italic"))
startButton.grid(row=0, column=4, padx=5, pady=5)
# second row of functions
sizelabel = Label(UI_frame, text="       Size:      ", bg="grey")
sizelabel.grid(row=1, column=0, padx=5, pady=5)
sizeEntry = Scale(UI_frame, from_ =1, to=200, length = 200, digits=3, resolution = 0.1, orient= HORIZONTAL, label= "Array Size and Speed:")
sizeEntry.grid(row=1, column=1, padx=200, pady=5)
sizeEntry.set(100)

window.mainloop()