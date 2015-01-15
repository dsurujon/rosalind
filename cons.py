#for the following problem
# http://rosalind.info/problems/cons/
 
#opens and reads a fasta file (filename), returns dictionary mapping each
#title (>...) to its corresponding protein sequence.
def read_sequences(filename):
    f=open(filename)
    lines=f.readlines()
    f.close()
    titles={}
    for i in lines:
        if i[0]==">":
            title=i[:-1]
            titles[title]=""
        else:
            titles[title]+=i.replace("X","A")[:-1]
    return titles
 
 
def transpose(m):           #Transpose a matrix
 
    mT=[['' for j in m] for x in m[0]]
    for i in range(0,len(m[0])):
        for j in range(0,len(m)):
            mT[i][j]=m[j][i]
            
    return mT
 
def generate_profile(f):
    seqs=read_sequences(f)
    l=len(seqs.values()[1])
    P={'A':[0 for i in range(0,l)],
       'C':[0 for i in range(0,l)],
       'G':[0 for i in range(0,l)],
       'T':[0 for i in range(0,l)]}
    #transposed matrix for sequences
    s=[[j for j in i] for i in seqs.values()]
    s_=transpose(s)
    consensus=""
    for i in range(0,len(s_)):
        maxcount=0
        best_nuc=""
        for nuc in P.keys():
            nuc_count=s_[i].count(nuc)
            P[nuc][i]=nuc_count
            if nuc_count>maxcount:
                maxcount=nuc_count
                best_nuc=nuc
        consensus+=best_nuc
    return P,consensus
 
P,c=generate_profile("DATASETS/rosalind_cons.txt")
print c
for i in ["A","C","G","T"]: print i,":", " ".join([str(j) for j in P[i]])
