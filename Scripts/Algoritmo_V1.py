"""
MESTRADO - DOUGLAS DE ANDRADE DE ALMEIDA

TÍTULO: ALGORITMO DE PREDIÇÃO DE DESENVOLVIMENTO DE RESISTÊNCIA
DO VÍRUS DA HEPATITE C (HCV) AOS ANTIVIRAIS DE AÇÃO DIRETA

FEVEREIRO/2018

"""
"""

Genetic Barrier

"""
import collections
"A module that implements specialized container datatypes. Ex: Ordered Dictionaries"
import json
"JavaScript Object Notation - a lightweight data interchange format"
import Home_Functions as AuxFile

import numpy as np

"""Global Variables"""
Nucleotides = ["A", "T", "C" , "G"]
    
""" Resistance Table """

Resistance = collections.OrderedDict()
Resistance[28] = ['T','V','A','S']
Resistance[29] = ['S'],
Resistance[30] = ['E','H','R','D','G','K','T','Q','P','S'], 
Resistance[31] = ['M','I','V','F'],
Resistance[32] = ['L'],
Resistance[58] = ['D','S'],
Resistance[92] = ['K'],
Resistance[93] = ['H','N','C','S']


""" Genetic Code """

codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

""" Open fasta file & Acession Number e Sequence """

All_database = {}


Datasets_Reference = [("NS5A_1b_06.03.2018.aln","1b"),
                     ("NS5A_GEN1a_02.05.16","1a"),
                     ("NS5A_GEN3_05.05.16","3"),
                      ("LISTA_TESTE.txt","TESTE")]

for dataset in Datasets_Reference:
    name_dataset = dataset[0]
    genotype_dataset = dataset[1]
    All_database[genotype_dataset] = []
    fasta = open(name_dataset) 
    """The file must be in the same folder as the code"""
    Sequences = collections.OrderedDict() 
    """[Acession Number, Sequence]"""
    Data_Seq = []
    """[Sequence Name,[Position,codon,AminoAcid,Resistance(True or False)]]"""

    for linha in fasta:
        linha = linha.replace("\n","")
        if linha.startswith(">"):
            name = linha[1:]
            name = name.split()
            name = name[0]
            sequence = ""
            Data_Seq.append([name])
            """Acession Number"""
        else:
            sequence += linha
            """Sequence"""
        Sequences[name] = sequence
        
    All_database[genotype_dataset].append(Sequences)

    """ Position, codon, AminoAcid e Resistance """
    for Sequence in Data_Seq:
        codons = []
        for ras in Resistance:
            """ras = resistance associated substitutions"""
            resistant = False
            Complete_sequence = Sequences[Sequence[0]]
            """Position"""
            codon = Complete_sequence[(ras*3)-3:(ras*3)]
            """Codon"""
            AminoAcid = codontable[codon] 
            """AminoAcid"""
            if AminoAcid in Resistance[ras]:
                """Resistance Check"""
                resistant = True
            codons.append([ras,codon,AminoAcid,resistant])
        Sequence.append(codons)
    
    All_database[genotype_dataset].append(Data_Seq)
    fasta.close() 

    """ Frequency Analysis """

    Frequencies = collections.OrderedDict()
    Info_Frequency = []
    for Sequence in Data_Seq:
        for data in Sequence[1]:
            """ data = [Position, codon, AminoAcid, Resistance] """
            if "Position %d" % data[0] not in Frequencies:
                Frequencies["Position %d" % data[0]] = collections.OrderedDict()
            if data[1] not in Frequencies["Position %d" % data[0]]:
                Frequencies["Position %d" % data[0]][data[1]] = 0
            Frequencies["Position %d" % data[0]] [data[1]] += 1

    for x,y in Frequencies.items():
        """Posição"""
        for key,value in y.items():
            relative_frequency = (value/len(Data_Seq))
            Info_Frequency.append([x,key,value, relative_frequency])
    All_database[genotype_dataset].append(Info_Frequency)
    frequency_file = open("Frequência_Genótipo %s" % genotype_dataset, "w")
    print("Genótipo %s " % genotype_dataset)
    #frequencia_file.write(("Genótipo %s " % genotype_dataset) + "\n") 
    for z in Info_Frequency:
        frequency_instance = str(z)
        frequency_instance = frequency_instance.replace("\'","")
        frequency_file.write(frequency_instance[1:-1] + "\n")
    print(np.array(Info_Frequency))
    frequency_file.close()







