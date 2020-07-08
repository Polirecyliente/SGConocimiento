#!/bin/bash
#   Arrays

#T# Array initialization, length of array #Arr[@], all elements Arr[@]
Arr1=( elem1 elem2 elem3 "elem 4" )
Arr2[3]=el3
echo -e "Length of Arr1: ${#Arr1[@]}\nElement3 in Arr2: ${Arr2[3]}"
echo "Elements in Arr1: ${Arr1[@]}"