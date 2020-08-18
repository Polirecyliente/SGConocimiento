import sys
import re
import math
from decimal import *
getcontext().prec = 10
import constantsAGM as cA
#T# from the constantsAGM is used:
#T# xAmin is the minimum x in the graphed number line or graphed area
#T# xAmax is the maximum x in the graphed number line or graphed area
#T# yAmin is the minimum y in the graphed number line or graphed area
#T# yAmax is the maximum y in the graphed number line or graphed area

#T# if the GUI was used, use a matplotlib's interactive backend
#if cA.GUIUSE is True:
    #import matplotlib
    #matplotlib.use('TkAgg')
#T# if the CLI was used, use a matplotlib's non interactive backend
#else:
    #import matplotlib
    #matplotlib.use('svg')
import matplotlib.pyplot as plt

#T# DOCUMENTATION:
#T# (1) makegraph is the function that carries the weight of graphing

#T# (1.1) arrowKwargs holds the default args to make the arrow look good

#T# (1.2) check that both the operation and the format strings are valid
#T# first check that the operation string is valid with validOp for valid operation
#T# if validOp is not None that means a match was found, a valid op was found
#T# in the regex string there are three groups: first group is operand one,
#T# second group is the operation symbol, and third group is the operand two

#T# (1.3) fmtStr is for format string
#T# check if the user is using a format string
#T# fmtStr must name a valid matplotlib style (like seaborn, bmh, etc)
#T# try to use the selected matplotlib style, if it's invalid exit

#T# (1.4) cast the operands as float values, assign the symbol to a variable

#T# (1.5) kScale allows the displayed segment to be bigger than the used number line
#T# by a given factor. If the final showed segment is bigger this leaves space
#T# for the axis arrows to be seen outside the number line
#T# noClipP is a proportion to avoid clipping of ticklabels. The ignored tick
#T# is the context tick (the one that shows a power of 10)
#T# resA is the result of the operation

#T# (1.6) check if the operation is + or -
#T# calculate borders accordingly
#T# noClipNums is a proportion to avoid clipping of numbers in the number line
#T# if the oneOperand number label is too near the resA label, the oneOperand
#T# will be sent to the other side of the axis
#T# yOffP is the proportion of y offset applied when the two arrows would collide
#T# this offset avoids such collision
#T# negTickP is the factor by which the negative side has to surpass the positive
#T# in order to spawn the tick at the negative side rather than the positive
#T# a positive tick is preferable, therefore negTickP is greater than one
#T# twoSign gives the sign of the second operand. This is to allow changing
#T# the direction of the second arrow according to its sign

#T# (1.6.1) in addition and subtraction four cases are considered, 
#T# the total possibilities for the first and second operands to be positive
#T# or negative. This section 1.6.1 applies to both operations (changing the
#T# sign of the twoOperand in subtraction)
#T# yOffset is an offset in y that is only neccessary if the arrows go in
#T# opposite directions, so that they are not drawn in top of each other and clip
#T# This is because the arrow of the oneOperand is always drawn first,
#T# followed by the arrow of the twoOperand.
#T# If the arrow of the twoOperand follows in the opposite direction of oneOperand
#T# it will be drawn on top of the arrow of oneOperand, unless they are separated
#T# in the y axis
#T# tickSign gives the sign of a context tick. This context tick gives a context
#T# of the scale of the graph. It can be 1, 10, 100, 1000, in general a power of 10
#T# (therefore it can also be 0.1, 0.01 etc).
#T# If both operands are positive, the range is between 0 and resA
#T# no need for yOffset (equals 0) because both go in the same direction.
#T# If oneOperand is positive and twoOperand negative, 
#T# as oneOperand is drawn first it will always be the max value, because
#T# twoOperand goes to the other side. The minimum depends on if resA is
#T# under zero or not (as zero must always be included)
#T# in this case offset is neccessary in the y axis as twoOperand goes to the
#T# negative side, the offset is in proportion the the graph size.
#T# If oneOperand is negative and twoOperand zero or positive, 
#T# as oneOperand is drawn first, the min will be oneOperand. The max depends
#T# on if resA gets the result over zero or not
#T# here y offset is neccessary to avoid collision of the arrows.
#T# If both operands are negative,
#T# both arrows point to the negative side. The range is between zero and resA

