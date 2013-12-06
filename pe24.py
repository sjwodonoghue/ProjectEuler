# pe24.py

import itertools


def lex_perm(n):
    l = []
    for i in range(n+1):
        l.append(i)
    print l

    # The following puts all of the permutation of the elements of l into a list (also to be called l)
    # This feature also puts them into lexicographic order
    l = list(itertools.permutations(l))         
    print len(l)
    return l

l = lex_perm(9)
print l[999999]


# convert into a more readable string
ans = ''
for i in (l[999999]):
    ans += str(i)

print ans
