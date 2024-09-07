""" "Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
" """
a = 0
b = 0
c = 0
d = 0
nulo = 0
branco = 0
voto = 0


while True:
  
  voto = int(input("Digite 1 para votar em A, 2 em B, 3 em C, 4 em D, 5 para nulo, 6 em branco e 7 para finalizar: "))

  if voto == 1:
    a += 1
  elif voto == 2:
    b += 1
  elif voto == 3:
    c += 1
  elif voto == 4:
    d += 1
  elif voto == 5:
    nulo += 1
  elif voto == 6:
    branco += 1
  elif voto == 7:
    print("Votação encerrada!")
    break
  else:
    print("Valor inválido!")


total_votos = float(a + b + c + d + branco + nulo)

print(f"O candidato A recebeu: {a} votos!")
print(f"O candidato B recebeu: {b} votos!")
print(f"O candidato C recebeu: {c} votos!")
print(f"O candidato D recebeu: {d} votos!")
print(f"A quantidade de votos nulo foram: {nulo} votos!")
print(f"A quantidade de votos em branco foram: {branco} votos!")
print(f"A percetagem de votos nulo foi de: {(nulo/total_votos) * 100:.2f}%")
print(f"A percetagem de votos em branco foi de: {(branco/total_votos) * 100:.2f}%")
