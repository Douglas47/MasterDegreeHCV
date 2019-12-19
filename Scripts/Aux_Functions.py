""" FUNCTIONS MODULE """

from Global_Variables import *


""" Functions """

def intermediaries(codon, rcodon):
   """ Generator of Intermediaries """
   codon = codon.upper()
   rcodon = rcodon.upper()
   codon_inter = []
   codon_inter.append(codon[:2] + rcodon[2])
   codon_inter.append(codon[0] + rcodon[1:])
   codon_inter.append(rcodon[0] + codon[1:])
   codon_inter.append(rcodon[:2] + codon[2])
   codon_inter.append(codon[0] + rcodon[1] + codon[2])
   codon_inter.append(rcodon[0] + codon[1] + rcodon[2])
   codon_inter.append(rcodon[:])
   return(codon_inter)                      


""" Nucleotide Nitrogen Base Group """

Nucleotides_types = {"A":"Purina","G":"Purina","T":"Pirimidina","C":"Pirimidina"}


""" Compare Two Nucleotides """

def nt_distance(nt_1,nt_2):
    if nt_1 == nt_2:
        return 0
    else:
        if Nucleotides_types[nt_1] == Nucleotides_types[nt_2]:
            return 1
        else:
            return 2.5

""" Calculates Genetic Barrier """

def genetic_barrier(codon_1,codon_2):
    codon_1 = codon_1.upper()
    codon_2 = codon_2.upper()
    position = 0
    valor = 0
    for nt in codon_1:
        valor += nt_distance(nt,codon_2[position])
        position += 1
    return valor
     
    
""" This function prints in a more organized way the informations about the sequences """
        
def List_Info_Seqs(Data_Seq):
    Frequencies = collections.OrderedDict()
    for Sequence in Data_Seq:
        print("Sequence: %s " % Sequence[0])
        for info_seq in Sequence[1]:
            print("Position: %s " % info_seq[0])
            if info_seq[1] not in Frequencies:
                Frequencies[info_seq[1]] = 0
            Frequencies[info_seq[1]] += 1
            print("codon: %s AminoAcid: %s Resistance: %r" % (info_seq[1],info_seq[2],info_seq[3]))
            
            
