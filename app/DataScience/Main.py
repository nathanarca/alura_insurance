import numpy as np

km = np.loadtxt("c:\\NAC\\alura_insurance\\app\\DataScience\\data\\carros-km.txt")

anos = np.loadtxt("c:\\NAC\\alura_insurance\\app\\DataScience\\data\\carros-anos.txt", dtype=int)

km_media = km / (2023 - anos)

#type(km_media)

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

a1 = letras[:2]
print(a1)

a2 = letras[2:5]

print(a2)

a3 = letras[-3:]

print(a3)