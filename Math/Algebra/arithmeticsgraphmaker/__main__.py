#    Arithmetics Graph Maker: makes basic arithmetics graphs
#    Copyright (C) 2020  Julian Dario Tovar Roa
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


#T#T#T Start

#T# main imports
import sys, getopt

#T# imports from other files in the program itself
import interfaces as intF
import constantsAGM as cA

#T# get the command line arguments
argvMain = sys.argv
argvMain = argvMain[1:]

#T# use "def main()" to allow this program to be used as a module
def main(argvMainA):

#T#T#T check if the help flag is present
    try:
        optsA,argsA = getopt.getopt(argvMainA,"ho:f:",["help","gui","GUI"])
    except getopt.GetoptError as err1:
        print(cA.WR1.fill(f"Error2: there is something wrong with the options passed to the program. Check the spelling. {err1}"),file=sys.stderr)

#T# exit if there was an error in the flags
        exit(2)

    opers = None
    fmtA = ""
    for opti,vali in optsA:

#T# if the help flag is present, print help to the console and exit
        if opti == "-h" or opti == "--help":
            print(
"""Arithmetics Graph Maker (or AGM) is a program that makes graphs from 
arithmetic operations: addition, subtraction, multiplication, and division.

AGM can be executed in a GUI (Graphical User Interface), or in a CLI 
(Command Line Interface)


-----GUI Execution-----
To execute AGM in a GUI run the program with the GUI flag. For example: in
a shell (e.g. Bash) type arithmeticsgraphmaker --GUI, or 
arithmeticsgraphmaker --gui

-----CLI Execution-----
To execute AGM in a CLI you must pass 2 flags (the second is optional):

    1. A string with the operations to be graphed, after the -o flag,
    (-o for operation) for instance:
        -o "3+2, 12*23, 62-129"
    Double quotes are important to allow spaces inside the array.
    Each operation is separated from the others with commas.

    2. Either a single string with a matplotlib style name, or an array of
    eleven strings with the format to apply to eleven parts of the graph.
    Each string uses Python syntax, and only valid matplotlib parameters may
    be used. This argument is optional, if omitted the default style will be
    used. This argument is written with the -f flag (-f for format).

    Example of a style being used:
        -f "STYLE:seaborn"
    As seen from the example, if a style is going to be used, the string must
    start with the word STYLE in capitalized letters followed by a colon, and
    then the name of the matplotlib style. You can search for all the 
    available styles in the matplotlib documentation, but for your reference,
    here is the list of styles at the moment of the most recent update of 
    this program: '_classic_test', 'bmh', 'classic', 'dark_background', 
    'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 
    'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 
    'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 
    'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 
    'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 
    'seaborn-whitegrid', 'Solarize_Light2', 'tableau-colorblind10'

    Example of an array of strings with formats:
        -f "(format1),(format2),(format3)"
    As the example shows, each format string is enclosed in parentheses, and
    separated with commas. The outer double quotes are mandatory.
    Also from the example, only 3 formats are input to the program. It's not
    necessary to fill the 11 format strings, any of them can be left empty,
    or even all of them can be empty (in that case the default style is used)

    The format strings follow a specific order:
      First: the format to the addend arrow, as written in the keyword
      arguments inside the parentheses of a pyplot.arrow()
      Second: the format to the subtrahend arrow, as inside of a 
      pyplot.arrow()
      Third: the format of the area formed by multiplication or division,
      as inside of a pyplot.Rectangle()
      Fourth: the format of the major grid in the x axis, as inside of an
      axes.Axes.grid()
      Fifth: the format of the major grid in the y axis, as inside of an 
      axes.Axes.grid()
      Sixth: the format of the minor grid in the x axis, as inside of an
      axes.Axes.grid()
      Seventh: the format of the minor grid in the y axis, as inside of an
      axes.Axes.grid()
      Eighth: the format of the title of the graph, as inside of an
      axes.Axes.set_title()
      Ninth: the format of the lower x axis label, as inside of an
      axes.Axes.set_xlabel()
      Tenth: the format of the upper x axis label, as inside of an
      axes.Axes.set_xlabel()
      Eleventh: the format of the y axis label, as inside of an
      axes.Axes.set_ylabel()

    If all this last information looks confusing it may be better to use the
    matplotlib styles as they are beautiful on their own, or use the GUI.

    Final example about how to use AGM in a CLI:
        arithmeticsgraphmaker -o "2*5,29-42" -f "(),(width=0.2,alpha=0.7)"
    In this example, two operations will be graphed, namely 2*5, and 29-42.
    The format string array only affects the subtrahend arrow, because the
    first format string has been left void as there is nothing inside the
    parentheses. The rest of the parts of the graphs will use the default
    style.""")
            exit(0)

#T# choose between CLI and GUI with the command options
        elif opti == "--gui" or opti == "--GUI":

            cA.GUIUSE = True
#T# send to GUI_AGM.py file
            intF.guiMain()
            print("AGM ended in GUI")
            exit(0)
        elif opti == '-o':
            opers = vali
        elif opti == '-f':
            fmtA = vali

#T# send to CLI_AGM.py file
    if opers is None:
        print(cA.WR1.fill("Error3: To use this program in the command line, either one or two \
flags must be provided, check that you have at least the obligatory flag written in the command line: the obligatory flag -o (for operation) with an argument to know the operations to graph, \
and the optional flag -f (for format) with an argument to know the format of the graph. If you intended to use this program \
in a GUI use the --gui or --GUI flag. See the help for more \
information, by executing this program with the -h or --help flag."),file=sys.stderr)
        exit(3)
        
    cA.GUIUSE = False
    intF.cliMain(opers,fmtA)
    print("AGM ended in CLI")
    exit(0)

if __name__ == "__main__":
    main(argvMain)