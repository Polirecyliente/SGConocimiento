
#   System calls

#T# Table of contents

#C# File input output
#C# --- Piping and redirection

#T# Beginning of content

#C# File input output

# |-------------------------------------------------------------

#C# --- Piping and redirection

# |-----
#T# 

# |-----

# |-------------------------------------------------------------





# trapping operating system signals, trap -l (lists the operating system signals)

#T# job control for foreground and background processes, ampersand & to start an asynchronous script or command as a background process vs semicolon ; to start processes synchronously, the vertical line | pipes the output of a command as input of another
# && and || in piping commands, the exit command to quit the current script or interpreter session

# the syntax to read a file line by line 'while read -r line1; do echo $line1; done < file1', or 'file1 output | while read line1...'