n  = int(input())
dictionary = {}

for _ in range(n):
    word1, word2 = input().split()
    dictionary[word1] = word2
    dictionary[word2] = word1


word_new = input()

if word_new in dictionary:
    print(dictionary[word_new])
else:
    print(word_new)
