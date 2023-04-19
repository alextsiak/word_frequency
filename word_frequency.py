'''
word_frequency.py

Finds the most frequent words in a text file, as well as the number of total and unique words.

'''

import string

fin = open('160-0.txt', encoding="utf8") #book
fin2 = open('words.txt', encoding="utf8") #word list
begin = False
total_words = 0
unique_words = 0
words_hist = dict()
word_list = []

def most_frequent(d): #finds the most frequent words
    t = []
    for x, freq in d.items():
        t.append((freq, x))
    t.sort(reverse=True)
    res = []
    for freq,x in t:
        res.append(x)
    return res

for line in fin:
    if line.startswith('***'):
        begin = True
    if begin == True:
        words = line.split() #this is a list
        for word in words:
            stripped_word = word.strip(string.whitespace).translate(str.maketrans('', '', string.punctuation)).lower()
            total_words += 1
            words_hist[stripped_word] = words_hist.get(stripped_word, 0) + 1

def words_histogram():
    return words_hist

for value in words_hist:
    unique_words += 1   

#finds the unique words that aren't in a word list
'''def notInWordList():
    for line in fin2:
        word = line.strip()
        word_list.append(word)
    for value in words_hist:
        if value not in word_list:
            print(value)'''

def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res


#finds the most frequent words in the text
f_words = []
for x in range(20):
    f_words.append(most_frequent(words_hist)[x])

print(f"The number of total words is {total_words}. The number of unique words is {unique_words}")
print(f"The most frequent words are: {f_words}")

