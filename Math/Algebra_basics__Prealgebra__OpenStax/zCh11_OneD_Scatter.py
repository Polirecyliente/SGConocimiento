import sys
from decimal import Decimal

#T# the statistics module has functions like mean() to calculate the average
import statistics

import matplotlib.pyplot as plt

argv = sys.argv

def main(argv):
    """Plots a 1D scatter plot of a set of x points. Colors different the
    average."""
    pointsX = list(map(Decimal,argv[1:]))
    pointsY = [0 for i1 in range(0,len(pointsX))]
    print("Graphing scatter plot...")
    graphScatterPlot(pointsX,pointsY)

def graphScatterPlot(pointsX,pointsY):
#T# calculate the average of a set of points with statistics.mean(points)
    avg = statistics.mean(pointsX)
#T# calculate the median of a set of points with statistics.median(points)
    medi = statistics.median(pointsX)
#T# calculate the mode of a set of points with statistics.mode(points),
#T# it must be in a try except block, it throws an exception if no mode
    try:
        mode = statistics.mode(pointsX)
    except:
        mode = -1
    print("The average is:",avg,"\nThe median is:",medi,"\nThe mode is:",mode)
#T# make a scatter plot with plt.scatter()
    plt.scatter(pointsX,pointsY)
    plt.scatter([avg,medi,mode],[0,0,0],c=['k','g','r'])
    plt.show()
    return

if __name__ == '__main__':
    main(argv)