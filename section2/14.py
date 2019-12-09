import sys
args = sys.argv


with open("hightemp.txt",'r') as f:
    for text in f.readlines()[:int(args[1])]:
        print(text,end='')