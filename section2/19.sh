#!/bin/bash
cut -f 1 hightemp.txt |sort -r | uniq -c |sort -k 1 -r
