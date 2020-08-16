
#   Python packages

#T# get help and documentation about a module with the pydoc program
# pydoc module1
pydoc itertools

#T# show information about a module with the pip3 program
# pip3 show module1
#T# if it returns nothing the package is not installed
pip3 show alabaster

#T# if the installation of a module gets timeout errors in the download, it may be fixed with the --default-timeout=1000 option
pip3 install --default-timeout=1000 matplotlib