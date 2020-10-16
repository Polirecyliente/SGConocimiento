
#   Data types

#T# Table of contents

#T# Types in general
#T# Numeric types
#T# String types
#T# --- Heredoc
#T# Boolean type
#T# Composite types
#T# --- Lists
#T# --- Tuples
#T# --- Dictionaries
#T# --- Sets
#T# Enum type
#T# Null type
#T# Type casting

#T# Beginning of content

#T# Types in general

# |-------------------------------------------------------------
#T# types are not fully supported, the only considered types are strings and numbers
# |-------------------------------------------------------------

#T# Numeric types

# |-------------------------------------------------------------

# |--------------------------------------------------\
#T# numerical types are
#T#     integer
#T#     octal, with prefix 0
#T#     hexa, with prefix 0x or 0X
#T#     arbitrary base from 1 to 64, with $((base#number))
#T#     float, substituting the bc command using heredoc notation

#T# the following are particular examples, numbers in any non decimal base must be enclosed in an arithmetic expansion
int1=5
int1=$((011))     # 9
int1=$((0x17))    # 23
int1=$((2#10101)) # 21
flo1=$(bc <<< "12.415") # 12.415 # heredoc is explained later in this file
# |--------------------------------------------------/

# |-------------------------------------------------------------

#T# String types

# |-------------------------------------------------------------
#T# strings are created inside quotation symbols, single quotes or double quotes
str1='string one'
str2="string two"

#T# --- Heredoc

# |-----
# |-----

# |-------------------------------------------------------------