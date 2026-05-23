text = input().split()
string = {}

for word in text:
    string[word] = string.get(word, 0) + 1

words = list(string.keys())

n = len(words)
for i in range(n - 1):
    for j in range(n - i - 1):
        if string[words[j]] < string[words[j + 1]]:
            # Changing names
            words[j], words[j + 1] = words[j + 1], words[j]

for word in words:
    print(word)
