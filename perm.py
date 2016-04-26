import itertools
k=5
perms=list(itertools.permutations(range(1,k+1)))

print len(perms)
for i in perms:
    x=""
    for j in i: x+=str(j)+" "
    print x
