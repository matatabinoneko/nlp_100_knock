with open("hightemp.txt",'r') as f:
    text = f.readlines()
    for i in range(len(text)):
        text[i] = text[i].split('\t')
    text = sorted(text,key=lambda x:x[2],reverse=True)

    for i in range(len(text)):
        text[i] = '\t'.join(text[i])

for i in range(len(text)):
    print(text[i],end='')
