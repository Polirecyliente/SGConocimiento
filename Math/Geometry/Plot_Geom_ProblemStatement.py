import argparse

import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    """
This program serves to plot the geometry of a problem statement.
For example, if you need to plot labeled segments, and labeled angles, this
program may help you.
"""

#T# arg parsing section
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--segments",nargs='+',help="-s or --segments receives strings with the segments to plot.\
 Each segment has 6 parts: labelPoint1 labelPoint2 xPoint1 yPoint1 xPoint2 yPoint2. For example --segments 'A B 1 1 3 4' plots segment AB, A is the point (1,1), B is (3,4)")
    parser.add_argument("-a","--angles",nargs='+',help="-a or --angles receives strings with the angles to plot.\
 Each angle has 5 parts: labelVertex angleSide1 angleSide2 xVertex yVertex. For example --angles 'A pi/3 0 2 2' plots the angle pi/3 with an horizontal side1 with vertex at point (2,2). Angles in radians")
    args = parser.parse_args()
    
    segments = args.segments
    angles = args.angles

#T# plot start section
    fig1, ax1 = plt.subplots()
    ax1.set_aspect('equal','box')
    for spine in ['top','left','right','bottom']:
        ax1.spines[spine].set_visible(False)
    ax1.xaxis.set_visible(False)
    ax1.yaxis.set_visible(False)

    

    if segments == None and angles == None:
        ax1.plot([5,5],[5,5],color='k',marker='o')
        plt.show()
        exit(0)
    pText = 1/30
    if segments is not None:
        for segment in segments:
            segment = segment.replace("pi",str(np.pi))
            segment = segment.split()
            segment[2:] = list(map(eval,segment[2:]))
            P1Label = segment[0]
            P2Label = segment[1]
            xP1 = segment[2]
            yP1 = segment[3]
            xP2 = segment[4]
            yP2 = segment[5]
            ax1.plot([xP1,xP2],[yP1,yP2],color='k')
            pX = ax1.get_xlim()[1] - ax1.get_xlim()[0]
            ax1.annotate(P1Label,xy=(xP1,yP1-pText*pX),xytext=(xP1,yP1-pText*pX))
            ax1.annotate(P2Label,xy=(xP2,yP2-pText*pX),xytext=(xP2,yP2-pText*pX))
    pX = ax1.get_xlim()[1] - ax1.get_xlim()[0]
    pSide = 1/2
    if angles is not None:
        for angle in angles:
            angle = angle.replace("pi",str(np.pi))
            angle = angle.split()
            angle[1:] = list(map(eval,angle[1:]))
            aLabel = angle[0]
            aSide1 = angle[1]
            aSide2 = angle[2]
            xVertex = angle[3]
            yVertex = angle[4]
            xSide1 = pSide*pX*math.cos(aSide1) + xVertex
            ySide1 = pSide*pX*math.sin(aSide1) + yVertex
            xSide2 = pSide*pX*math.cos(aSide2) + xVertex
            ySide2 = pSide*pX*math.sin(aSide2) + yVertex
            ax1.plot([xVertex,xSide1],[yVertex,ySide1],color='k')
            ax1.plot([xVertex,xSide2],[yVertex,ySide2],color='k')
            ax1.annotate(aLabel,xy=(xVertex-pText*pX,yVertex-pText*pX),xytext=(xVertex-pText*pX,yVertex-pText*pX))

    ax1.margins(0.15)
    plt.show()

if __name__ == '__main__':
    main()