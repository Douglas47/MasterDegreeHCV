import Home_Functions as auxfunction
""" Open the patient file"""

paciente = open("patient_info")
""" List of all Genotypes Availables"""
Genotypes = {"1a": "Frequência_Genótipo 1a", "1b":"Frequência_Genótipo 1b", "3":"Frequência_Genótipo 3"}
paciente_info = []
""" Convert the patient data - String to List of Strings"""
for info in paciente:
   info_clean = info.replace("\'","")
   info_clean = info_clean.replace("\n", "")
   paciente_info.append(info_clean.split(","))
""" Here the user have to input the Patient Genotype"""
while True:
   p_genotype = input("Genótipo (1a, 1b ou 3):")
   if p_genotype not in Genotypes:
      print ("Genótipo não identificado")
   else:
      break
""" Opens the population file for the input genotype"""
population = open(Genotypes[p_genotype])
Pop_positions = {}
for x in population:
   x = x.replace("\n","")
   x = x.replace("Position ", "")
   x = x.split(",")
   if x[0] not in Pop_positions:
      Pop_acumulador = []
   Pop_acumulador.append(x[1:])
   Pop_positions[x[0]] = Pop_acumulador
for data in Pop_positions.items():
   """ Position """
   print(data[0])
   """ Codon data """
   for codon_data in data[1]:
      print(codon_data)
print("-------------------------------------------")
print(paciente_info)
print("-----------------")
paciente_dict = {}
for position in paciente_info:
   paciente_dict[position[0]] = position[1:]
print(paciente_dict)
print("-----------------")
for position in paciente_dict:
   print("*****************")
   print(position)
   print(paciente_dict[position])
   print(Pop_positions[position])

      
   
