n = int(input())
dictionary = {}

for _ in range(n):
    forma, *figures = input().split()
    dictionary[forma] = figures

thing = input()

for shape, things in dictionary.items():
    if thing in things:
        print(shape)
