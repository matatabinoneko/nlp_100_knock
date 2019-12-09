from collections import Counter


with open("hightemp.txt",'r') as f:
    print(Counter([i.split('\t')[0] for i in f.readlines()]).most_common)
    