#T# (1.6.1.1) choose the side of the tick, positive or negative

#T# (1.6.2) amplify the scale to allow ending arrows to the number line
#T# make y axis proportional to the x axis

#T# (1.6.3) give a coat of paint to the graph's parts

#T# (1.6.4) draw the arrow pointing both ways in the number line

#T# (1.6.5) proportionA is just to store the value of the final range size
#T# ordOfMag stores the order of magnitude of the number line, so that a
#T# context tick can be added at a power of ten, 10 to the ordOfMag
#T# the context tick is newTick
#T# in case the newTick gets out of the used number line, a fallbackTick is used

#T# (1.6.6) set the x ticks. The minimum is 0, oneOperand, and resA (twoOperand comes
#T# included within oneOperand and resA, it's the distance between them)
#T# in the case none of the ticks clip, both can be included
#T# if both ticks clip, just don't include any context tick

#T# (1.6.7) finally draw the arrows
#T# if the proportion of oneOperand is too low avoid clipping by sending
#T# it's label to the other side. Also reduce the size of the arrow head
#T# otherwise if oneOperand is too low the arrow head would look gigantic
#T# do the same for twoOperand arrow

#T# (1.6.8) save the figure to hard drive (if from CLI) or show it (if from GUI) and return

#T# (1.7) check if the operation is * or /

#T# (1.7.1) no matter the quadrant in which the result falls, in all 4 quadrants the
#T# used interval in each axis is between 0 and the operand of that axis
#T# change xMultDiv, yMultDiv, and areaMD so that the same code can graph both
#T# division and multiplication

#T# (1.7.2) amplify both scales to allow ending arrows to the axes
#T# as the rectangle formed by * and / always starts at the origin,
#T# deltaAxesA is the extra interval size that both axes will get

#T# (1.7.3) graph and put each part in its place

#T# (1.7.4) graph the axes arrows

#T# (1.7.5) calculate order of mag

#T# (1.7.6) put the context ticks in the x axis
#T# totalNewTicksX stores the max amount of extra x ticks to add,
#T# totalFallTicksX stores the max amount of extra fallback x ticks to add
#T# ticksX stores the tick marks for the x axis
#T# to use ticks in the order of mag of x, the distance from xMultDiv to newTickX
#T# must be greater or equal to a newTickX.
#T# Sort the ticks and remove the ones too close

#T# (1.7.7) put the y ticks in a similar fashion to addition and subtraction

#T# (1.7.8) add unique parts for these operations * and /
#T# add pseudo tick marks with annotations (twiny() is buggy for this)
#T# va is vertical alignment. Change va according to the sign of y
#T# distanceLblP for distance label proportion is a proportion for the
#T# tick labels in the second x axis, so they don't clip inside the axis

#T# (1.7.9) according to the quadrant, change the side of the ticks

#T# (1.7.10) draw the rectangle

#T# (1.7.11) save to disk or show in GUI, then return


#T# (1)
def makegraph(opStr,fmtStr):
    """
opStr is for operation string, it's the string with the operation to be
graphed, e.g. "1+1" or "3*2.5" or "-532+42" etc.

fmtStr is for format string, it's the string with the format to apply to
the graph. Example with matplotlib styles "STYLE:seaborn"
    """
#T# (1.1)
    arrowKwargs = {'length_includes_head':True}

#T# (1.2)
    validOp = re.match('(-?\d+\.?\d*)([+\-*/])(-?\d+\.?\d*)',opStr)
    if validOp is None and cA.GUIUSE is False:
        print(cA.WR1.fill("Error5: The operation (in the first argument) lacks one of its parts. \
It must strictly be a number followed by an operation and then another number. \
The numbers can be decimal and negative. Decimal is indicated by a dot . and negative is indicated by a hyphen -"),file=sys.stderr)
        exit(5)
    elif validOp is None and cA.GUIUSE is True:
        pass #T# TODO: implement GUI

