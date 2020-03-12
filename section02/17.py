s = set()
with open("hightemp.txt",'r') as f:
    for text in f.readlines():
        text = text.split('\t')
        s.add(text[0])


print(s)