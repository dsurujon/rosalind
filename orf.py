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
    for i in range(0,len(r)/3):
        amino=codon_table[r[3*i:3*i+3]]
        if amino=="Stop":
            stop=1
            break
        peptide+=amino
    if stop==1: return peptide
    else: return 

#find the start codons in the dna sequence and translate until
#the stop codon
def find_starts(r):
    z=0
    l=[0]
    dna=r
    peptides=[]
    while z>=0:
        z=dna[1:].find("ATG")
        pep=dna_translate(dna[z+1:])
        if pep!=None :peptides.append(pep)
        dna=dna[z+1:]
    return peptides
    

#generate the reverse complement of a DNA sequence
def revcomp(s):
    sc=""
    for i in range(1,len(s)+1):
        if s[-i]=="T":sc+="A"
        if s[-i]=="A":sc+="T"
        if s[-i]=="G":sc+="C"
        if s[-i]=="C":sc+="G"
    return sc

#find protein sequences for both forward and reverse strands
#display only unique peptide sequences
def find_prots(d):
    p=find_starts(d)
    p+=find_starts(revcomp(d))
    for i in set(p): print i

find_prots("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")

