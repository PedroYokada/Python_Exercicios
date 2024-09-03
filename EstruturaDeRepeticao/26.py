""" Numa eleição existem três candidatos. 
Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. """

a = 0
b = 0
c = 0
voto_nulo = 0

eleitores = int(input("Insira o numero de eleitores: "))

candidato = input("Insira para 1 para votar no Candidato A/ 2 no B , 3 no C.")

for i in range(1,eleitores):
  candidato = input("Insira para 1 para votar no Candidato A/ 2 no B , 3 no C.")
  if candidato == "1":
    a += 1
  elif candidato == "2":
    b += 1
  elif candidato == "3":
    c += 1
  else:
    voto_nulo += 1
    
print(f"O candidato A recebeu {a} votos!")
print(f"O candidato B recebeu {b} votos!")
print(f"O candidato C recebeu {c} votos!")
print(f"Os votos anulados foi de: {voto_nulo} votos!")
    
