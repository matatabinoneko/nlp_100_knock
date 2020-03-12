import sys
args = sys.argv


with open("hightemp.txt",'r') as f:
    text = f.readlines()
    length = len(text)
    for text in text[len(text)-int(args[1]):]:
        print(text,end='')
