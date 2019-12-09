col1 = ''
col2  = ''
with open("hightemp.txt",'r') as f, open("col1.txt", 'w') as c1 , open("col2.txt",'w') as c2:
    for text in f.readlines():
        text = text.split('\t')
        col1 += text[0] + '\n'
        col2 += text[1] + '\n'

    c1.write(col1)
    c2.write(col2)