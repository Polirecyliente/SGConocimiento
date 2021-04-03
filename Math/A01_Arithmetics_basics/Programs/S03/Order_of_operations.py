#T# the order of operations can be decided to set which operations are done first and which later, and avoid ambiguity about which is the next operation

#T# this is done with grouping or enclosing operators, operations are done first inside these grouping operators, and then outside, so the most inner enclosed operation is done earlier than the others, and the calculations are then performed outwards

#T# the basic grouping operator is the parenthesis pair ()
num1 = ((3 + 4) * 5) + 1 # 36 #| first (3 + 4) is calculated which gives 7, then (7 * 5) is 35, and 35 + 1 is 36

#T# the PEMDAS order of operations is respected
num1 = (3 + 2) ** 2 * 3 / 5 + 6 - 1 # 20.0 #| (3 + 2) is 5, 5 ** 2 is 25, 25 * 3 is 75, 75 / 5 is 15, 15 + 6 is 21, 21 - 1 is 20