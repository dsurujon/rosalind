codon_table={'TTT': 'F',      'CTT': 'L',      'ATT': 'I',      'GTT': 'V',
'TTC': 'F',      'CTC': 'L',      'ATC': 'I',      'GTC': 'V',
'TTA': 'L',      'CTA': 'L',      'ATA': 'I',      'GTA': 'V',
'TTG': 'L',      'CTG': 'L',      'ATG': 'M',      'GTG': 'V',
'TCT': 'S',      'CCT': 'P',      'ACT': 'T',      'GCT': 'A',
'TCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
'TCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
'TCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
'TAT': 'Y',      'CAT': 'H',      'AAT': 'N',      'GAT': 'D',
'TAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
'TAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
'TAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
'TGT': 'C',      'CGT': 'R',      'AGT': 'S',      'GGT': 'G',
'TGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
'TGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
'TGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G'}

#translate a dna sequence based on the codon table above
#note: if the sequence doesn't have a stop codon, it's
#not considered a valid orf. 
def dna_translate(r):
    peptide=""
    stop=0
    start=r.find("ATG")
    for i in range(start,len(r)-2,3):
        amino=codon_table[r[i:i+3]]
        if amino=="Stop":
            stop=1
            break
        peptide+=amino
    return peptide

#opens and reads a fasta file (filename), returns a list of sequences
def read_sequences(filename):
    f=open(filename)
    lines=f.readlines()
    lines.append(">")
    f.close()
    seqs=[]
    myseq=""
    for i in lines[1:]:
        if i[0]==">":
            seqs.append(myseq)
            myseq=""
        else:
            myseq+=i[:-1]
    return seqs

def dna_splice(dataset):
    dna_spliced=seqs[0]
    introns=seqs[1:]
    for intron in introns:
        dna_spliced=dna_spliced.replace(intron,"")
    return dna_spliced
    

seqs=read_sequences("DATASETS/rosalind_splc.txt")
dna=dna_splice(seqs)
peptide=dna_translate(dna)
print peptide
