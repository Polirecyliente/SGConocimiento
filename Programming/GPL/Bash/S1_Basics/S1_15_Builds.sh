
#   Builds

#T# Table of contents

#C# Build approximation

#T# Beginning of content

#C# Build approximation

# |-------------------------------------------------------------
#T# Bash always executes commands line by line, there is no intermediate compilation, so that even if the same command is repeated, it is parsed from zero, each time

#T# a set of scripts that form a project can't be built into a single executable file, but one way to approximate this behavior would be to paste all the individual scripts into a single file, and make executable this file of the whole project
# |-------------------------------------------------------------