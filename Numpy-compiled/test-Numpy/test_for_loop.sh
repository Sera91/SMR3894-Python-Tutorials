#!/bin/bash
# declare an array called array and define 3 vales
array=( one two three )
for i in "${array[@]}"
do
	echo "$i"
done
