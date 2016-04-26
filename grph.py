#opens and reads a fasta file (filename), returns dictionary mapping each
#title (>...) to its corresponding protein sequence.
def read_sequences(filename):
    f=open(filename)
    lines=f.readlines()
    f.close()
    titles={}
    for i in lines:
        if i[0]==">":
            title=i[1:-1]
            titles[title]=""
        else:
            titles[title]+=i.replace("X","A")[:-1]
    return titles

def make_graph(f):
    seqs=read_sequences(f)
    S=seqs.keys()
    for seq1 in S:
        for seq2 in S:
            if seqs[seq1]!=seqs[seq2] and seqs[seq1][-3:]==seqs[seq2][:3]:
                print seq1, seq2
make_graph("DATASETS/rosalind_grph.txt")
                
