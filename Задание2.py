n  = int(input())
translate = {}
result = []

for _ in range(n):
    russian, english = input().split()
    translate[russian] = english

sentence = input().split()
for word in  range(len(sentence)):
    if sentence[word] in translate:
        result.append(translate[sentence[word]])
    else:
        result.append(sentence[word])

print(' '.join(result))
