import csv
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerBase
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

list_color  = ["red", "yellow", "blue", "green"]
list_mak    = ["s", "o", "v", "*"]
list_lab    = ['STD', 'Numpy', 'Box-Mueller', 'Marsaglia']

class MarkerHandler(HandlerBase):
    def create_artists(self, legend, tup,xdescent, ydescent,
                        width, height, fontsize,trans):
        return [plt.Line2D([width/2], [height/2.],ls="",
                       marker=tup[1],color=tup[0], transform=trans)]

def plotDistrs(fileName, fig, position, label):
    N = []
    P = []
    STD = []
    Numpy = []
    BoxMueller = []
    Marsaglia = []
    with open(fileName, newline='') as dklsFile:
        reader = csv.reader(dklsFile, delimiter=',')
        next(reader, None)  # skip the headers
        for row in reader:
            N.append(float(row[0]))
            P.append(float(row[1]))
            STD.append(float(row[2]))
            Numpy.append(float(row[3]))
            BoxMueller.append(float(row[4]))
            Marsaglia.append(float(row[5]))
    graph = fig.add_subplot(position, projection='3d')
    for distr, c, m in [(STD, 'red', 's'), (Numpy, 'yellow', 'o'), (BoxMueller, 'blue', 'v'), (Marsaglia, 'green', '*')]:
        graph.scatter(N, P, distr, color=c,marker=m)
    graph.set_xlabel('N')
    graph.set_ylabel('P')
    graph.set_zlabel(label)


fig1 = plt.figure()
fig1.legend(list(zip(list_color,list_mak)), list_lab,
          handler_map={tuple:MarkerHandler()})
fig2 = plt.figure()
fig2.legend(list(zip(list_color,list_mak)), list_lab,
          handler_map={tuple:MarkerHandler()})
plotDistrs('../binom_bad/DKLs.csv', fig1, 111, 'DKL')  # row 1, column 1, Plot 1
plotDistrs('../binom_bad/durations.csv', fig2, 111, 'T')  # row 1, column 2, Plot 1
plt.show()