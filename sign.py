n=6

import itertools

perms=list(itertools.permutations(range(1,n+1)))

combs=list(itertools.product([1,-1],repeat=n))

com=[]
for p in perms:
    for c in combs:
        x=[str(c[i]*p[i]) for i in range(0,n)]
        com.append(" ".join(x))

print len(com)
for i in com: print i
