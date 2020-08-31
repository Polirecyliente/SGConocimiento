
#   Openpyxl

#T# Table of contents

#T# Basic usage

#T# Beginning of content

# |-------------------------------------------------------------
#T# Openpyxl is a package to read, and write Excel spreadsheet files
# |-------------------------------------------------------------

#T# Basic usage

# |-------------------------------------------------------------
#T# import the whole package, or import specific modules, functions, classes
from openpyxl import Workbook

#T# create a workbook
workbook1 = Workbook()

#T# select the active worksheet (the default one, if none have been created)
worksheet1 = workbook1.active
#T# TODO the active attribute can be used as a function 'active(val1)' but this is to set the active sheet to val1

#T# create new worksheets
# 

# |-------------------------------------------------------------