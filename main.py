import sorting as s
import visualizer as vs
import random

def get_random_array(length):
    n = list(range(length))
    random.shuffle(n)
    return n

def getTitle(name):
    til = name
    til = til.replace('_', ' ')
    return til

array_size = 30
tempArr = get_random_array(array_size)

bubbleArr = s.Array(tempArr)
gnomeArr = s.Array(tempArr)

# Bubble
s.bubble_sort(bubbleArr)
bubblePlot = vs.Plotter(bubbleArr.pile, title="Algorithm: {}".format(getTitle(s.bubble_sort.__name__)), 
                        repeat=True, interval=1)
bubblePlot.plot()

# Gnome
s.gnome_sort(gnomeArr)
gnomePlot = vs.Plotter(gnomeArr.pile, title ="Algorithm: {}".format(getTitle(s.gnome_sort.__name__)),
                        repeat=True, interval=1)
gnomePlot.plot()