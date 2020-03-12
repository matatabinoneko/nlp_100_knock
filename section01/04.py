s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

s = s.replace(',','')
s = s.replace('.','')
words_list = s.split(' ')
word_dict = {}
for i in range(len(words_list)):
    if (i+1 in [1,5,6,7,8,9,15,16,19]):
        word_dict[words_list[i][0]] = i+1
    else:
        word_dict[words_list[i][0:2]] = i+1

print(word_dict)