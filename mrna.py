protein="MA"

codon_table={"F":2,"L":6,"I":3,"M":1,"V":4,"S":6,"P":4,"T":4,
              "A":4,"Y":2,"Stop":3,"H":2,"N":2,"Q":2,"K":2,"D":2,
              "E":2,"C":2,"W":1,"R":6,"G":4}
def mrna(prot):
    perms=1
    for i in prot:
        perms*=codon_table[i]
        if perms>=1000000:
            perms=perms%1000000
    perms=(perms*3)%1000000
    return perms
