import textwrap

#T# use a TextWrapper object to use textwrap.fill() to avoid breaking words and join with newlines
WR1 = textwrap.TextWrapper(width=78)

#T# flag to know where CLI or GUI was picked
GUIUSE = False

#T# vars to set min and max values in x and y axes
xAmin = 0
xAmax = 0
yAmin = 0
yAmax = 0