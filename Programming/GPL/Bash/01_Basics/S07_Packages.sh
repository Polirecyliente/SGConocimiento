
#   Packages

#T# Table of contents

#C# Importing packages
#C# Package creation

#T# Beginning of content

#C# Importing packages

# |-------------------------------------------------------------
#T# a package is imported with the source command applied to each sh file in the package
# SYNTAX source /path/to/package1/file1.sh
# |-------------------------------------------------------------

#C# Package creation

# |-------------------------------------------------------------
#T# packages are not really supported in Bash, so they can only be mimicked

# SYNTAX function package1::func1() { statements1 }
#T# this creates a function named package1::func1, but no actual package, also the colon : is not a POSIX allowed char to name a function
function package1::func1() { echo "str1"; }
package1::func1 # str1

# |--------------------------------------------------\
#T# the file system hierarchy can still be used to create packages of Bash code

# SYNTAX file system hierarchy
# package1
# -- main.sh
# -- subpackage1
# -- -- subp1_funcs1.sh
# -- subpackage2
# -- -- subp2_funcs1.sh

#T# code from subp1_funcs1.sh can be executed from subp2_funcs1.sh by using the source command, or with the bash command

# SYNTAX source ../subpackage1/subp1_funcs1.sh
#T# this executes subp1_funcs1.sh in the same shell environment

# SYNTAX bash ../subpackage1/subp1_funcs1.sh
#T# this executes subp1_funcs1.sh in a subshell environment
# |--------------------------------------------------/

# |-------------------------------------------------------------