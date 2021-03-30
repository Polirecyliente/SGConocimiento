
#   Pandoc

#T# Table of contents

#C# Basic usage
#C# General flags and kwargs
#C# Inserting images
#C# Pandoc Lua filters

#T# Beginning of content

# |-------------------------------------------------------------
#T# the pandoc program is used to change the format of a file, from a format in a set of input formats, to another format in a set of output formats

#T# by default, pandoc converts Markdown files into HTML files, but specifying formats in the file names, attempts to convert from the format of the input file to the format of the output file

#T# if no output file is given, output is sent to stdout
# |-------------------------------------------------------------

#C# Basic usage

# |-------------------------------------------------------------
#T# the following command turns input_file1.md into output_file1.pdf
# SYNTAX pandoc input_file1.md -o output_file1.pdf
# |-------------------------------------------------------------

#C# General flags and kwargs

# |-------------------------------------------------------------
#T# with a given input, if the output is a plain text format, then Pandoc only outputs the bare minimum plain text necessary to convert from the input format to the output format, which commonly is not a complete, standalone file in the output format

#T# the create a standalone file in the output format, the -s flag is used
# SYNTAX pandoc -s input_file1.md -o output_file1.html

cat file1 # word1

pandoc file1 # <p>word1</p>

pandoc -s file1
#T# the former prints
# [WARNING] This document format requires a nonempty <title> element.
#   Please specify either 'title' or 'pagetitle' in the metadata,
#   e.g. by using --metadata pagetitle="..." on the command line.
#   Falling back to 'file1'
# <!DOCTYPE html>
# <html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
# <head>
#   <meta charset="utf-8" />
#   <meta name="generator" content="pandoc" />
#   <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
#   <title>file1</title>
#   <style type="text/css">
#       code{white-space: pre-wrap;}
#       span.smallcaps{font-variant: small-caps;}
#       span.underline{text-decoration: underline;}
#       div.column{display: inline-block; vertical-align: top; width: 50%;}
#   </style>
# </head>
# <body>
# <p>word1</p>
# </body>
# </html>

#T# the --version flag outputs information like the user data directory, which is where Pandoc searches for files, like templates, by default
pandoc --version

#T# the --list-highlight-languages is used to output the list of programming languages with syntax highlighting available
pandoc --list-highlight-languages

#T# the --number-sections flag is used to make numbered sections, the default numbering pattern for sections and subsections is 1, 1.1, 1.1.1, 1.1.1.1, etcetera, in HTML, the number of a section is placed inside a <span class="header-section-number"> tag -->
pandoc file1.md -s --number-sections -o file1.html

#T# the --toc flag is used to include a table of contents in the output file
pandoc file1.md -s --toc -o file1.html
# |-------------------------------------------------------------

#C# Inserting resources

# |-------------------------------------------------------------
#T# when the input file contains resources such as images, referenced with relative paths, the --resource-path kwarg is used to specify the path or paths (path1, path2, etcetera) where the resources will be searched for
# SYNTAX pandoc --resource-path path1:path2 input_file1.md -o output_file1.pdf
pandoc --resource-path Math/:Science/dir1/ input_file1.md -o output_file1.pdf
# |-------------------------------------------------------------

#C# Pandoc Lua filters

# |-------------------------------------------------------------
#T# Lua filters for Pandoc, are applied with the --lua-filter kwarg
pandoc --lua-filter file1.lua input_file1.md -o output_file1.pdf

#T# several filters can be applied, from left to right one after the other
pandoc --lua-filter file1.lua --lua-filter file2.lua input_file1.md -o output_file1.pdf

#T# for information about how to create Lua filters, see /path/to/SGConocimiento/Programming/GPL/Lua/02_Applied/S01_Pandoc_filters.lua
# |-------------------------------------------------------------