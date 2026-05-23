def count_descendants(name, family_tree):
    """
    Recursively counts the number of offspring for a given name.
    :param name: name of the member in family
    :param family_tree: family tree
    :return: number of descendants
    """

    if name not in family_tree:
        return 0

    total = 0
    for child in family_tree[name]:
        # Count the offspring themselves + their descendants
        total += 1 + count_descendants(child, family_tree)
    return total


n = int(input())
family_tree = {}

for _ in range(n):
    parent, child = input().split()
    if parent not in family_tree:
        family_tree[parent] = []
    family_tree[parent].append(child)

name = input()

result = count_descendants(name, family_tree)
print(result)
