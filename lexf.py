import itertools

f=open("DATASETS/rosalind_lexf.txt")
lines=f.readlines()
f.close()

letters=lines[0][:-1].split(" ")
n=int(lines[1])

x=itertools.product(letters,repeat=n)

y=list(map("".join,x))

for i in y:print i
