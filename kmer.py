import itertools
def read_kmer(filename):
    f=open(filename)
    lines=f.readlines()
    f.close()
    line=1
    reference=""
    while line<len(lines):
        if lines[line][-1]=="\n":reference+=lines[line][:-1]
        else:reference+=lines[line]
        line+=1
    return reference
r=read_kmer("DATASETS/rosalind_kmer.txt")

lex=list(itertools.product("ACGT",repeat=4))
def concat(x):
    s=""
    for i in x: s+=i
    return s

def mycount(x,sub):
    c=0
    s=0
    while s<=len(x)-len(sub):
        if x[s:s+len(sub)]==sub:c+=1
        s+=1
    return c

counts=[mycount(r,concat(i)) for i in lex]
result=""
for i in counts:
    result+= str(i)+" "

print result[:-1]
