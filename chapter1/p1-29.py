from itertools import permutations

words = ['c','a','t','d','o','g']
perms = permutations(words)

for perm in perms:
    print(perm)
