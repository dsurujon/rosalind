f=open("DATASETS/rosalind_tree.txt")
tree=f.readlines()
f.close()

n=int(tree[0])
trenum=[x[:-1].strip("\n").split(" ") for x in tree[1:]]

nums=[]
for x in trenum:
    for j in x:nums.append(int(j))
    
totcounts=0
for i in range(n+1):
    totcounts+=nums.count(i)

print (n-1)-(totcounts/2)
