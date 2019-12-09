s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# words_list = s.split(' ')
# word_len_list = []
# for i in range(len(words_list)):
#     if(('a' <= words_list[i][-1] and words_list[i][-1] <= 'z') or ('A' <= words_list[i][-1] and words_list[i][-1] <= 'Z')):
#         None
#     else:
#         words_list[i] = words_list[i][:-1]
#     word_len_list.append(len(words_list[i]))



s = s.replace(',','')
s = s.replace('.','')
words_list = s.split(' ')
word_len_list = []
for i in range(len(words_list)):
    word_len_list.append(len(words_list[i]))
    
print(word_len_list)