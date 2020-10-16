
#   Operators

#T# Arithmetics with $(()), *, +, **, -, /, %
A=3
B=$(((6 * (${A} + 5)) ** 2))
C=404
D=$((((${C} - 4)/100) % 27))
echo -e "${B}\n${D}"

#T# assignment operators with let "var = 4"
let "A = 2"
echo "A value is: $A"
let "A += 3"
echo "A value is: $A"
let "A -= 4"
echo "A value is: $A"
let "A *= 8"
echo "A value is: $A"
let "A /= 2"
echo "A value is: $A"

#T# let, declare keywords, expr command