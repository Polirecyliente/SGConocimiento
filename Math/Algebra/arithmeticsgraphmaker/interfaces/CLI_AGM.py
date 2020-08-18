import re
import sys

import subroutines as subR
import constantsAGM as cA

#T#T#T Get arguments
def cliMain(opsArg,formatArg):

#T#T#T check if opsArg is well formed
    wrongChar = re.search('([^.\d,+\-*/])',opsArg)
    if wrongChar is not None:
        print(cA.WR1.fill("Error4: The first argument, the string of operations is misconstructed. \
Only numbers, the comma, and the four operation symbols + - * / are allowed. "),file=sys.stderr)
        print(cA.WR1.fill(f"The first wrong charater is '{wrongChar.group(1)}' at position {wrongChar.start(1)+1}"),file=sys.stderr)
        exit(4)

    a1List = opsArg.split(",")
#T#T#T for each value in a1List execute makegraph()
    for i1 in range(len(a1List)):
        subR.makegraph(a1List[i1],formatArg)
    return