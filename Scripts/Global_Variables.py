""" GLOBAL VARIABLES MODULE """

import pandas as pd
import collections


""" Global Variables"""

Nucleotides = ["A", "T", "C" , "G"]



""" Direct-Acting Antivirals Agents  """

drugs_3letters = {
    "ASV":"asunaprevir",
    "DCV":"daclatasvir",
    "DSV":"dasabuvir",
    "EBR":"elbasvir",
    "GZR":"grazoprevir",
    "LDV":"ledipasvir",
    "NSV":"nebusvir",
    "OMV":"ombitasvir",
    "PIB":"pibrentasvir",
    "PTV":"paritaprevir",
    "SOF":"sofosbuvir",
    "VEL":"velpatasvir",
    "VOX":"voxilaprevir"
}



""" CODON USAGE """

codon_usage_table = pd.read_csv("../Data/Codon_Usage.csv", delimiter = ";")
codon_usage_g1 = dict(zip(list(codon_usage_table['Codon']), list(codon_usage_table['HCV-G1'])))
codon_usage_g3 = dict(zip(list(codon_usage_table['Codon']), list(codon_usage_table['HCV-G3'])))


""" GENETIC CODE """

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


""" POSITION LIST """

positions_list = (24,28,29,30,31,32,54,58,92,93) 

""" Nucleotide Nitrogen Base Group """

Nucleotides_types = {"A":"Purina","G":"Purina","T":"Pirimidina","C":"Pirimidina"}
