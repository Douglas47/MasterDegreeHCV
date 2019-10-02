import collections

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

""" USER INPUT """

patient = open("Patient","r")
patient_sequence = ""
patient_name = ""
for linha in patient:
    linha = linha.replace("\n","")
    if linha.startswith(">"):
        name = linha[1:]
        name = name.split()
        name = name[0]
        patient_name = name
    else:
        linha = linha.replace("\n","")
        patient_sequence += linha
print(patient_name)
print(patient_sequence)
patient_info = []
for ras in Resistance:
    resistant = False
    """Position"""
    codon = patient_sequence[(ras*3)-3:(ras*3)]
    """Codon"""
    AminoAcid = codontable[codon] 
    """AminoAcid"""
    if AminoAcid in Resistance[ras]:
        """Resistance Check"""
        resistant = True
    patient_info.append([ras,codon,AminoAcid,resistant])
patient_file = open ("patient_info","w")
for x in patient_info:
    x = str(x)
    x = x[1:-1]
    x = x.replace("\'","")
    patient_file.write(x + "\n")
patient_file.close()

















    
