#!/bin/bash
# Author: Milesh B
# Github: https://github.com/milesh-b
# Bash script to calculate a Vanilla Put option.
# Execute in terminal chmod u+x *.sh
# Demo: ./Euro_Binomial.sh 144 0.315573 0.19062 144 0 1.5 97 50000
# Value of option=  6.49818
# Input the following parameters separated by spaces:
# s0 vol r x div time tree sim

echo "You have inputted the following parameters:"
echo "s0= ${1}"
echo "vol= ${2}"
echo "r= ${3}"
echo "x= ${4}"
echo "div= ${5}"
echo "time= ${6}"
echo "tree= ${7}"
echo "sim= ${8}"

awk -f Binomial.awk -v s0=$1 -v vol=$2 -v r=$3 -v x=$4 -v div=$5 -v time=$6 -v tree=$7 -v sim=$8 -v seed=$RANDOM
