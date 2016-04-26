def revcomp(s):
    sc=""
    for i in range(1,len(s)+1):
        if s[-i]=="T":sc+="A"
        if s[-i]=="A":sc+="T"
        if s[-i]=="G":sc+="C"
        if s[-i]=="C":sc+="G"
    return sc

def rev_pal(seq):
    n=len(seq)
    s1=seq[:n/2]
    s2=revcomp(seq[n/2:])
    if s1==s2:return True
    else: return False

s="ATATAGGATCGTGAAACACGGTGTGAGGTCAGGTTGGAGGCCCAAAGATTAGATGTGCCTATCTTCAAGGCCGCGCTAGGTGGTAACTCGCCGTGTACACCACTGCCTCCAAATCTCTGGCATCACGATAGGTAACGCTAAGAGGAGGACTCCCGACTCACGCCAACTGAATTCCGTTCCAACACGAGGGGCTTGTCCACAGGTCGTAATCAAAAAATTGGTGAAACATCGTAATAGGTAATCTCAATGATCCGCTTTAGTCTCCGCGCTCGGTCCGCACATCAGTTCGAAATGCCACGTAGGGGGTGTGGGAGCCGATCCGATATCCTAGTATCCTCAGCTCAGCCTCTTAAACGAGCCTAGCGGAAAACTTACATGGACATTTTGCTCGCCCGTTGTCTGGGATGTGTGACTACGTTTCCGAATATTTGATTAGCTAAGGCTGATCGTGTCCCGTTTCCTTAGAATCAGTCTAACTCCCGGGAGTCATTTGATCAGGTACCCTCGTAAAAGCATCGGCTACAACTCTAAAACTTTGTGGCTCTCCTCCACAGAGTGGTTATCCTGTAGTGCGGTAAAGTGTTATTTAATACGCCTGAACACCAATGTCCCCTCCGCTAGTGTGTACACCCAGGCCTGAGTCGGCTACCTAGCCCTTATAGCTTAGCACTTTGGTACACTTTCCGCGCAGTAGGATGACACCGCCACCCTCGAACAGAGGCTATGTGTGTGTCACACGACTCGCCGTGGTGTTTTGCATGCTTGAGGTGTCACTCTTGGCAGCCCGTCGGTCAGTACTTTTATCACATAGAGGATATGATATCGCGTAGGTCAGTGTGGGATATGAAAGGGGGCGACGAAAGTCATATACATGCAGCTGGTACAGGTCTCCTGGACGGGACGGAACGTCCACTCATCGCTTGTGACTGAGCCGAACTTAACAAAGCACCCAATGTCTTATA"

def find_revp(seq):
    for i in range(0,len(seq)-3):
        for pallen in range(4,13,2):
            j=i+pallen
            if j<=len(seq):
                s=seq[i:j]
                if rev_pal(s):
                    print i+1,pallen
                
find_revp(s)
