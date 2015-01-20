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

#find the longest subsequence that appears in all sequences
def find_common(filename):
    seqs=read_sequences(filename)
    seqs=seqs.values()
    #find shortest sequence
    lengths=[len(i) for i in seqs]
    shortest=seqs[lengths.index(min(lengths))]
    for i in range(0,len(shortest)):
        for j in range(0,i):
            common_candidate=shortest[j:j-i]
            if all(common_candidate in s for s in seqs)==True:
                return common_candidate
                

fn="DATASETS/rosalind_lcsm.txt"

x=find_common(fn)
print x
