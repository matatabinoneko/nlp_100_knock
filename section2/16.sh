#!/bin/bash
l=`wc -l list.txt | awk '{print $1}'`

l=l/$1
echo $l

# split -l l hightemp.txt split