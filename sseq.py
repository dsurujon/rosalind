def read_sseq(filename):
    f=open(filename)
    lines=f.readlines()
    f.close()
    line=1
    reference=""
    query=""
    while lines[line][0]!=">":
        reference+=lines[line][:-1]
        line+=1
    query=lines[line+1][:-1]
    return query, reference

q,r = read_sseq("DATASETS/rosalind_sseq.txt")

start=0
indices=[]
for i in range(0,len(q)):
    for j in range(start,len(r)):
        if q[i]==r[j]:
            indices.append(j)
            start=j
            break

result=""
for i in indices:
    result+= str(i+1)+" "

print result[:-1]
