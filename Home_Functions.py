""" FUNÇÕES QUE UTILIZO NO PROGRAMA PRINCIPAL, MAS NÃO TENHO UM TÍTULO MELHOR """



""" Global Variables"""

Nucleotides = ["A", "T", "C" , "G"]

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

def genetic_barrier(codon):
    Nucleotides = ["A", "T", "C" , "G"]
    codon = codon.upper()
    List_1 = []
    """List all possible codons by changing the first nucleotide """
    List_2 = []
    """List all possible codons by changing the second nucleotide"""
    List_3 = []
    """List all possible codons by changing the third nucleotide"""
    Scores_1 = {}
    """
    Scores of the alterations in the first nucleotide
    
    Key = Reference Nucleotide in the first position + 0 (the position) + Altered Nucleotide in the first position
    
    Example:  'A0T': 2.5

    Value = Genetic Barrier until this step

    """
    Scores_2 = {}
    """
    Added alteration score in the first and second positions
    
    Key = Reference Nucleotide in the first position + 0 (position) + Altered Nucleotide in the first position
    + Reference Nucleotide in the second position + 1 (position) + Altered Nucleotide in the second position
    
    Example: 'A0CC1T': 3.5

    Value = Genetic Barrier until this step

    """
    Scores_3 = {}

    """
    All the 64 possible altered codons from the reference codon

    Key: Altered Nucleotide

    Value: Genetic Barrier Score

    This is the dictionary returned from the function.

    """
    
    """Substitution of the First Nucleotide"""
    
    if codon[0] == "A":
        """ The first step is to know what Nucleotide is in the position"""
        for N in Nucleotides:
            score = 0
            codon_0 = (codon[0].replace(codon[0], N)) + codon[1:]
            """Here, the algorithm replace the nucleotide with all the 4 DNA nucleotides, including the same one"""
            List_1.append(codon_0)
            if codon_0[0] == "T" or codon_0[0] == "C":
                """Then, a score is give based on the nature of the substitution, Transition or Transversion. For the same one the score remains the same."""
                score += 2.5
            elif codon_0[0] == "G":
                score += 1
            Scores_1[codon[0] + "%d" % 0 + codon_0[0]] = score
            """The respective score is stored with the altered codon in a dictionary | altered codon : score"""
            """The process repeats for all the 4 nucleotides possibles in the 3 positions, resulting in 64 possibilities"""
    elif codon[0] == "T":
        for N in Nucleotides:
            score = 0
            codon_0 = (codon[0].replace(codon[0], N)) + codon[1:]
            List_1.append(codon_0)
            if codon_0[0] == "A" or codon_0[0] == "G":
                score += 2.5
            elif codon_0[0] == "C":
                score += 1
            Scores_1[codon[0] + "%d" % 0 + codon_0[0]] = score
    elif codon[0] == "C":
        for N in Nucleotides:
            score = 0
            codon_0 = (codon[0].replace(codon[0], N)) + codon[1:]
            List_1.append(codon_0)
            if codon_0[0] == "A" or codon_0[0] == "G":
                score += 2.5
            elif codon_0[0] == "T":
                score += 1
            Scores_1[codon[0] + "%d" % 0 + codon_0[0]] = score
    elif codon[0] == "G":
        for N in Nucleotides:
            score = 0
            codon_0 = (codon[0].replace(codon[0], N)) + codon[1:]
            List_1.append(codon_0)
            if codon_0[0] == "T" or codon_0[0] == "C":
                score += 2.5
            elif codon_0[0] == "A":
                score += 1
            Scores_1[codon[0] + "%d" % 0 + codon_0[0]] = score

    """Substitution of the Second Nucleotide"""
            
    for C in List_1:               
            if C[1] == "A":
                for N in Nucleotides:
                    codon_1 = C[0] +(C[1].replace(C[1], N)) + C[2]
                    score_2 = Scores_1[codon[0] + "%d" % 0 + C[0]]
                    List_2.append(codon_1)
                    if codon_1[1] == "T" or codon_1[1] == "C":
                        score_2 += 2.5 
                    elif codon_1[1] == "G":
                        score_2 += 1
                    Scores_2[codon[0] + "%d" % 0 + C[0] + codon[1] + "%d" % 1 + codon_1[1]] = score_2
            if C[1] == "T":
                for N in Nucleotides:
                    codon_1 = C[0] +(C[1].replace(C[1], N)) + C[2]
                    score_2 = Scores_1[codon[0] + "%d" % 0 + C[0]]
                    List_2.append(codon_1)
                    if codon_1[1] == "A" or codon_1[1] == "G":
                        score_2 += 2.5 
                    elif codon_1[1] == "C":
                        score_2 += 1
                    Scores_2[codon[0] + "%d" % 0 + C[0] + codon[1] + "%d" % 1 + codon_1[1]] = score_2
            if C[1] == "C":
                for N in Nucleotides:
                    codon_1 = C[0] +(C[1].replace(C[1], N)) + C[2]
                    score_2 = Scores_1[codon[0] + "%d" % 0 + C[0]]
                    List_2.append(codon_1)
                    if codon_1[1] == "A" or codon_1[1] == "G":
                        score_2 += 2.5 
                    elif codon_1[1] == "T":
                        score_2 += 1
                    Scores_2[codon[0] + "%d" % 0 + C[0] + codon[1] + "%d" % 1 + codon_1[1]] = score_2
            if C[1] == "G":
                for N in Nucleotides:
                    codon_1 = C[0] +(C[1].replace(C[1], N)) + C[2]
                    score_2 = Scores_1[codon[0] + "%d" % 0 + C[0]]
                    List_2.append(codon_1)
                    if codon_1[1] == "T" or codon_1[1] == "C":
                        score_2 += 2.5 
                    elif codon_1[1] == "A":
                        score_2 += 1
                    Scores_2[codon[0] + "%d" % 0 + C[0] + codon[1] + "%d" % 1 + codon_1[1]] = score_2
                    
    """Substitution of the Third Nucleotide"""
                    
    for C in List_2:
            if C[2] == "A":
                for N in Nucleotides:
                    codon_2 = C[0:2] +(C[2].replace(C[2], N))
                    score_3 = Scores_2[codon[0] + "%d" % 0 + C[0] + codon[1] + "%d" % 1 + C[1]]
                    List_3.append(codon_2)
                    if codon_2[2] == "T" or codon_2[2] == "C":
                        score_3 += 2.5
                    elif codon_2[2] == "G":
                        score_3 += 1
                    Scores_3[codon_2] = score_3
            elif C[2] == "T":
                for N in Nucleotides:
                    codon_2 = C[0:2] +(C[2].replace(C[2], N))
                    score_3 = Scores_2[codon[0] + "%d" % 0 + C[0] + codon[1] + "%d" % 1 + C[1]]
                    List_3.append(codon_2)
                    if codon_2[2] == "A" or codon_2[2] == "G":
                        score_3 += 2.5
                    elif codon_2[2] == "C":
                        score_3 += 1
                    Scores_3[codon_2] = score_3
            elif C[2] == "C":
                for N in Nucleotides:
                    codon_2 = C[0:2] +(C[2].replace(C[2], N))
                    score_3 = Scores_2[codon[0] + "%d" % 0 + C[0] + codon[1] + "%d" % 1 + C[1]]
                    List_3.append(codon_2)
                    if codon_2[2] == "A" or codon_2[2] == "G":
                        score_3 += 2.5
                    elif codon_2[2] == "T":
                        score_3 += 1
                    Scores_3[codon_2] = score_3
            elif C[2] == "G":
                for N in Nucleotides:
                    codon_2 = C[0:2] +(C[2].replace(C[2], N))
                    score_3 = Scores_2[codon[0] + "%d" % 0 + C[0] + codon[1] + "%d" % 1 + C[1]]
                    List_3.append(codon_2)
                    if codon_2[2] == "T" or codon_2[2] == "C":
                        score_3 += 2.5
                    elif codon_2[2] == "A":
                        score_3 += 1
                    Scores_3[codon_2] = score_3
    return (Scores_3)
    """This is the dictionary that will be returned from the function"""
    
""" Dictionary for not having to calculate every time """
Genetic_Barrier_Scores = {}
for x in Nucleotides:
    for y in Nucleotides:
        for z in Nucleotides:
           Genetic_Barrier_Scores[x+y+z] = genetic_barrier(x+y+z)
           
""" Genetic Barrier Calculator """ 
def Genetic_Barrier_Calc(first_codon,second_codon):
    first_codon = first_codon.upper()
    second_codon = second_codon.upper()
    try:
        print ("Genetic Barrier: %s -> %s = %.1f" % (first_codon,second_codon,Genetic_Barrier_Scores[first_codon][second_codon]))
    except:
        print ("Invalid codons!")
        
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
