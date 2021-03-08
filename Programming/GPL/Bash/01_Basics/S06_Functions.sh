
#   Functions

#T# Table of contents

#C# Function definition
#C# Function call
#C# Scope
#C# Recursion

#T# Beginning of content

#C# Function definition

# |-------------------------------------------------------------
#T# functions are defined just with its name and empty parentheses, no parameters, no return value, they are called with arguments to calculate and return the exit status of the function

#T# the function definition starts with the function keyword, but this keyword is optional, the bare minimum is either the name of the function and the empty parentheses, or the function keyword followed by the function name, no parentheses

#T# the function execution can occur in the current shell context (with braces {}), or in a subshell (with parentheses ())

# SYNTAX function definition, current shell context, name and parentheses alone, passed arguments, exit status
# func1() {
#     statements1
#     positional_parameter1
#     return exit_status1
# }
#T# func1 is the function name, statements1 are executed when func1 is called, and then exit_status1 is returned from the function as its exit status (this can only be an integer)

#T# the passed arguments to the function are identified via positional parameters (variables), $0, $1, $2, and so on, their use inside func1 is represented with positional_parameter1, $0 is the name of the script or program executing the function, $1 is the first argument, $2 is the second argument, and so on

func1() {
    echo "func1 executed in current shell"
    return 37 # this exit status represents an error, only exit status 0 represents correct execution
}
func1 # func1 executed in current shell # $? == 37

# SYNTAX function definition, subshell execution, function keyword and function name alone
# function func1
# (
#     statements1
# )
#T# same as before, but this executes statements1 inside a subshell when func1 is called, the opening parenthesis must be in a newline after the function name

function func1
(
    echo "func1 executed in subshell"
)
func1 # func1 executed in subshell # $? == 0

#T# there is a third syntax to declare a function, it's without braces or parentheses, because the body of a function can consist of control flow statements (see S05_Control_flow.sh)

# SYNTAX function definition with control flow statement
# func1() control_flow1
#T# control_flow1 is the body of func1, control_flow1 can be any of, an if construct, a case statement, a for loop, a while loop, an until loop, and a select loop

#T# this doesn't have to be a one-liner, but it can only be one control flow statement

func1() if [ $1 == "arg1" ]; then echo "with $1, $2, and $3"; fi

#T# the name of a function can be accessed from inside the function by using the FUNCNAME special variable (parameter)
func1() { echo "the function name is $FUNCNAME"; }
func1 # the function name is func1
# |-------------------------------------------------------------

#C# Function call

# |-------------------------------------------------------------
#T# a function is called directly, its arguments use no parentheses nor commas, there can be more or less arguments than those used inside the function
func1() if [ $1 == "arg1" ]; then echo "with $1, $2, and $3"; fi
func1 arg1 arg2 arg3 arg4 arg5 # with arg1, arg2, and arg3

#T# in Bash, functions are not really first class citizens, still, the name of a function can be assigned to a variable, and expanding that variable will call the function
var1=func1
$var1 arg1 # with arg1, , and
# |-------------------------------------------------------------

#C# Scope

# |-------------------------------------------------------------
#T# variables (parameters) inside a function are treated with global scope if the function is defined with braces (the function executes in the current shell), and variables are treated with local scope if the function is defined with parentheses (executed in a subshell)

#T# local scope can be achieved regardless of the use of braces or parentheses with the local command

# SYNTAX local scope variables inside functions
# func1() {
#     local -o1 var1
#     statements1
# }
#T# var1 can be used inside func1 in statements1, and the value of var1 won't become part of the executing shell, -o1 is a flag passed to the local command, the flags accepted by the local command are the same as those of the declare command (see S02_Data_types.sh)

var1=5
function func1
{
    local var1=261
}
func1
echo $var1 # 5
# |-------------------------------------------------------------

#C# Recursion

# |-------------------------------------------------------------
#T# recursion allows calling a function from inside itself

# SYNTAX function recursion
# func1() {
#     statements1
#     func1 args1
#     return exit_status1
# }
#T# same as before, but func1 is called inside func1 with arguments args1, statements1 must ensure that there is a way to stop calling func1, so that recursion stops

var1=0
recursion_func1() {
    if [[ $1 -ge 0 ]]; then
        let "var1 += 1"
        recursion_func1 $(( $1 - 1 ))
    fi
}
recursion_func1 3
echo $var1 # 4
# |-------------------------------------------------------------