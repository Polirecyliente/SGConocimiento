
#   Basic Syntax

#T# macros serve to define values, with macro1 = value1
MACROMAIN = "strMain"

#T# makefiles are written with rules, the parts of a rule are:
#T# target: dependency1 dependency2
#T#		recipe_for_the_shell

#T# there are implicit variables like:
#T# $(CC) is the C compiler name
#T# $(CXX) ix the C++ compiler name
#T# $(CFLAGS) are the flags passed to the compiler
#T# $?, $^ is the dependencies names
#T# $@ is the target name
#T# these implicit variables can be changed as macros, e.g. CC = "gcc"
#T# get all implicit variables with make -p, in a dir without Makefile
makeSection1_1Debug: Section1_1AuxA.cpp Section1_1AuxC.cpp \
Section1_1AuxD.cpp
	$(CXX) $(CFLAGS) $? -o $@

clean:
	$(RM) makeSection1_1Debug Section1_1AuxC.o elseExecDebug

#T# implicit rules start with %.fileExtension
#T# the % percent sign is pattern replaced by any string
#T# this works for example with make Section1_1AuxC.o
%.o: %.cpp
	$(CXX) -c $^ -o $@

#T# conditional directives are:
#T# ifeq (arg1,arg2), ifneq (arg1,arg2), ifdef(arg1), ifndef(arg1),
#T# else, endif
directivesExecDebug: Section1_1AuxA.cpp Section1_1AuxC.cpp \
Section1_1AuxD.cpp
ifeq ($(CXX),'g++')
	$(CXX) $^ -o ifeqExecDebug
else
	g++ $^ -o elseExecDebug
ifndef (Var1)
	Var1=14
	echo "Var1 defined"
endif
endif

#T# include directive, includes other makefiles
#T# make a target in makeFile.mk, e.g. make target1
include make2.mk

#T# override directive, overrides CLI var given to make
override VarCLI := "strMake"
PHONY:
	echo "VarCLI is $(VarCLI)"

#T# the following is run in a shell environment
#T# make executes targets with make targetName, common targets are
#T# install, all
#T# make install
#T# make all