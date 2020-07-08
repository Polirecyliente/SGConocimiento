#!/bin/bash
#   Functions

#T# function, local, return
function funA()
{
    local A=5
    A=$((${A} + 6))
    echo ${A}
    return 0
}
B=$(funA)
echo ${B}