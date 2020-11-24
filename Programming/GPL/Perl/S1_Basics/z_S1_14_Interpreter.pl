
#   Interpreter

#T# Table of contents

#C# Interpreter customization
#C# --- Interpreter options

#T# Beginning of content

#C# Interpreter customization

# |-------------------------------------------------------------

#C# --- Interpreter options

# |-----
#T# the interpreter can have several options set at the start

# SYNTAX perl -o1 -o2 val2
#T# this must be executed outside Perl, in the operating system shell, -o1 is optional, it's the flag being turned on, the flags that modify the options of the interpreter are set before starting it, -o2 val2 is an optional kwarg pair, perl is the Perl interpreter

#T# -o1 and -o2 val2 can be one of the following
#T#     -e 'command_string1', makes Perl execute command_string1, so command_string1 must have valid Perl syntax
# |-----

# |-------------------------------------------------------------