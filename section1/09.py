import numpy as np

def parse(s):
    s = s.replace('.','')
    s = s.replace(',','')
    s = s.replace(': ','')
    s = s.split(' ')
    return s

def shuffle(word):
    shuffle_word = ''
    shuffle_order = np.random.permutation(len(word))
    for i in shuffle_order:
        shuffle_word += word[i]
    return shuffle_word

if __name__ == "__main__":
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."
    word_list = parse(sentence)
    print(word_list)
    for i in range(len(word_list)):
        if(4<len(word_list[i])):
            word_list[i] = shuffle(word_list[i])
    print(word_list)