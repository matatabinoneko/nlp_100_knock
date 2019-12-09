import sys
args = sys.argv

# text_list = [[]for i in range(int(args[1]))]
# with open("hightemp.txt",'r') as f:
#     text = f.readlines()
#     for i in range(len(text)):
#         text_list[i%int(args[1])].append(text)

# for i in range(len(text_list)):
#     for j in range(len(text_list[i])):
#         for k in range(len(text_list[i][j])):
#             print(text_list[i][j][k],end='')
#     print()
    

text_list = [[]for i in range(int(args[1]))]
with open("hightemp.txt",'r') as f:
    text = f.readlines()
    for i in range(len(text)):
        text_list[i%int(args[1])].append(text)