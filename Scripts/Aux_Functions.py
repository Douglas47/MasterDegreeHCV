""" FUNCTIONS MODULE """

from Global_Variables import *

""" FUNCTIONS """


""" Intermediaries between two codons """

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
    try:
        codon_1 = codon_1.upper()
        codon_2 = codon_2.upper()
        position = 0
        valor = 0
        for nt in codon_1:
            valor += nt_distance(nt,codon_2[position])
            position += 1
        return valor
    except:
        return 0
     
    
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
     
""" Transforma um arquivo fasta em um dicionário """
    
def fasta_to_dict(file):
    fasta_file = open(file)
    output_dict = {}
    for line in fasta_file:
        line = line.replace("\n","")
        if line.startswith(">"):
            sequence = ""
            name = line[1:]
            name = name.split()
            name = name[0]
            """Acession Number"""
        else:
            sequence += line
            """Sequence"""
        output_dict[name] = sequence
    return(output_dict)

""" Retorna um dicionário com as posições e os codons """

def sequence_codons(sequence):
    codons = {}
    for position in positions_list:
        codon = sequence[(position*3)-3:(position*3)]
        codons[position] = codon
    return(codons)
            
""" Retorna os codons de cada aminoácido """   

def aa_to_codons(aa):
    codons = []
    for item in codontable.items(): 
        if item[1] == aa: 
           codons.append(item[0])
    return codons


def codons_row(row):
    row["Codons"] = aa_to_codons(row['AminoAcid'])
    return row