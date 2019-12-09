def word_n_gram(type,s,n):
    if(type=="string"):
        string_n_dict = {}
        for i in range(0,len(s)-n+1):
            if(s[i:i+n] in string_n_dict.keys()):
                string_n_dict[s[i:i+n]] += 1
            else:
                string_n_dict[s[i:i+n]] = 1

        return string_n_dict
    else:
        word_n_dict = {}
        s = s.replace('.','')
        s = s.replace(',','')
        s = s.split(' ')
        for i in range(0,len(s)-n+1):
            key = ' '.join(s[i:i+n])
            if(key in word_n_dict.keys()):
                word_n_dict[key] += 1
            else:
                word_n_dict[key] = 1
        return word_n_dict
        
# print(word_n_gram(type="string",s="きしゃがきしゃにきしゃできしゃした",n=1))
print(word_n_gram(type="string",s="I am an NLPer",n=2))
print(word_n_gram(type="word",s="I am an NLPer",n=2))