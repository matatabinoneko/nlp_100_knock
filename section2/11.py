with open("hightemp.txt","r") as f:
    for text in f.readlines():
        print(text)
        text = text.replace('\t',' ')
        print(text)