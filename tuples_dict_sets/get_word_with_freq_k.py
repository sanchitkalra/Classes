sentence = "this is a word string having many many word"
k = 2

words = sentence.split()
words_d = {}

# basic solution
# for word in words:
#     if word in words_d:
#         words_d[word] += 1
#     else:
#         words_d[word] = 1

# better solution
for word in words:
    words_d[word] = words_d.get(word, 0) + 1

print(words_d)

# print all words with frequency k
for word in words_d:
    if words_d[word] == k:
        print(word)

# create a function to do the same
def printWords(sentence, k):
    words = sentence.split()
    words_d = {}
    for word in words:
        words_d[word] = words_d.get(word, 0) + 1
    for word in words_d:
        if words_d[word] == k:
            print(word)

printWords(sentence, k)