#T# (1.3)
    if fmtStr is not "":
        try:
            plt.style.use(fmtStr)
        except:
            print("format string is written incorrectly. Please check the spelling.",file=sys.stderr)
            exit(7)

#T# (1.4)
    oneOperand = float(validOp.group(1))
    symbolOp = validOp.group(2)
    twoOperand = float(validOp.group(3))
    

#T# (1.5)
    kScale = 1.2
    noClipP = 0.07
    
    #T# (1.6)
    if symbolOp == '+' or symbolOp == '-':
        noClipNums = 0.2
        yOffP = 0.02
        negTickP = 1.4
        twoSign = 1
        #T# (1.6.1)
        if symbolOp == '+':            
            resA = oneOperand + twoOperand
            if oneOperand >= 0 and twoOperand >= 0:
                cA.xAmin = min(0,resA)
                cA.xAmax = max(0,resA)
                yOffset = 0
                tickSign = 1
            elif oneOperand >= 0 and twoOperand < 0:
                cA.xAmin = min(0,resA)
                cA.xAmax = max(0,oneOperand)
                yOffset = yOffP*(cA.xAmax-cA.xAmin)
                #T# (1.6.1.1)
                if resA >= 0:
                    tickSign = 1
                elif resA < 0:
                    if abs(resA)/abs(oneOperand) >= negTickP:
                        tickSign = -1
                    else:
                        tickSign = 1
            elif oneOperand < 0 and twoOperand >= 0:
                cA.xAmin = min(0,oneOperand)
                cA.xAmax = max(0,resA)
                yOffset = yOffP*(cA.xAmax-cA.xAmin)
                if resA < 0:
                    tickSign = -1
                elif resA >= 0:
                    if abs(oneOperand)/abs(resA) >= negTickP:
                        tickSign = -1
                    else:
                        tickSign = 1
            elif oneOperand < 0 and twoOperand < 0:
                cA.xAmin = min(0,resA)
                cA.xAmax = max(0,resA)
                yOffset = 0
                tickSign = -1
        
        #T# (1.6.1)
        elif symbolOp == '-':
            resA = oneOperand - twoOperand
            twoSign = -1
            if oneOperand >= 0 and twoOperand >= 0:
                cA.xAmin = min(0,resA)
                cA.xAmax = max(0,oneOperand)
                yOffset = yOffP*(cA.xAmax - cA.xAmin)
                #T# (1.6.1.1)
                if resA >= 0:
                    tickSign = 1
                elif resA < 0:
                    if abs(resA)/abs(oneOperand) >= negTickP:
                        tickSign = -1
                    else:
                        tickSign = 1
            elif oneOperand >= 0 and twoOperand < 0:
                cA.xAmin = min(0,resA)
                cA.xAmax = max(0,resA)
                yOffset = 0
                tickSign = 1
            elif oneOperand < 0 and twoOperand >= 0:
                cA.xAmin = min(0,resA)
                cA.xAmax = max(0,resA)
                yOffset = 0
                tickSign = -1
            elif oneOperand < 0 and twoOperand < 0:
                cA.xAmin = min(0,oneOperand)
                cA.xAmax = max(0,resA)
                yOffset = yOffP*(cA.xAmax - cA.xAmin)
                if resA < 0:
                    tickSign = -1
                elif resA >= 0:
                    if abs(oneOperand)/abs(resA) >= negTickP:
                        tickSign = -1
                    else:
                        tickSign = 1

        #T# (1.6.2)
        tmpxAmin = ((kScale + 1)*cA.xAmin + (-kScale + 1)*cA.xAmax)/2
        tmpxAmax = ((-kScale + 1)*cA.xAmin + (kScale + 1)*cA.xAmax)/2
        cA.xAmin = tmpxAmin
        cA.xAmax = tmpxAmax
        cA.yAmax = (cA.xAmax-cA.xAmin)/15
        cA.yAmin = -cA.yAmax

        fig1, ax1 = plt.subplots()
        ax1.axis([cA.xAmin,cA.xAmax,cA.yAmin,cA.yAmax])
        #T# (1.6.3)
        ax1.set_aspect('equal')
        ax1.yaxis.set_visible(False)
        for direc in ['top','left','right']:
            ax1.spines[direc].set_visible(False)
        ax1.spines['bottom'].set_position('zero')
        ax1.tick_params(length=14,direction="inout")

        #T# (1.6.4)
        ax1.annotate("",xy=(cA.xAmin,0),xytext=(cA.xAmax,0),arrowprops={'arrowstyle':"<->",'shrinkA':0,'shrinkB':0})

        #T# (1.6.5)
        proportionA = (cA.xAmax-cA.xAmin)
        ordOfMag = math.floor((math.log10(max(abs(oneOperand),abs(resA)))))
        newTick = tickSign*10**ordOfMag
        fallbackTick = tickSign*10**(ordOfMag-1)

        #T# (1.6.6) 
        if abs(newTick-oneOperand)*kScale/proportionA >= noClipP and abs(newTick-resA)*kScale/proportionA >= noClipP and abs(newTick-0)*kScale/proportionA >= noClipP:
            if abs(fallbackTick-oneOperand)*kScale/proportionA >= noClipP and abs(fallbackTick-resA)*kScale/proportionA >= noClipP and abs(fallbackTick-0)*kScale/proportionA >= noClipP:
                ax1.set_xticks([0,oneOperand,resA,newTick,fallbackTick])
            else:
                ax1.set_xticks([0,oneOperand,resA,newTick])
        elif abs(fallbackTick-oneOperand)*kScale/proportionA >= noClipP and abs(fallbackTick-resA)*kScale/proportionA >= noClipP and abs(fallbackTick-0)*kScale/proportionA >= noClipP:
            ax1.set_xticks([0,oneOperand,resA,fallbackTick])
        else:
            ax1.set_xticks([0,oneOperand,resA])

        #T# (1.6.7)
        widthArrow = 0.01*proportionA
        if abs(oneOperand)*kScale/proportionA <= noClipNums:
            ax1.xaxis.get_majorticklabels()[1].set_y(0.08*proportionA)
            expK = 20*abs(oneOperand)*kScale/proportionA
            ax1.arrow(0,yOffset,oneOperand,0,**arrowKwargs,width=widthArrow,head_width=expK*widthArrow,head_length=1.2*expK*widthArrow)
        else:
            ax1.arrow(0,yOffset,oneOperand,0,**arrowKwargs,width=widthArrow)
        if abs(twoOperand)*kScale/proportionA <= noClipNums:
            ax1.xaxis.get_majorticklabels()[1].set_y(0.08*proportionA)
            expK = 20*abs(twoOperand)*kScale/proportionA
            ax1.arrow(oneOperand,-yOffset,twoSign*twoOperand,0,**arrowKwargs,width=widthArrow,head_width=expK*widthArrow,head_length=1.2*expK*widthArrow)
        else:
            ax1.arrow(oneOperand,-yOffset,twoSign*twoOperand,0,**arrowKwargs,width=widthArrow)

        #T# (1.6.8)
        if cA.GUIUSE is False:
            plt.show()
            #fig1.savefig("DebugFig1")
        elif cA.GUIUSE is True:
            plt.show() #T# TODO: or something similar, depends on TkInter
        return

    #T# (1.7)
    elif symbolOp == '*' or symbolOp == '/':
        #T# (1.7.1)
        if symbolOp == '*':
            resA = oneOperand*twoOperand
            cA.xAmin = min(0,oneOperand)
            cA.xAmax = max(0,oneOperand)
            cA.yAmin = min(0,twoOperand)
            cA.yAmax = max(0,twoOperand)

            xMultDiv = oneOperand
            yMultDiv = twoOperand
            areaMD = resA
            if xMultDiv >= 0:
                tickSignX = 1
            else:
                tickSignX = -1
            if yMultDiv >= 0:
                tickSignY = 1
            else:
                tickSignY = -1

        #T# (1.7.1)
        elif symbolOp == '/':
            resA = float(Decimal(str(oneOperand))/Decimal(str(twoOperand)))
            cA.xAmin = min(0,resA)
            cA.xAmax = max(0,resA)
            cA.yAmin = min(0,twoOperand)
            cA.yAmax = max(0,twoOperand)

            xMultDiv = resA
            yMultDiv = twoOperand
            areaMD = oneOperand
            if xMultDiv >= 0:
                tickSignX = 1
            else:
                tickSignX = -1
            if yMultDiv >= 0:
                tickSignY = 1
            else:
                tickSignY = -1
        
        #T# (1.7.2)
        deltaAxesA = max(abs(xMultDiv),abs(yMultDiv))*(kScale-1)/2
        if xMultDiv >= 0 and yMultDiv >=0:
            cA.xAmax = xMultDiv + deltaAxesA
            cA.xAmin = -deltaAxesA
            cA.yAmax = yMultDiv + deltaAxesA
            cA.yAmin = -deltaAxesA
        elif xMultDiv >= 0 and yMultDiv < 0:
            cA.xAmax = xMultDiv + deltaAxesA
            cA.xAmin = -deltaAxesA
            cA.yAmax = deltaAxesA
            cA.yAmin = yMultDiv - deltaAxesA
        elif xMultDiv < 0 and yMultDiv >= 0:
            cA.xAmax = deltaAxesA
            cA.xAmin = xMultDiv - deltaAxesA
            cA.yAmax = yMultDiv + deltaAxesA
            cA.yAmin = -deltaAxesA
        elif xMultDiv < 0 and yMultDiv < 0:
            cA.xAmax = deltaAxesA
            cA.xAmin = xMultDiv - deltaAxesA
            cA.yAmax = deltaAxesA
            cA.yAmin = yMultDiv - deltaAxesA
        
        fig1, ax1 = plt.subplots()
        #T# (1.7.3)
        ax1.axis([cA.xAmin,cA.xAmax,cA.yAmin,cA.yAmax])
        ax1.set_aspect('equal')
        for direc in ['top','right','left','bottom']:
            ax1.spines[direc].set_visible(False)
        ax1.spines['bottom'].set_position('zero')
        ax1.spines['left'].set_position('zero')
        ax1.spines['right'].set_position('zero')
        ax1.spines['top'].set_position('zero')
        ax1.tick_params(length=14,direction="inout")
        ax1.grid(b=True,which='both')
        
        proportionAX = (cA.xAmax-cA.xAmin)
        proportionAY = (cA.yAmax-cA.yAmin)
        #T# (1.7.4)
        ax1.annotate("",xy=(cA.xAmin,0),xytext=(cA.xAmax,0),arrowprops={'arrowstyle':"<->",'shrinkA':0,'shrinkB':0,'alpha':0.55})
        ax1.annotate("",xy=(0,cA.yAmin),xytext=(0,cA.yAmax),arrowprops={'arrowstyle':"<->",'shrinkA':0,'shrinkB':0,'alpha':0.55})

        #T# (1.7.5)
        ordOfMagX = math.floor(math.log10(abs(xMultDiv)))
        newTickX = tickSignX*10**ordOfMagX
        fallbackTickX = tickSignX*10**(ordOfMagX-1)
        ordOfMagY = math.floor(math.log10(abs(yMultDiv)))
        newTickY = tickSignY*10**ordOfMagY
        fallbackTickY = tickSignY*10**(ordOfMagY-1)
        
        #T# (1.7.6)
        totalNewTicksX = math.floor(xMultDiv/newTickX)
        totalFallTicksX = math.floor(xMultDiv/fallbackTickX)
        ticksX = [float(Decimal(str(xMultDiv)))]
        if abs(newTickX-xMultDiv) >= abs(newTickX) and abs(newTickX-0)*kScale/proportionAX >= noClipP:
            for ti1 in range(1,totalNewTicksX+1):
                ticksX.append(float(Decimal(str(ti1))*Decimal(str(newTickX))))
                if tickSignX >= 0:
                    ticksX.sort()
                elif tickSignX < 0:
                    ticksX.sort(reverse=True)
                if abs(ticksX[ti1]-ticksX[ti1-1])*kScale/proportionAX < noClipP:
                    ticksX.remove(ticksX[ti1-1])
            ax1.set_xticks(ticksX)
        elif abs(fallbackTickX-xMultDiv)*kScale/proportionAX >= noClipP and abs(fallbackTickX-0)*kScale/max(proportionAX,proportionAY) >= noClipP:
            for ti1 in range(1,totalFallTicksX+1):
                ticksX.append(float(Decimal(str(fallbackTickX))*Decimal(str(ti1))))
                if tickSignX >= 0:
                    ticksX.sort()
                elif tickSignX < 0:
                    ticksX.sort(reverse=True) 
                if abs(ticksX[ti1]-ticksX[ti1-1])*kScale/proportionAX < noClipP:
                    ticksX.remove(ticksX[ti1-1])
            ax1.set_xticks(ticksX)
        else:
            ax1.set_xticks(ticksX)

        #T# (1.7.7)
        if abs(newTickY-yMultDiv)*kScale/proportionAY >= noClipP and abs(newTickY-0)*kScale/proportionAY >= noClipP:
            if abs(fallbackTickY-yMultDiv)*kScale/proportionAY >= noClipP and abs(fallbackTickY-0)*kScale/proportionAY >= noClipP:
                ax1.set_yticks([0,yMultDiv,newTickY,fallbackTickY])
            else:
                ax1.set_yticks([0,yMultDiv,newTickY])
        elif abs(fallbackTickY-yMultDiv)*kScale/proportionAY >= noClipP and abs(fallbackTickY-0)*kScale/proportionAY >= noClipP:
            ax1.set_yticks([0,yMultDiv,fallbackTickY])
        else:
            ax1.set_yticks([0,yMultDiv])
        
        #T# (1.7.8)
        ax1.axhline(y=yMultDiv,alpha=0.6,linewidth=1)
        if tickSignY >= 0:
            va = 'bottom'
        elif tickSignY < 0:
            va = 'top'    
        distanceLblP = 0.05
        for tickX in ticksX:
            plotTickX = float(Decimal(str(tickX))*Decimal(str(yMultDiv)))
            ax1.annotate(f"{plotTickX}",xy=(tickX,yMultDiv-distanceLblP*tickSignY*proportionAY),xytext=(tickX,yMultDiv+distanceLblP*tickSignY*proportionAY),horizontalalignment='center',verticalalignment=va,rotation=90,arrowprops={'arrowstyle':"-",'shrinkA':0,'shrinkB':0})
        plt.xticks(rotation=90)
        #T# (1.7.9)
        if xMultDiv >= 0 and yMultDiv < 0:
            ax1.xaxis.tick_top()
            plt.xticks(rotation=90)
        elif xMultDiv < 0 and yMultDiv >= 0:
            ax1.yaxis.tick_right()
            plt.xticks(rotation=90)
        elif xMultDiv < 0 and yMultDiv < 0:
            ax1.xaxis.tick_top()
            ax1.yaxis.tick_right()
            plt.xticks(rotation=90)
        #T# (1.7.10)
        rec1 = plt.Rectangle((0,0),xMultDiv,yMultDiv,alpha=0.8)
        ax1.add_patch(rec1)
        #T# (1.7.11)
        if cA.GUIUSE is False:
            #fig1.savefig("DebugFig1")
            plt.show()
        if cA.GUIUSE is True:
            plt.show()
        return

    return